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

import asyncio
from pathlib import Path
import pprint
import re

import httpx
import jwt

# Optislang Integration Test
# A poor attempt at integration test for the optislang integration.
# Looks at conceptev/utils/api_helper.py to see pyconceptev usage within ConceptEV integration.
import pytest

from ansys.conceptev.core import app, auth, exceptions

DATA_DIR = Path(__file__).parent


@pytest.fixture
def msal_app():
    """Fixture to create a MSAL PublicClientApplication instance."""
    return auth.create_msal_app()


@pytest.fixture
def token(msal_app):
    """Fixture to get a valid AnsysID token."""
    token = auth.get_ansyId_token(msal_app)
    return token


@pytest.fixture
def client(token):
    """Fixture to provide a client for testing."""
    with app.get_http_client(token) as client:
        yield client


@pytest.fixture
def design_instance_id(creation_design_instance_id):
    """Fixture to provide a design instance ID for testing.

    Uses the session-scoped creation concept so component/config creation tests
    share one concept rather than hitting a stale hardcoded server-side concept.
    """
    return creation_design_instance_id


@pytest.fixture
def client_with_design_instance(design_instance_id, token):
    """Fixture to provide a client with a design instance ID for testing."""
    with app.get_http_client(token, design_instance_id) as client:
        yield client


@pytest.fixture
def accounts(token):
    """Fixture to get accounts."""
    accounts = app.get_account_ids(token)
    return accounts


@pytest.fixture
def concept_data(populated_concept):
    """Fixture to get concept data from the session-scoped fully-populated concept."""
    concept_data, _, _ = populated_concept
    return concept_data


@pytest.fixture
def account_id(accounts):
    """Fixture to provide an account ID for testing."""
    return accounts[auth.settings.account_name]


@pytest.fixture
def hpc_id(token, account_id):
    """Fixture to get the HPC ID."""
    hpc_id = app.get_default_hpc(token, account_id)
    return hpc_id


@pytest.fixture
def job_info(job_client, concept_data, session_account_id, session_hpc_id):
    """Submit a job to the HPC using the fully-populated session concept."""
    job_info = app.create_submit_job(
        job_client,
        concept_data,
        session_account_id,
        session_hpc_id,
    )
    return job_info


@pytest.fixture
def read_results(job_client, job_info):
    """Read results from the job."""
    read_results = app.read_results(
        job_client,
        job_info,
        calculate_units=False,
        filtered=True,
    )
    return read_results


@pytest.fixture
def console_log(job_info, job_client):
    console_log = app.post(job_client, "/jobs:error_file", data=job_info)
    return console_log


@pytest.fixture
def project_name():
    """Project name fixture."""
    return "Integration Test from pyconceptev"


@pytest.fixture
def created_project(client, account_id, hpc_id, token, project_name):
    created_project = app.create_new_project(client, account_id, hpc_id, f"{project_name}")
    yield created_project
    app.delete_project(created_project["projectId"], token)


@pytest.fixture
def project_id(created_project):
    """Fixture to provide a project ID for testing."""
    return created_project["projectId"]


@pytest.fixture
def created_concept(client, project_id):
    concept_data = app.create_new_concept(
        client,
        project_id,
        title="ConceptEV Integration Test",
    )
    return concept_data


@pytest.fixture
def account_ids(token):
    """Fixture to get accounts."""
    account_ids = app.get_account_ids(token)
    return account_ids


@pytest.fixture
def project_ids(project_name, created_project, account_id, token):
    """Fixture to get project IDs."""
    project_ids = app.get_project_ids(re.escape(project_name), account_id, token)
    return project_ids


def test_exceptions():
    """Example Exception Usage in api_helper"""
    try:
        raise exceptions.ResponseError("This is a test error")
    except exceptions.ResponseError as e:
        assert e.args[0].lower()


def test_msal_app(msal_app):
    """Test that the MSAL PublicClientApplication is created."""
    assert isinstance(msal_app, auth.PublicClientApplication)
    assert msal_app.client_id == auth.client_id
    assert msal_app.authority.authorization_endpoint == auth.authority + "/oauth2/v2.0/authorize"


