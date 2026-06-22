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

import json
import logging
import os
import re
import shutil
import traceback
from typing import Any

from ansys.optislang.core import Optislang
import ansys.optislang.core.node_types as node_types
from ansys.optislang.core.nodes import DesignFlow
from ansys.optislang.core.project_parametric import (
    ComparisonType,
    ConstraintCriterion,
    ObjectiveCriterion,
)
from conftest import _OSL_INTEGRATIONS_DIR
import pytest

from ansys.conceptev.core.settings import Settings


class QueryHandler(logging.Handler):
    def __init__(self, log_filepath=None):
        super().__init__()
        self._collected_messages = []
        self.log_filepath = log_filepath

    def emit(self, record):
        self._collected_messages.append(record.getMessage())
        if self.log_filepath is not None:
            with open(str(self.log_filepath), "a") as f:
                f.write(record.getMessage() + "\n")

    def get_messages(self):
        collected_messages = [msg for msg in self._collected_messages]
        self._collected_messages = []
        return collected_messages


class LogFilter(logging.Filter):
    def __init__(self, level):
        super().__init__()
        self._level = level

    def filter(self, record):
        return record.levelno <= self._level


def prepare_logging_facilities(osl_object, working_dir):
    osl_object.log.setLevel(logging.DEBUG)
    error_handler = QueryHandler(os.path.join(working_dir, "stderr.txt"))
    error_handler.setLevel(logging.WARNING)
    std_handler = QueryHandler(os.path.join(working_dir, "stdout.txt"))
    std_handler.setLevel(logging.DEBUG)
    std_handler.addFilter(LogFilter(logging.INFO))

    osl_object.log.addHandler(std_handler)
    osl_object.log.addHandler(error_handler)

    return std_handler, error_handler


def register_parameter(node, name):
    location = get_input_location_by_name(node, name)
    node.register_location_as_parameter(
        location=location,
        name=name,
    )


def get_input_location_by_name(node, name):
    input_locations = node.get_available_input_locations()
    for loc in input_locations:
        if loc["location"]["name"] == name:
            return loc["location"]
    raise KeyError(f"Input location '{name}' not found.")


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


# Markers emitted by pyconceptev's websocket progress monitoring
# (see ansys.conceptev.core.progress). These surface in the optiSLang node log
# when the ConceptEV integration actually submits a job and monitors it.
OCM_WEBSOCKET_MARKER = "connected to ocm websockets."
STATUS_RUNNING_MARKER = "status:running"
# pyconceptev treats both COMPLETED and FINISHED as terminal-success states, so
# accept either as the "finished" marker.
STATUS_FINISHED_MARKERS = ("status:finished", "status:completed")
PROGRESS_PATTERN = re.compile(r"progress:\s*([0-9]+(?:\.[0-9]+)?)", re.IGNORECASE)


def collect_run_log_text(osl: Optislang, node: Any, working_dir: str) -> str:
    """Aggregate optiSLang log text so progress/websocket markers can be searched.

    Pulls from the handler-written log files (stdout.txt / stderr.txt) and the
    node's actor log messages, since the ConceptEV plugin's stdout (and the
    pyconceptev progress prints) are captured by optiSLang on the node actor.
    """
    chunks: list[str] = []
    for name in ("stdout.txt", "stderr.txt"):
        path = os.path.join(working_dir, name)
        if os.path.exists(path):
            with open(path, encoding="utf-8", errors="replace") as fh:
                chunks.append(fh.read())
    try:
        actor_info = osl.osl_server.get_actor_info(uid=node.uid, include_log_messages=True)
        for entry in actor_info.get("log_messages", []) or []:
            if isinstance(entry, dict):
                chunks.append(str(entry.get("message", entry)))
            else:
                chunks.append(str(entry))
    except Exception as exc:
        chunks.append(f"<failed to read actor log messages: {exc!r}>")
    return "\n".join(chunks)


def check_progress_log_markers(log_text: str) -> dict[str, Any]:
    """Inspect aggregated log text for the websocket/status/progress markers."""
    lowered = log_text.lower()
    progress_values = PROGRESS_PATTERN.findall(log_text)
    return {
        "ocm_websocket_connected": OCM_WEBSOCKET_MARKER in lowered,
        "status_running": STATUS_RUNNING_MARKER in lowered,
        "status_finished": any(marker in lowered for marker in STATUS_FINISHED_MARKERS),
        "progress_values": progress_values,
        "progress_seen": bool(progress_values),
    }


