# Copyright (C) 2023 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import glob
import json
import os
import shutil
import traceback
from typing import Any

from ansys.optislang.core import Optislang
import ansys.optislang.core.node_types as node_types
from ansys.optislang.core.nodes import DesignFlow
from conftest import _OSL_INTEGRATIONS_DIR
import pytest

from ansys.conceptev.core.settings import Settings


def get_output_location_by_name(node, name):
    output_locations = node.get_available_output_locations()
    for loc in output_locations:
        if loc["location"]["name"] == name:
            return loc["location"]
    raise KeyError(f"Output location '{name}' not found.")


def register_response(node, name):
    location = get_output_location_by_name(node, name)
    node.register_location_as_response(
        location=location,
        name=name,
    )


def assert_integration_results(
    working_dir: str, debug_dir: str, project_name: str = "test_conceptev_ci"
) -> None:
    """Assert that the ConceptEV integration ran at least one job and returned results.

    The installed integration plugin (conceptev_ci.pye) uses REST polling, not
    websockets, so there are no ``Connected to OCM Websockets.`` / ``Status:``
    print markers.  Instead this function asserts on what the integration
    actually writes:

    1. ``conceptev_debug.log`` must exist and contain at least one successful
       ``get_results`` call.
    2. At least one ``Design*/conceptev/job_results.json`` must exist and
       contain at least one result entry.
    """
    opd_dir = os.path.join(working_dir, f"{project_name}.opd")

    # 1. Debug log must exist and have a successful get_results entry.
    debug_log_path = os.path.join(opd_dir, "conceptev_debug.log")
    assert os.path.exists(debug_log_path), (
        f"conceptev_debug.log not found at {debug_log_path} — "
        "the integration plugin may not have run at all."
    )
    with open(debug_log_path, encoding="utf-8", errors="replace") as fh:
        log_text = fh.read()

    succeeded_get_results = any(
        "get_results" in line and "Succeeded." in line
        for line in log_text.splitlines()
    )
    assert succeeded_get_results, (
        f"No successful get_results call found in {debug_log_path}. "
        "The ConceptEV job may have failed to return results. "
        f"See {debug_dir} for the copied log."
    )

    # 2. At least one design must have a non-empty job_results.json.
    #
    # Results land in two places depending on whether parameters were registered:
    #   - Reference-only run (no parameters): .opr/{concept_id}/job_results.json
    #   - Parameter sweep: .opd/Sensitivity/Design*/conceptev/job_results.json
    opr_dir = os.path.join(working_dir, f"{project_name}.opr")
    sensitivity_dir = os.path.join(opd_dir, "Sensitivity")
    result_files = sorted(
        glob.glob(os.path.join(opr_dir, "*", "job_results.json"))
        + glob.glob(os.path.join(sensitivity_dir, "Design*", "conceptev", "job_results.json"))
    )
    assert result_files, (
        f"No job_results.json found in {opr_dir} or {sensitivity_dir}. "
        "The ConceptEV node did not produce any design results."
    )

    all_results: list[Any] = []
    for path in result_files:
        with open(path, encoding="utf-8") as fh:
            all_results.extend(json.load(fh))

    assert all_results, (
        "job_results.json files exist but are all empty. "
        f"Files checked: {result_files}"
    )

    print(
        f"[integration-check] {len(result_files)} design(s), "
        f"{len(all_results)} total result(s) — integration ran successfully."
    )


_OSL_VERSION_QUERY = """\
import importlib.metadata as _m, json as _j, sys as _s, os as _o

_r = {}

try:
    _r['pyconceptev_version'] = _m.version('ansys-conceptev-core')
except Exception as _e:
    _r['pyconceptev_version'] = f'<not found: {_e}>'

try:
    import ansys.conceptev.core as _cev
    _r['pyconceptev_path'] = _cev.__file__
except Exception as _e:
    _r['pyconceptev_path'] = f'<not importable: {_e}>'

# Try direct import of the integration plugin to get its file path.
# Note: optiSLang uses .pye (not .py) for integration scripts and these are
# executed directly by optiSLang, not via Python's import system.  Direct
# import will therefore usually fail.  We fall back to a sys.path scan for
# any .py copy, purely for informational purposes.
try:
    import conceptev_ci as _ci
    _r['conceptev_ci_path'] = _o.path.abspath(_ci.__file__)
except Exception as _e:
    _found = [
        _o.path.join(_p, 'conceptev_ci.py')
        for _p in _s.path
        if _o.path.isfile(_o.path.join(_p, 'conceptev_ci.py'))
    ]
    _r['conceptev_ci_path'] = _found[0] if _found else f'<not found on sys.path: {_e}>'

print(_j.dumps(_r))
"""


