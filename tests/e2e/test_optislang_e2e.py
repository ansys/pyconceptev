# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
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

import logging
import os
import shutil

from ansys.optislang.core import Optislang
import ansys.optislang.core.node_types as node_types
from ansys.optislang.core.nodes import DesignFlow
from ansys.optislang.core.project_parametric import (
    ComparisonType,
    ConstraintCriterion,
    ObjectiveCriterion,
)
import pytest


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


@pytest.mark.e2e
def test_optislang_connection() -> None:
    # create fresh working directory
    # this is logging in interactively and connecting to prod server at the moment
    working_dir = get_working_dir()
    opf_filepath = os.path.join(working_dir, "test_conceptev_ci.opf")
    opd_dir = os.path.join(working_dir, "test_conceptev_ci.opd")
    remove_non_empty_dir(working_dir)
    os.makedirs(working_dir)

    osl_project_path = os.path.join(working_dir, "test_conceptev_ci.opf")

    # created concept
    # configure environment
    design_instance_id = "121222c8-f2e8-4fa2-84fb-69336bbdc548"
    osl = Optislang(project_path=osl_project_path)
    print(osl)
    osl.osl_server.timeouts_register.default_value = 180
    std_handler, err_handler = prepare_logging_facilities(osl, working_dir)

    root_system = osl.application.project.root_system
    sensitivity = root_system.create_node(type_=node_types.Sensitivity)
    concept_ev_node_type = node_types.NodeType(
        id="conceptev",
        subtype=node_types.AddinType.PYTHON_BASED_INTEGRATION_PLUGIN,
        osl_class_type=node_types.NodeClassType.INTEGRATION_NODE,
    )
    node_name = "conceptev"
    cev_node = sensitivity.create_node(
        type_=concept_ev_node_type,
        name=node_name,
        design_flow=DesignFlow.RECEIVE_SEND,
    )
    non_modifying_settings = cev_node.get_property("NonModifyingSettings")
    non_modifying_settings["cev_account_name"] = "ConceptEv Test Account"
    cev_node.set_property("NonModifyingSettings", non_modifying_settings)
    modifying_settings = cev_node.get_property("ModifyingSettings")
    modifying_settings["cev_concept_id"] = design_instance_id
    cev_node.set_property("ModifyingSettings", modifying_settings)
    cev_node.load()

    input_locations = cev_node.get_available_input_locations()
    output_locations = cev_node.get_available_output_locations()
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

    # limit the number of designs to compute
    algo_settings = sensitivity.get_property("AlgorithmSettings")
    algo_settings["num_discretization"] = 10
    sensitivity.set_property("AlgorithmSettings", algo_settings)

    # define parallelism
    cev_node.set_property("MaxParallel", 10)

    # define max runtime
    cev_node.set_property("MaxRuntime", 180000)  # milliseconds

    # save
    osl.application.save()

    # run
    osl.application.project.start()

    # save and close
    osl.application.save()
    osl.dispose()

    stderr = "".join(err_handler.get_messages())
    stdout = "".join(std_handler.get_messages())