def assert_progress_log_markers(
    osl: Optislang, node: Any, working_dir: str, debug_dir: str
) -> None:
    """Fail the test if the optiSLang run log is missing expected run markers."""
    log_text = collect_run_log_text(osl, node, working_dir)
    log_path = os.path.join(debug_dir, "progress_log.txt")
    with open(log_path, "w", encoding="utf-8") as fh:
        fh.write(log_text)
    print(f"[progress-check] aggregated run log written to {log_path}")

    markers = check_progress_log_markers(log_text)
    print(f"[progress-check] markers: {markers}")

    missing: list[str] = []
    if not markers["ocm_websocket_connected"]:
        missing.append("Connected to OCM Websockets.")
    if not markers["status_running"]:
        missing.append("Status:RUNNING")
    if not markers["status_finished"]:
        missing.append("Status:FINISHED (or COMPLETED)")
    if not markers["progress_seen"]:
        missing.append("Progress:<float>")

    assert not missing, (
        f"optiSLang run log missing expected markers: {missing}. "
        f"See {log_path} for the captured log."
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


def export_project_snapshot(osl: Optislang, debug_dir: str, label: str) -> dict[str, str]:
    project = osl.application.project
    snapshot = {
        "label": label,
        "osl_version": osl.osl_version_string,
        "project_status": project.get_status(),
        "project_working_dir": str(project.get_working_dir()),
        "basic_project_info": osl.osl_server.get_basic_project_info(),
        "project_tree": osl.osl_server.get_full_project_tree_with_properties(),
    }
    artifacts = {
        "snapshot": write_json_debug(debug_dir, f"project_snapshot_{label}", snapshot),
        "project_tree": write_json_debug(
            debug_dir, f"project_tree_{label}", snapshot["project_tree"]
        ),
        "project_file": export_optislang_project_file(osl, debug_dir, label),
    }
    print(
        f"[debug] project snapshot '{label}': "
        f"status={snapshot['project_status']}, "
        f"working_dir={snapshot['project_working_dir']}"
    )
    return artifacts


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
    stdout: str,
    stderr: str,
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
        summary_file.write("\noptislang stdout:\n")
        summary_file.write(stdout or "<empty>\n")
        summary_file.write("\noptislang stderr:\n")
        summary_file.write(stderr or "<empty>\n")
    print(f"[debug] wrote {summary_path}")
    return summary_path


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
    std_handler = None
    err_handler = None
    debug_artifacts: dict[str, str] = {}
    caught_error: Exception | None = None

    try:
        osl = e2e_optislang(osl_project_path)
        _log_osl_runtime_versions(osl, debug_dir, inject_integration=inject_integration)
        std_handler, err_handler = prepare_logging_facilities(osl, working_dir)

        debug_artifacts.update(export_project_snapshot(osl, debug_dir, "initialized"))

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
        debug_artifacts["node_created"] = export_node_snapshot(
            osl, cev_node, debug_dir, "created", node_name
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
        debug_artifacts["node_loaded"] = export_node_snapshot(
            osl, cev_node, debug_dir, "loaded", node_name
        )
        debug_artifacts.update(export_project_snapshot(osl, debug_dir, "after_load"))

        # Verify the injected integration is active by querying INTEGRATION_VERSION
        # from the installed .pye file via optiSLang's own Python subprocess.
        # Performed here — after the node exists — so the integration has been
        # picked up by optiSLang before we assert.
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

        register_parameter(cev_node, "rear_motor")
        register_response(cev_node, "_00__capability_curve__torque_vs_speed")
        register_response(cev_node, "_02__summary__cost")
        register_response(cev_node, "_02__summary__mass")
        register_response(cev_node, "_02__summary__constraints_fulfilled")
        register_response(cev_node, "_02__summary__n_constraints_fulfilled")

        sensitivity.criteria_manager.add_criterion(
            ObjectiveCriterion(
                name="obj_cost", expression="_02__summary__cost", criterion=ComparisonType.MIN
            )
        )
        sensitivity.criteria_manager.add_criterion(
            ConstraintCriterion(
                name="constraints_fulfilled",
                expression="_02__summary__n_constraints_fulfilled",
                criterion=ComparisonType.GREATEREQUAL,
                limit_expression="1",
            )
        )

        algo_settings = sensitivity.get_property("AlgorithmSettings")
        algo_settings["num_discretization"] = 10
        sensitivity.set_property("AlgorithmSettings", algo_settings)
        cev_node.set_property("MaxParallel", 10)
        cev_node.set_property("MaxRuntime", 180000)

        debug_artifacts["node_configured"] = export_node_snapshot(
            osl, cev_node, debug_dir, "configured", node_name
        )
        debug_artifacts.update(export_project_snapshot(osl, debug_dir, "configured"))

        osl.application.save()
        print(f"[debug] project status before run: {osl.application.project.get_status()}")
        osl.application.project.start()
        print(f"[debug] project status after run: {osl.application.project.get_status()}")
        debug_artifacts.update(export_project_snapshot(osl, debug_dir, "after_run"))
        debug_artifacts["node_finished"] = export_node_snapshot(
            osl, cev_node, debug_dir, "finished", node_name
        )

        assert_progress_log_markers(osl, cev_node, working_dir, debug_dir)

        osl.application.save()
    except Exception as exc:
        caught_error = exc
        print(f"[debug] test failed at stage with error: {exc!r}")
        if osl is not None:
            try:
                debug_artifacts.update(export_project_snapshot(osl, debug_dir, "on_failure"))
            except Exception as export_exc:
                print(f"[debug] failed to export project snapshot on failure: {export_exc!r}")
        raise
    finally:
        stdout = "".join(std_handler.get_messages()) if std_handler is not None else ""
        stderr = "".join(err_handler.get_messages()) if err_handler is not None else ""
        summary_label = "on_failure" if caught_error is not None else "completed"
        write_debug_summary(debug_dir, summary_label, stdout, stderr, debug_artifacts, caught_error)
        # optiSLang session lifecycle (incl. disposal of launched instances) is owned
        # by the e2e_optislang fixture.