def _query_integration_version(osl: Optislang) -> str:
    """Read INTEGRATION_VERSION from the installed conceptev_ci.pye via optiSLang's Python.

    optiSLang executes .pye files directly as scripts — they are not importable
    via Python's standard import system.  This function opens the installed
    conceptev_ci.pye as plain text inside optiSLang's run_python_script
    subprocess and extracts the INTEGRATION_VERSION marker using regex.

    Returns the version string, or an error sentinel beginning with ``<``.
    """
    import json as _json

    pye = _OSL_INTEGRATIONS_DIR / "conceptev_ci.pye"
    # Build the query as a format string so the file path is baked in.
    # Double-brace {{ }} to escape the f-string; single-brace for the version.
    query = (
        "import re as _re, json as _j\n"
        f"_pye = r'{pye}'\n"
        "try:\n"
        "    _content = open(_pye, encoding='utf-8').read()\n"
        "    _m = _re.search(\n"
        r"        r'^INTEGRATION_VERSION\s*=\s*[\"\'](.*?)[\"\']'," + "\n"
        "        _content, _re.MULTILINE,\n"
        "    )\n"
        "    _v = _m.group(1) if _m else '<not set>'\n"
        "except Exception as _e:\n"
        "    _v = f'<error: {_e}>'\n"
        "print(_j.dumps({'integration_version': _v}))\n"
    )
    try:
        stdout, stderr = osl.application.project.run_python_script(query)
        result = _json.loads(stdout.strip()) if stdout.strip() else {}
        return result.get("integration_version", "<empty response>")
    except Exception as exc:
        return f"<run_python_script error: {exc}>"


def _log_osl_runtime_versions(osl: Optislang, debug_dir: str, inject_integration=None) -> None:
    """Query version info from the live optiSLang instance and write to versions.txt.

    Uses osl.osl_version_string (property) and
    osl.application.project.run_python_script() (non-deprecated Project API) to
    surface:
      - optiSLang application version
      - pyconceptev version + path as seen by optiSLang's Python
      - Integration search directories on optiSLang's sys.path

    Always writes to <debug_dir>/versions.txt so the info is available regardless
    of pytest's stdout capture mode.

    Parameters
    ----------
    osl:
        Live optiSLang session.
    debug_dir:
        Directory to write versions.txt into.
    inject_integration:
        Path to the injected integration source directory, or None when no
        injection was performed.  Recorded in versions.txt for traceability.
    """
    import json as _json

    versions: dict[str, Any] = {
        "osl_version": osl.osl_version_string,
    }

    # Query pyconceptev version + integration dirs from optiSLang's Python runtime.
    try:
        stdout, stderr = osl.application.project.run_python_script(_OSL_VERSION_QUERY)
        if stderr.strip():
            versions["osl_script_stderr"] = stderr.strip()
        versions.update(_json.loads(stdout.strip()) if stdout.strip() else {})
    except Exception as exc:
        versions["osl_script_error"] = repr(exc)

    # Record whether integration injection was active.
    versions["integration_injected"] = str(inject_integration) if inject_integration else "no"

    # Confirm the conceptev node is registered and find which category it's in.
    try:
        available = osl.osl_server.get_available_nodes()
        conceptev_category = next(
            (cat for cat, nodes in available.items() if "conceptev" in nodes),
            "<not found in available nodes>",
        )
        versions["conceptev_node_category"] = conceptev_category
    except Exception as exc:
        versions["available_nodes_error"] = repr(exc)

    # Write to file — always visible regardless of pytest capture.
    versions_path = os.path.join(debug_dir, "versions.txt")
    with open(versions_path, "w", encoding="utf-8") as fh:
        fh.write("[versions] optiSLang runtime\n")
        for key, value in versions.items():
            fh.write(f"  {key}: {value}\n")
    print(f"[versions] written to {versions_path}")

    # Also print for -s / --capture=no runs.
    v = versions
    print(
        f"[versions]   optiSLang application      : {v.get('osl_version')}\n"
        f"[versions]   pyconceptev  (osl Python)  : {v.get('pyconceptev_version', '<unknown>')}\n"
        f"[versions]   pyconceptev path           : {v.get('pyconceptev_path', '<unknown>')}\n"
        f"[versions]   conceptev_ci.py path       : {v.get('conceptev_ci_path', '<unknown>')}\n"
        f"[versions]   conceptev node category    : {v.get('conceptev_node_category', '<unknown>')}"
    )


