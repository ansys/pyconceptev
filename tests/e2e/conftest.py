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

"""Pytest configuration for e2e tests.

Forces the same ConceptEV / Ansys ID test environment used in CI so local runs
match the GitHub Actions e2e job.

IMPORTANT: PYCONCEPTEV_SETTINGS must be set before ansys.conceptev.core is first
imported, because settings.py evaluates os.environ.get("PYCONCEPTEV_SETTINGS") at
class-definition time (module import). We do this at the top of this file before
any ansys imports, and also in pytest_configure for any late-importing test modules.

Uses the same config.toml as the integration tests to ensure a single source of
truth for test-environment settings.
"""

import os
from pathlib import Path

# Shared config with integration tests — single source of truth.
E2E_CONFIG = Path(__file__).resolve().parent.parent / "integration" / "config.toml"
PROD_CONCEPTEV_URL = "https://conceptev.ansys.com/api"
TEST_AUTHORITY_MARKER = "signup_signin_test"

# Set env var NOW — before any ansys.conceptev.core import triggers settings.py load.
os.environ["PYCONCEPTEV_SETTINGS"] = str(E2E_CONFIG)
os.environ.setdefault("PYOPTISLANG_DISABLE_OPTISLANG_OUTPUT", "true")

import pytest  # noqa: E402

from ansys.conceptev.core import app, auth  # noqa: E402
from ansys.conceptev.core.settings import load_settings  # noqa: E402

# e9.lab lives next to the integration tests (single copy, shared by both suites).
DATA_DIR = Path(__file__).resolve().parent.parent / "integration"


def pytest_configure(config) -> None:
    """Re-affirm env vars in case a plugin imported settings before our module-level set."""
    os.environ["PYCONCEPTEV_SETTINGS"] = str(E2E_CONFIG)
    os.environ.setdefault("PYOPTISLANG_DISABLE_OPTISLANG_OUTPUT", "true")


@pytest.fixture(scope="session")
def e2e_settings():
    """Load and validate the CI-equivalent e2e settings."""
    settings = load_settings(E2E_CONFIG)

    assert settings.conceptev_url == "https://test-conceptev.awsansys3np.onscale.com/api", (
        "e2e tests must target the ConceptEV test API, not production. "
        f"Got conceptev_url={settings.conceptev_url!r}"
    )
    assert settings.ocm_url == "https://dev.portal.onscale.com/api", (
        f"e2e tests must target the OCM dev API. Got ocm_url={settings.ocm_url!r}"
    )
    assert TEST_AUTHORITY_MARKER in settings.authority, (
        "e2e tests must use the Ansys ID test authority "
        f"({TEST_AUTHORITY_MARKER}). Got authority={settings.authority!r}"
    )
    assert settings.conceptev_url != PROD_CONCEPTEV_URL
    assert settings.account_name == "ConceptEv Test Account"

    if settings.conceptev_username and not os.environ.get("CONCEPTEV_PASSWORD"):
        # CI provides CONCEPTEV_PASSWORD via secrets; locally it can come from a
        # pydantic-settings secret file named "conceptev_password" in the project root.
        from ansys.conceptev.core.settings import settings as loaded_settings

        if not loaded_settings.conceptev_password:
            print(
                "[e2e-env] WARNING: CONCEPTEV_PASSWORD not set and no secret file found. "
                "MSAL will attempt an interactive login or use a cached token."
            )

    print(
        "[e2e-env] Using CI-equivalent settings:\n"
        f"  PYCONCEPTEV_SETTINGS={os.environ['PYCONCEPTEV_SETTINGS']}\n"
        f"  CONCEPTEV_URL={settings.conceptev_url}\n"
        f"  OCM_URL={settings.ocm_url}\n"
        f"  OCM_SOCKET_URL={settings.ocm_socket_url}\n"
        f"  AUTHORITY={settings.authority}\n"
        f"  ACCOUNT_NAME={settings.account_name}\n"
        f"  CONCEPTEV_USERNAME={settings.conceptev_username}\n"
        f"  CONCEPTEV_PASSWORD set: {bool(settings.conceptev_password)}"
    )
    return settings