def test_auth_app(token):
    """Test that the optislang integration works."""
    assert isinstance(token, str)
    claims = jwt.decode(token, options={"verify_signature": False})
    # Step 1: Fetch JWKS
    jwks = httpx.get(auth.settings.authority + "/discovery/v2.0/keys").json()

    # Step 2: Get headers from token to find correct kid
    unverified_header = jwt.get_unverified_header(token)
    kid = unverified_header["kid"]
    key = next(k for k in jwks["keys"] if k["kid"] == kid)
    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
    algorithm = unverified_header["alg"]
    jwt.decode(token, public_key, verify=True, algorithms=algorithm, options={"verify_aud": False})


def test_client(client, token):
    """Test that the client can make a request."""
    assert str(client.base_url).strip("/") == auth.settings.conceptev_url
    assert client.headers["Authorization"] == f"{token}"


def test_client_design_instance(client_with_design_instance, token, design_instance_id):
    """Test that the client can make a request with a design instance."""
    assert str(client_with_design_instance.base_url).strip("/") == auth.settings.conceptev_url
    assert client_with_design_instance.headers["Authorization"] == f"{token}"
    assert client_with_design_instance.params["design_instance_id"] == design_instance_id
    # Additional checks can be added here for specific endpoints or data


def test_health(client):
    """Test the health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["name"] == "ConceptEV"


def test_authorised(client):
    """Test the health endpoint."""
    response = client.get("/authenticated_user")
    assert response.status_code == 200


def test_get_concept(client, job_client, populated_design_instance_id, concept_data):
    """Test getting a concept and getting ids."""
    concept = app.get(
        client, "/concepts", id=populated_design_instance_id, params={"populated": False}
    )
    concept["configurations"] = app.get(
        job_client, f"/concepts/{populated_design_instance_id}/configurations"
    )
    concept["components"] = app.get(
        job_client, f"/concepts/{populated_design_instance_id}/components"
    )
    concept["requirements"] = app.get(
        job_client, f"/concepts/{populated_design_instance_id}/requirements"
    )
    concept["architecture"] = app.get(
        job_client, f"/concepts/{populated_design_instance_id}/architecture"
    )
    assert concept == concept_data


def test_accounts(accounts, token):
    """Test accounts endpoint."""
    assert isinstance(accounts, dict)
    assert auth.settings.account_name in accounts


def test_hpc_endpoint(hpc_id):
    assert isinstance(hpc_id, str)
    assert len(hpc_id) > 0, "HPC ID should not be empty"


def test_submit_job(job_info):
    assert isinstance(job_info, dict)
    assert "job_id" in job_info


def test_get_status(job_info, token):
    """Smoke-test that ocm.get_status returns a non-empty uppercase string for a submitted job."""
    from ansys.conceptev.core import ocm

    status = ocm.get_status(job_info, token)
    assert isinstance(status, str)
    assert status  # non-empty
    assert status == status.upper()


def test_diagnose_status_transport(job_info, token):
    """Diagnostic: print the raw OCM REST status fields and a sample of WebSocket messages.

    Run with ``pytest -s`` to see printed output.  This test always passes — its
    purpose is to expose the exact field names / message shapes returned by OCM
    so any contract change (e.g. renamed status fields) is immediately visible.
    """
    from ansys.conceptev.core import ocm, progress

    job_id = job_info["job_id"]

    # ------------------------------------------------------------------ REST --
    client = ocm.create_ocm_client(token)
    raw = client.post(url="/job/load", json={"jobId": job_id})
    print(f"\n=== REST /job/load  (HTTP {raw.status_code}) ===")
    payload = raw.json()
    # Print only the status-related keys to keep output concise
    status_keys = {k: v for k, v in payload.items() if "status" in k.lower() or "Status" in k}
    print("Status-related keys:")
    pprint.pprint(status_keys)
    print("All top-level keys:", sorted(payload.keys()))

    # ------------------------------------------------------- WebSocket sample --
    user_id = ocm.get_user_id(token)

    async def _collect(n=10, timeout=60):
        """Connect once and collect up to *n* messages within *timeout* seconds."""
        collected = []
        try:
            async with asyncio.timeout(timeout):
                async with progress.connect_to_ocm(user_id, token) as ws:
                    print("\n=== WebSocket connected ===")
                    async for raw_msg in ws:
                        collected.append(raw_msg)
                        if len(collected) >= n:
                            break
        except TimeoutError:
            print(f"WebSocket: timed out after {timeout}s (collected {len(collected)} messages)")
        except Exception as exc:
            print(f"WebSocket: connection ended — {type(exc).__name__}: {exc}")
        return collected

    messages = asyncio.run(_collect())

    # ----------------------------------------- compare messages to code expectations --
    import json

    # What progress.get_status / get_values reads from each WebSocket message:
    #   jobId        — must equal job_id to be processed at all
    #   messagetype  — "status" | "progress" | "error"
    #   status       — present on messagetype=="status", called with .upper()
    #   progress     — present on messagetype=="progress"
    #   message      — present on messagetype=="error"
    #   calculated_values — present on messagetype=="progress" when progress==1

    EXPECTED_FIELDS_BY_TYPE = {
        "status": ["jobId", "messagetype", "status"],
        "progress": ["jobId", "messagetype", "progress"],
        "error": ["jobId", "messagetype", "message"],
    }

    print(f"\n=== WebSocket messages received: {len(messages)} ===")
    issues_found = []

    for i, msg in enumerate(messages, start=1):
        try:
            parsed = json.loads(msg)
        except Exception as exc:
            print(f"--- message {i}: could not parse JSON — {exc} ---")
            print(repr(msg))
            issues_found.append(f"message {i}: unparsable")
            continue

        print(f"\n--- message {i} (raw) ---")
        pprint.pprint(parsed)

        msg_job_id = parsed.get("jobId")
        msg_type = parsed.get("messagetype")

        # Check 1: does this message carry a jobId at all?
        if "jobId" not in parsed:
            issues_found.append(
                f"message {i}: missing 'jobId' — "
                f"code checks `message_data.get('jobId', 'Unknown') == job_id`"
            )

        # Check 2: is messagetype present?
        if "messagetype" not in parsed:
            issues_found.append(f"message {i}: missing 'messagetype' — code routes on this field")

        # Check 3: per-type field validation (only for messages belonging to our job)
        if msg_job_id == job_id:
            print(f"    -> belongs to our job ({job_id})")
            expected = EXPECTED_FIELDS_BY_TYPE.get(msg_type)
            if expected is None:
                issues_found.append(
                    f"message {i}: unrecognised messagetype={msg_type!r} "
                    f"(code handles 'status', 'progress', 'error')"
                )
            else:
                for field in expected:
                    if field not in parsed:
                        issues_found.append(
                            f"message {i} (type={msg_type!r}): missing expected field {field!r}"
                        )
                # Extra check: status messages must have a non-None status so .upper() won't crash
                if msg_type == "status" and parsed.get("status") is None:
                    issues_found.append(
                        f"message {i}: 'status' is None — "
                        "code calls .upper() on it without a None guard"
                    )
        else:
            print(f"    -> belongs to a different job ({msg_job_id}), skipping field check")

    print("\n=== Comparison summary ===")
    if issues_found:
        print("MISMATCHES vs current code expectations:")
        for issue in issues_found:
            print(f"  !! {issue}")
    else:
        print("All received messages are compatible with current code expectations.")

    # Always pass — this is a diagnostic/introspection test only
    assert True


def test_read_results(read_results):
    """Test reading results from the job."""
    assert isinstance(read_results, list)
    assert len(read_results) > 0, "Results should not be empty"
    assert isinstance(read_results[0]["feasible"], bool)
    assert "requirements" in read_results[0], "Each result item must contain 'requirements' key"


def test_console_log(read_results, console_log):
    """Test reading the console log."""
    assert isinstance(console_log, str)
    assert len(console_log) > 0, "Console log should not be empty"


def test_create_project(created_project):
    """Test creating a project."""
    assert isinstance(created_project, dict)
    assert "projectId" in created_project
    assert created_project["projectTitle"] == "Integration Test from pyconceptev"


def test_created_concept(created_concept, project_id):
    """Test creating a concept."""
    assert isinstance(created_concept, dict)
    assert created_concept["project_id"] == project_id
    assert "design_instance_id" in created_concept


def test_get_accounts(account_ids, account_id):
    """Test getting accounts."""
    assert isinstance(account_ids, dict)
    assert auth.settings.account_name in account_ids
    assert account_id in account_ids.values()


def test_project_ids(project_ids, project_id, project_name):
    """Test project ids"""
    assert isinstance(project_ids, dict)
    assert project_name in project_ids
    assert isinstance(project_ids[project_name], list)
    assert project_id in project_ids[project_name]


@pytest.fixture
def transmission_loss_coefficients(client_with_design_instance):
    """Fixture to provide transmission loss coefficients."""
    transmission = {
        "component_type": "TransmissionLossCoefficients",
    }
    return app.post(client_with_design_instance, "/components", data=transmission)


@pytest.fixture
def aero(client_with_design_instance):
    """Fixture to provide aero configuration."""
    aero = {
        "config_type": "aero",
    }
    return app.post(client_with_design_instance, "/configurations", data=aero)


@pytest.fixture
def mass(client_with_design_instance):
    """Fixture to provide mass configuration."""
    mass = {
        "config_type": "mass",
    }
    return app.post(client_with_design_instance, "/configurations", data=mass)


@pytest.fixture
def wheel(client_with_design_instance):
    """Fixture to provide wheel configuration."""
    wheel = {
        "config_type": "wheel",
    }
    return app.post(client_with_design_instance, "/configurations", data=wheel)


@pytest.fixture
def requirement(client_with_design_instance, aero, mass, wheel):
    requirement = {
        "requirement_type": "static_acceleration",
        "speed": 10,
        "mass_id": mass["id"],
        "aero_id": aero["id"],
        "wheel_id": wheel["id"],
        "state_of_charge": 0.75,
        "acceleration": 0.5,
    }
    requirement = app.post(client_with_design_instance, "/requirements", data=requirement)
    return requirement


@pytest.fixture
def motor_file(client_with_design_instance):
    """Fixture to provide a motor configuration."""
    motor_filename = DATA_DIR / "e9.lab"
    return app.post_component_file(
        client_with_design_instance, motor_filename, component_file_type="motor_lab_file"
    )


@pytest.fixture
def motor(client_with_design_instance, motor_file):
    """Fixture to provide a motor component using a motor lab file upload."""
    motor = {
        "component_type": "MotorLabID",
        "name": "Test Motor",
        "data_id": motor_file[0],
        "max_speed": motor_file[1],
        "inverter_losses_included": False,
    }
    return app.post(client_with_design_instance, "/components", data=motor)


@pytest.fixture
def battery(client_with_design_instance):
    """Fixture to provide a battery configuration."""
    battery = {"component_type": "BatteryFixedVoltages"}
    return app.post(client_with_design_instance, "/components", data=battery)


@pytest.fixture
def architecture(client_with_design_instance, transmission_loss_coefficients, motor, battery):
    architecture = {
        "number_of_front_motors": 1,
        "number_of_front_wheels": 2,
        "number_of_rear_motors": 0,
        "number_of_rear_wheels": 2,
        "front_transmission_id": transmission_loss_coefficients["id"],
        "front_motor_id": motor["id"],
        "battery_id": battery["id"],
    }
    architecture = app.post(client_with_design_instance, "/architectures", data=architecture)
    return architecture


def test_configuration(aero):
    """Test creating an aero configuration."""
    assert aero
    assert aero["config_type"] == "aero"
    assert "id" in aero


def test_component(transmission_loss_coefficients):
    assert transmission_loss_coefficients
    assert "id" in transmission_loss_coefficients


def test_create_requirement(requirement):
    assert requirement
    assert "id" in requirement


def test_architecture(architecture):
    """Test creating an architecture."""
    assert architecture
    assert "id" in architecture


def test_create_from_file(motor_file):
    assert isinstance(motor_file, list)
    assert len(motor_file) == 2