def get_unit_test_dir():
    unit_test_dir = os.path.join(".")
    return unit_test_dir


def get_working_dir():
    return os.path.join(get_unit_test_dir(), "test_working_dir")


def remove_non_empty_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=False, onerror=None)


def get_debug_dir(working_dir: str) -> str:
    debug_dir = os.path.join(working_dir, "debug")
    os.makedirs(debug_dir, exist_ok=True)
    return debug_dir


def _json_default(value: Any) -> str:
    return str(value)


def write_json_debug(debug_dir: str, label: str, data: Any) -> str:
    filepath = os.path.join(debug_dir, f"{label}.json")
    with open(filepath, "w", encoding="utf-8") as debug_file:
        json.dump(data, debug_file, indent=2, default=_json_default)
    print(f"[debug] wrote {filepath}")
    return filepath


def export_optislang_project_file(osl: Optislang, debug_dir: str, label: str) -> str:
    project_copy_path = os.path.join(debug_dir, f"investigation_{label}.opf")
    osl.application.save_copy(project_copy_path)
    print(f"[debug] saved optiSLang project copy to {project_copy_path}")
    return project_copy_path


def export_node_snapshot(
    osl: Optislang, node: Any, debug_dir: str, label: str, node_name: str
) -> str:
    node_snapshot = {
        "label": label,
        "node_name": node_name,
        "uid": node.uid,
        "status": node.get_status(),
        "actor_info": osl.osl_server.get_actor_info(
            uid=node.uid,
            include_log_messages=True,
            include_integrations_registered_locations=True,
        ),
        "input_locations": list(node.get_available_input_locations()),
        "output_locations": list(node.get_available_output_locations()),
    }
    try:
        node_snapshot["properties"] = osl.osl_server.get_actor_properties(node.uid)
    except Exception as exc:
        node_snapshot["properties_error"] = repr(exc)

    return write_json_debug(debug_dir, f"node_{node_name}_{label}", node_snapshot)


def write_debug_summary(
    debug_dir: str,
    label: str,
    artifacts: dict[str, str],
    error: Exception | None = None,
) -> str:
    summary_path = os.path.join(debug_dir, f"summary_{label}.txt")
    with open(summary_path, "w", encoding="utf-8") as summary_file:
        summary_file.write(f"debug stage: {label}\n")
        if error is not None:
            summary_file.write(f"error: {error!r}\n")
            summary_file.write(traceback.format_exc())
            summary_file.write("\n")
        summary_file.write("\nartifacts:\n")
        for artifact_name, artifact_path in artifacts.items():
            summary_file.write(f"- {artifact_name}: {artifact_path}\n")
    print(f"[debug] wrote {summary_path}")
    return summary_path