@pytest.fixture(scope="session", autouse=True)
def _enforce_e2e_test_environment(e2e_settings):
    """Ensure every e2e test session uses the validated test environment."""
    return e2e_settings


# ---------------------------------------------------------------------------
# Auth fixtures (session-scoped to avoid repeated MSAL round-trips)
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
# Fresh e2e concept — avoids stale server data entirely
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def e2e_concept(session_token, session_account_id, session_hpc_id):
    """Create a fresh, fully-populated e2e concept for the optiSLang integration test.

    The optiSLang ConceptEV plugin's ``sanitize_result_data`` requires
    ``data['requirements']`` and a valid architecture.  Stale concepts that
    contain deprecated component types (e.g. MotorCTCP) or no requirements
    cause the plugin to fail during ``cev_node.load()``.

    This fixture creates a known-good concept with:

    - MotorLabID rear motor (from the bundled ``e9.lab`` file)
    - BatteryFixedVoltages
    - TransmissionLossCoefficients
    - Rear-motor architecture (``number_of_rear_motors=1``)
    - Aero / mass / wheel configurations
    - Static-acceleration requirement

    Yields ``design_instance_id`` and tears down the whole project on
    session teardown so no orphan projects accumulate.
    """
    with app.get_http_client(session_token) as client:
        project = app.create_new_project(
            client,
            session_account_id,
            session_hpc_id,
            "E2E Tests – optiSLang connection",
        )
        concept = app.create_new_concept(
            client,
            project["projectId"],
            title="E2E optiSLang test concept",
        )

    design_instance_id = concept["design_instance_id"]

    with app.get_http_client(session_token, design_instance_id) as client:
        motor_file_result = app.post_component_file(
            client, DATA_DIR / "e9.lab", "motor_lab_file"
        )
        motor = app.post(
            client,
            "/components",
            data={
                "component_type": "MotorLabID",
                "name": "E2E Test Rear Motor",
                "data_id": motor_file_result[0],
                "max_speed": motor_file_result[1],
                "inverter_losses_included": False,
            },
        )
        battery = app.post(
            client,
            "/components",
            data={"component_type": "BatteryFixedVoltages"},
        )
        transmission = app.post(
            client,
            "/components",
            data={"component_type": "TransmissionLossCoefficients"},
        )
        app.post(
            client,
            "/architectures",
            data={
                "number_of_front_motors": 0,
                "number_of_front_wheels": 2,
                "number_of_rear_motors": 1,
                "number_of_rear_wheels": 2,
                "rear_transmission_id": transmission["id"],
                "rear_motor_id": motor["id"],
                "battery_id": battery["id"],
            },
        )
        aero = app.post(client, "/configurations", data={"config_type": "aero"})
        mass = app.post(client, "/configurations", data={"config_type": "mass"})
        wheel = app.post(client, "/configurations", data={"config_type": "wheel"})
        # Two requirements so that the optiSLang plugin's summary outputs land at
        # the _02__summary__ prefix (requirement 0 → _00__, requirement 1 → _01__,
        # summary group → _02__), matching the registered response names in the test.
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
        app.post(
            client,
            "/requirements",
            data={
                "requirement_type": "static_acceleration",
                "speed": 20,
                "mass_id": mass["id"],
                "aero_id": aero["id"],
                "wheel_id": wheel["id"],
                "state_of_charge": 0.75,
                "acceleration": 0.3,
            },
        )

    print(f"[e2e-setup] Created e2e concept: design_instance_id={design_instance_id}")

    yield design_instance_id

    app.delete_project(project["projectId"], session_token)
    print(f"[e2e-setup] Deleted e2e project {project['projectId']}")
