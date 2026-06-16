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
from pathlib import Path
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
import pytest

from ansys.conceptev.core.settings import Settings

E2E_CONFIG = Path(__file__).resolve().parent / "config.toml"


def stage_ci_environment(working_dir: str, e2e_settings: Settings) -> str:
    """Prepare the working directory and environment for the optiSLang plugin.

    The optiSLang conceptev plugin runs inside optiSLang's own Python process, which
    inherits the pytest process environment. We:
      1. Copy the test config.toml so the plugin finds it via "./config.toml".
      2. Set PYCONCEPTEV_SETTINGS so the plugin's settings.py loads the test config
         (needed in case optiSLang's CWD differs from the working_dir).
      3. Set CONCEPTEV_PASSWORD as an env var so the plugin's pydantic-settings picks
         it up regardless of where its CWD is (secrets file lookup is CWD-relative).
    """
    config_copy_path = os.path.join(working_dir, "config.toml")
    shutil.copy2(E2E_CONFIG, config_copy_path)

    os.environ["PYCONCEPTEV_SETTINGS"] = str(E2E_CONFIG)

    if e2e_settings.conceptev_password:
        os.environ["CONCEPTEV_PASSWORD"] = e2e_settings.conceptev_password

    print(
        "[e2e-env] staged settings for optiSLang plugin:\n"
        f"  config.toml={config_copy_path}\n"
        f"  PYCONCEPTEV_SETTINGS={os.environ.get('PYCONCEPTEV_SETTINGS')}\n"
        f"  CONCEPTEV_URL={e2e_settings.conceptev_url}\n"
        f"  AUTHORITY={e2e_settings.authority}\n"
        f"  CONCEPTEV_PASSWORD env var set: {bool(os.environ.get('CONCEPTEV_PASSWORD'))}"
    )
    return config_copy_path


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
        "osl_version": osl.get_osl_version_string(),
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
def test_optislang_connection(e2e_settings: Settings, e2e_concept: str) -> None:
    working_dir = get_working_dir()
    remove_non_empty_dir(working_dir)
    os.makedirs(working_dir)
    debug_dir = get_debug_dir(working_dir)
    stage_ci_environment(working_dir, e2e_settings)

    osl_project_path = os.path.join(working_dir, "test_conceptev_ci.opf")
    design_instance_id = e2e_concept
    node_name = "conceptev"

    osl = None
    std_handler = None
    err_handler = None
    debug_artifacts: dict[str, str] = {}
    caught_error: Exception | None = None

    try:
        osl = Optislang(project_path=osl_project_path)
        print(f"[debug] optiSLang session: {osl}")
        print(f"[debug] optiSLang version: {osl.get_osl_version_string()}")
        osl.osl_server.timeouts_register.default_value = 180
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
        non_modifying_settings["cev_account_name"] = e2e_settings.account_name
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
        if osl is not None:
            osl.dispose()