def collect_opd_debug_artifacts(
    working_dir: str, debug_dir: str, label: str, project_name: str = "test_conceptev_ci"
) -> dict[str, str]:
    """Read conceptev_debug.log and job result files from the optiSLang project data directory.

    The ``.opd`` directory (alongside the project ``.opf``) is where the ConceptEV
    integration writes ``conceptev_debug.log`` and per-design ``job_results.json``
    files.  This function copies the log into ``debug_dir``, walks all
    ``Design*/conceptev/`` sub-directories for result files, and writes a combined
    JSON summary.

    Returns a dict mapping artifact labels to their copied/written paths.
    """
    opd_dir = os.path.join(working_dir, f"{project_name}.opd")
    artifacts: dict[str, str] = {}

    # ---- conceptev_debug.log ------------------------------------------------
    debug_log_src = os.path.join(opd_dir, "conceptev_debug.log")
    if os.path.exists(debug_log_src):
        debug_log_dst = os.path.join(debug_dir, f"conceptev_debug_{label}.log")
        shutil.copy2(debug_log_src, debug_log_dst)
        artifacts["conceptev_debug_log"] = debug_log_dst

        with open(debug_log_src, encoding="utf-8", errors="replace") as fh:
            log_text = fh.read()

        succeeded_count = log_text.count(".. Succeeded.")
        failed_count = log_text.count(".. Failed.")
        exception_lines = [ln for ln in log_text.splitlines() if "Exception" in ln or "Error" in ln]
        print(
            f"[opd-check] conceptev_debug.log: {succeeded_count} succeeded, "
            f"{failed_count} transient failures, {len(exception_lines)} exception/error lines"
        )
        print(f"[opd-check] copied to {debug_log_dst}")
    else:
        print(f"[opd-check] conceptev_debug.log NOT found at {debug_log_src}")

    # ---- job_results.json / job_info.json per design ------------------------
    # Results land in two places:
    #   - Reference-only run (no parameters): .opr/{concept_id}/
    #   - Parameter sweep: .opd/Sensitivity/Design*/conceptev/
    opr_dir = os.path.join(working_dir, f"{project_name}.opr")
    sensitivity_dir = os.path.join(opd_dir, "Sensitivity")
    all_design_results: list[dict[str, Any]] = []

    result_dirs: list[tuple[str, str]] = []  # (label, dir containing job_*.json)
    for path in sorted(glob.glob(os.path.join(opr_dir, "*", "job_results.json"))):
        result_dirs.append((os.path.basename(os.path.dirname(path)), os.path.dirname(path)))
    for path in sorted(
        glob.glob(os.path.join(sensitivity_dir, "Design*", "conceptev", "job_results.json"))
    ):
        result_dirs.append((os.path.basename(os.path.dirname(os.path.dirname(path))), os.path.dirname(path)))

    print(f"[opd-check] found {len(result_dirs)} result location(s)")

    for design_name, result_dir in result_dirs:
        entry: dict[str, Any] = {"design": design_name}

        job_info_file = os.path.join(result_dir, "job_info.json")
        if os.path.exists(job_info_file):
            with open(job_info_file, encoding="utf-8") as fh:
                job_info = json.load(fh)
            entry["job_id"] = job_info.get("job_id")
            entry["job_name"] = job_info.get("job_name")
            print(
                f"[opd-check] {design_name}: job_id={job_info.get('job_id')}, "
                f"job_name={job_info.get('job_name')}"
            )

        job_results_file = os.path.join(result_dir, "job_results.json")
        if os.path.exists(job_results_file):
            with open(job_results_file, encoding="utf-8") as fh:
                results = json.load(fh)
            entry["results_count"] = len(results)
            entry["results"] = results
            feasible_count = sum(1 for r in results if r.get("feasible"))
            print(
                f"[opd-check] {design_name}: {len(results)} result(s), "
                f"{feasible_count} feasible"
            )
        else:
            print(f"[opd-check] {design_name}: job_results.json NOT found")

        all_design_results.append(entry)

    if not result_dirs:
        print(f"[opd-check] no result directories found under {opr_dir} or {sensitivity_dir}")

    if all_design_results:
        summary_path = write_json_debug(
            debug_dir, f"job_results_summary_{label}", all_design_results
        )
        artifacts["job_results_summary"] = summary_path
        total_results = sum(e.get("results_count", 0) for e in all_design_results)
        print(
            f"[opd-check] {len(all_design_results)} design(s), {total_results} total results "
            f"written to {summary_path}"
        )
    else:
        print("[opd-check] no design results collected")

    return artifacts


