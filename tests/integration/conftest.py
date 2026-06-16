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

"""Pytest configuration for integration tests.

Sets PYCONCEPTEV_SETTINGS before any ansys.conceptev.core import so the test
environment URL is used consistently. Also provides session-scoped fixtures for
two pre-built concepts:

- ``_creation_concept``: a minimal, empty concept used by component/config
  creation tests. Each creation test adds components into this shared concept,
  avoiding expensive project-per-test creation.

- ``populated_concept``: a session-scoped, fully-populated concept (with motor,
  battery, transmission, architecture, and a static-acceleration requirement)
  used by job-submission and concept-read tests.
"""

import os
from pathlib import Path

INTEGRATION_CONFIG = Path(__file__).resolve().parent / "config.toml"

# Must be set BEFORE any ansys.conceptev.core import — settings.py reads this
# at module-import time via os.environ.get("PYCONCEPTEV_SETTINGS").
os.environ.setdefault("PYCONCEPTEV_SETTINGS", str(INTEGRATION_CONFIG))

import pytest  # noqa: E402

from ansys.conceptev.core import app, auth  # noqa: E402

DATA_DIR = Path(__file__).parent


def pytest_configure(config) -> None:
    """Re-affirm the env var in case settings was imported before our module-level set."""
    os.environ.setdefault("PYCONCEPTEV_SETTINGS", str(INTEGRATION_CONFIG))


# ---------------------------------------------------------------------------
# Shared auth fixtures (session-scoped to avoid repeated MSAL round-trips)
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def session_token():
    """Acquire a long-lived AnsysID token once per test session."""
    msal = auth.create_msal_app()
    return auth.get_ansyId_token(msal)


@pytest.fixture(scope="session")
def session_account_id(session_token):
    """Look up the test account ID once per session."""
    accounts = app.get_account_ids(session_token)
    return accounts[auth.settings.account_name]


@pytest.fixture(scope="session")
def session_hpc_id(session_token, session_account_id):
    """Look up the default HPC ID once per session."""
    return app.get_default_hpc(session_token, session_account_id)


# ---------------------------------------------------------------------------
# Concept used by component/config creation tests
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def _creation_concept(session_token, session_account_id, session_hpc_id):
    """Create a minimal concept for component/config creation tests.

    Yields the concept dict and cleans up the whole project at the end of the
    session so no orphan projects accumulate on the test server.
    """
    with app.get_http_client(session_token) as client:
        project = app.create_new_project(
            client,
            session_account_id,
            session_hpc_id,
            "Integration Tests – creation",
        )
        concept = app.create_new_concept(
            client,
            project["projectId"],
            title="Component creation test concept",
        )
    yield concept
    app.delete_project(project["projectId"], session_token)


@pytest.fixture(scope="session")
def creation_design_instance_id(_creation_concept):
    """Design instance ID of the shared creation concept."""
    return _creation_concept["design_instance_id"]


# ---------------------------------------------------------------------------
# Fully-populated concept used by job-submission and concept-read tests
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def populated_concept(session_token, session_account_id, session_hpc_id):
    """Build a fully-populated concept for job submission and concept-read tests.

    Creates:
    - A new project + concept
    - MotorLabID component (from the bundled e9.lab file)
    - BatteryFixedVoltages component
    - TransmissionLossCoefficients component
    - Architecture linking all three
    - Aero / Mass / Wheel configurations
    - A static-acceleration requirement

    Yields ``(concept_data, design_instance_id, session_token)`` and tears down
    the project at the end of the session.
    """
    with app.get_http_client(session_token) as client:
        project = app.create_new_project(
            client,
            session_account_id,
            session_hpc_id,
            "Integration Tests – job",
        )
        concept = app.create_new_concept(
            client,
            project["projectId"],
            title="Job test concept",
        )

    design_instance_id = concept["design_instance_id"]

    with app.get_http_client(session_token, design_instance_id) as client:
        motor_file_result = app.post_component_file(client, DATA_DIR / "e9.lab", "motor_lab_file")
        motor = app.post(
            client,
            "/components",
            data={
                "component_type": "MotorLabID",
                "name": "Integration Test Motor",
                "data_id": motor_file_result[0],
                "max_speed": motor_file_result[1],
                "inverter_losses_included": False,
            },
        )
        battery = app.post(client, "/components", data={"component_type": "BatteryFixedVoltages"})
        transmission = app.post(
            client,
            "/components",
            data={"component_type": "TransmissionLossCoefficients"},
        )
        app.post(
            client,
            "/architectures",
            data={
                "number_of_front_motors": 1,
                "number_of_front_wheels": 2,
                "number_of_rear_motors": 0,
                "number_of_rear_wheels": 2,
                "front_transmission_id": transmission["id"],
                "front_motor_id": motor["id"],
                "battery_id": battery["id"],
            },
        )
        aero = app.post(client, "/configurations", data={"config_type": "aero"})
        mass = app.post(client, "/configurations", data={"config_type": "mass"})
        wheel = app.post(client, "/configurations", data={"config_type": "wheel"})
        app.post(
            client,
            "/requirements",
            data={
                "requirement_type": "static_acceleration",
                "speed": 10,
                "mass_id": mass["id"],
                "aero_id": aero["id"],
                "wheel_id": wheel["id"],
                "state_of_charge": 0.75,
                "acceleration": 0.5,
            },
        )
        concept_data = app.get_concept(client, design_instance_id)

    yield concept_data, design_instance_id, session_token

    app.delete_project(project["projectId"], session_token)


@pytest.fixture(scope="session")
def populated_design_instance_id(populated_concept):
    """Design instance ID of the fully-populated job-test concept."""
    _, design_instance_id, _ = populated_concept
    return design_instance_id


@pytest.fixture(scope="session")
def job_client(session_token, populated_design_instance_id):
    """Persistent httpx client for job-submission tests, bound to the populated concept."""
    with app.get_http_client(session_token, populated_design_instance_id) as client:
        yield client