@pytest.mark.e2e
def test_optislang_connection(
    e2e_settings: Settings,
    e2e_concept: str,
    e2e_optislang,
    account_name: str,
    inject_integration,
) -> None:
    """Smoke test: optiSLang orchestrates the ConceptEV node end-to-end.

    Runs against an already-installed optiSLang with the ConceptEV integration
    plugin already registered. Builds the node, loads the reference concept,
    configures a small sensitivity, runs it, and saves the project.

    Pass ``--integration-dir PATH`` to replace the installed integration files
    with a custom source before OptiSLang starts (see ``inject_integration``
    fixture in conftest.py).
    """
    working_dir = get_working_dir()
    remove_non_empty_dir(working_dir)
    os.makedirs(working_dir)
    debug_dir = get_debug_dir(working_dir)

    osl_project_path = os.path.join(working_dir, "test_conceptev_ci.opf")
    design_instance_id = e2e_concept
    node_name = "conceptev"

    osl = None
    debug_artifacts: dict[str, str] = {}
    caught_error: Exception | None = None

    try:
        osl = e2e_optislang(osl_project_path)
        _log_osl_runtime_versions(osl, debug_dir, inject_integration=inject_integration)

        root_system = osl.application.project.root_system
        sensitivity = root_system.create_node(type_=node_types.Sensitivity)
        concept_ev_node_type = node_types.NodeType(
            id="conceptev",
            subtype=node_types.AddinType.PYTHON_BASED_INTEGRATION_PLUGIN,
            osl_class_type=node_types.NodeClassType.INTEGRATION_NODE,
        )
        cev_node = sensitivity.create_node(
            type_=concept_ev_node_type,
            name=node_name,
            design_flow=DesignFlow.RECEIVE_SEND,
        )

        non_modifying_settings = cev_node.get_property("NonModifyingSettings")
        non_modifying_settings["cev_account_name"] = account_name
        cev_node.set_property("NonModifyingSettings", non_modifying_settings)
        modifying_settings = cev_node.get_property("ModifyingSettings")
        modifying_settings["cev_concept_id"] = design_instance_id
        cev_node.set_property("ModifyingSettings", modifying_settings)

        print(
            f"[debug] loading conceptev node for concept_id={design_instance_id}, "
            f"account={non_modifying_settings['cev_account_name']}"
        )
        cev_node.load()
        # Snapshot after load: confirms the concept was found and input/output
        # locations are populated (86 inputs, 147+ outputs for the test concept).
        debug_artifacts["node_loaded"] = export_node_snapshot(
            osl, cev_node, debug_dir, "loaded", node_name
        )

        # Verify the injected integration is active by querying INTEGRATION_VERSION
        # from the installed .pye file via optiSLang's own Python subprocess.
        if inject_integration:
            integration_version = _query_integration_version(osl)
            print(
                f"[inject-integration] INTEGRATION_VERSION read via optiSLang: "
                f"{integration_version!r}"
            )
            assert integration_version and not integration_version.startswith("<"), (
                f"INTEGRATION_VERSION not found in the running conceptev_ci after node "
                f"load. Got: {integration_version!r}. "
                f"Check that conceptev_ci.py defines INTEGRATION_VERSION and that "
                f"inject_integration had write access to {_OSL_INTEGRATIONS_DIR}."
            )

        # Register one response to verify the node returns output data.
        # No parameters are registered so the Sensitivity runs only the
        # reference design — exactly one ConceptEV job call.
        register_response(cev_node, "_02__summary__cost")

        osl.application.save()
        print(f"[debug] project status before run: {osl.application.project.get_status()}")
        osl.application.project.start()
        print(f"[debug] project status after run: {osl.application.project.get_status()}")
        debug_artifacts["node_finished"] = export_node_snapshot(
            osl, cev_node, debug_dir, "finished", node_name
        )
        debug_artifacts.update(
            collect_opd_debug_artifacts(working_dir, debug_dir, "after_run")
        )

        assert_integration_results(working_dir, debug_dir)

        osl.application.save()
    except Exception as exc:
        caught_error = exc
        print(f"[debug] test failed with error: {exc!r}")
        try:
            debug_artifacts.update(
                collect_opd_debug_artifacts(working_dir, debug_dir, "on_failure")
            )
        except Exception as collect_exc:
            print(f"[debug] failed to collect opd artifacts on failure: {collect_exc!r}")
        raise
    finally:
        summary_label = "on_failure" if caught_error is not None else "completed"
        write_debug_summary(debug_dir, summary_label, debug_artifacts, caught_error)
        # optiSLang session lifecycle (incl. disposal of launched instances) is owned
        # by the e2e_optislang fixture.
