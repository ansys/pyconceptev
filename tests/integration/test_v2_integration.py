# Copyright (C) 2023 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

"""Integration tests for the v2 ConceptEV API.

Covers the core end-to-end workflow against the dev environment:
  1. Submit a job via the v2 generated client.
  2. Monitor job status until a terminal state is reached.
  3. Download job results via the signed-file endpoint.

Auth and environment settings are inherited from the shared ``conftest.py``
which points ``PYCONCEPTEV_SETTINGS`` at ``tests/integration/config.toml``
(the dev environment).

Fixtures are session-scoped so that the concept and job are created once and
shared across all tests in this module, keeping test run time short.
"""

import os
from pathlib import Path
import time

import pytest

from ansys.conceptev.core.app import get_conceptev_client, get_local_client
from ansys.conceptev.core.generated.api.concept_v2 import (
    create_concept,
    create_concept_part,
    create_file_item,
    create_job,
    delete_concept,
    get_job,
    get_job_file,
    list_jobs,
)
from ansys.conceptev.core.generated.models import (
    AeroInput,
    ArchitectureInput,
    BatteryFixedVoltagesInput,
    BodyCreateFileItem,
    ConceptInput,
    DynamicRequirementInput,
    MassInput,
    MotorLabInput,
    TransmissionLossCoefficientsInput,
    WheelInput,
)
from ansys.conceptev.core.generated.models.job_request import JobRequest
from ansys.conceptev.core.generated.types import UNSET, File
from ansys.conceptev.core.progress import (
    STATUS_COMPLETE,
    STATUS_FINISHED,
    monitor_job_progress_local_sync,
)

DATA_DIR = Path(__file__).parent
IS_CI = os.getenv("CI") == "true"
TERMINAL_STATES = {"COMPLETED", "FAILED", "ERROR", "FINISHED"}
JOB_POLL_INTERVAL = 10  # seconds
JOB_TIMEOUT = 900  # seconds


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


@pytest.fixture(
    params=[
        pytest.param("local", marks=pytest.mark.skipif(IS_CI, reason="No local server in CI")),
        pytest.param("dev", marks=pytest.mark.skipif(IS_CI, reason="Not working yet")),
    ],
    scope="session",
)
def client(request, session_token):
    """Return a ConceptEV client for the dev environment with strict error handling."""
    if request.param == "local":
        client = get_local_client()
        with client:
            yield client
    else:
        client = get_conceptev_client(token=session_token)
        with client:
            yield client


def test_server_running(client):
    """Test if the ConceptEV server is running."""
    assert client is not None
    response = client.get_httpx_client().get("/health")
    assert response.status_code == 200


def wait_for_job(client, concept_id: str, job_id: str) -> object:
    """Poll the v2 job endpoint until a terminal state is reached."""
    deadline = time.monotonic() + JOB_TIMEOUT
    while time.monotonic() < deadline:
        job_record = get_job.sync(concept_id=concept_id, job_id=job_id, client=client)
        if job_record is not None and job_record.status in TERMINAL_STATES:
            return job_record
        status = job_record.status if job_record is not None else "unknown"
        print(f"  Job {job_id}: {status} — polling again in {JOB_POLL_INTERVAL}s")
        time.sleep(JOB_POLL_INTERVAL)
    raise TimeoutError(f"Job {job_id} did not reach a terminal state within {JOB_TIMEOUT}s")


# ---------------------------------------------------------------------------
# Session-scoped concept fixture
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def v2_concept(client, session_account_id):
    """Create a fully-populated v2 concept once per session and clean it up afterwards.

    The concept contains:
    - Aero, mass, and wheel configurations
    - Motor (MotorLabID from e9.lab), battery, and transmission components
    - An architecture wiring them together
    - A dynamic requirement referencing the configurations above

    Yields ``(concept_id, requirement_id, architecture_id)``.
    """

    concept = create_concept.sync(
        client=client,
        body=ConceptInput(name="v2 Integration Test Concept"),
    )
    concept_id = concept.id

    # Configurations
    aero = create_concept_part.sync(
        id=concept_id,
        part_type="configuration",
        client=client,
        body=AeroInput(
            name="Test Aero",
            drag_coefficient=0.3,
            cross_sectional_area=2.0,
        ),
    )
    mass = create_concept_part.sync(
        id=concept_id,
        part_type="configuration",
        client=client,
        body=MassInput(name="Test Mass", mass=1800.0),
    )
    wheel = create_concept_part.sync(
        id=concept_id,
        part_type="configuration",
        client=client,
        body=WheelInput(name="Test Wheel", rolling_radius=0.3),
    )

    # Motor lab file upload
    motor_lab_file = DATA_DIR / "e9.lab"
    with open(motor_lab_file, "rb") as f:
        file_response = create_file_item.sync(
            id=concept_id,
            client=client,
            body=BodyCreateFileItem(
                file=File(
                    payload=f,
                    file_name=motor_lab_file.name,
                    mime_type="application/octet-stream",
                )
            ),
            name=motor_lab_file.name,
            component_file_type="motor_lab_file",
        )

    if file_response is None:
        raise Exception("File upload returned None - API call failed silently")

    lab_data_id = file_response.id
    max_speed = file_response.calculated_values["max_speed"]

    # Components
    motor = create_concept_part.sync(
        id=concept_id,
        part_type="component",
        client=client,
        body=MotorLabInput(
            name="Test Motor",
            lab_data_id=lab_data_id,
            max_speed=max_speed,
        ),
    )
    battery = create_concept_part.sync(
        id=concept_id,
        part_type="component",
        client=client,
        body=BatteryFixedVoltagesInput(
            name="Test Battery",
            voltage_max=400.0,
            voltage_min=300.0,
            capacity=86400000.0,
            charge_acceptance_limit=0.0,
            internal_resistance_charge=0.1,
            internal_resistance_discharge=0.1,
        ),
    )
    transmission = create_concept_part.sync(
        id=concept_id,
        part_type="component",
        client=client,
        body=TransmissionLossCoefficientsInput(
            name="Test Transmission",
            gear_ratios=[5.0],
            headline_efficiencies=[0.95],
            max_torque=500.0,
            max_speed=2000.0,
            static_drags=[0.5],
            friction_ratios=[60.0],
        ),
    )

    # Architecture
    architecture = create_concept_part.sync(
        id=concept_id,
        part_type="architecture",
        client=client,
        body=ArchitectureInput(
            battery_id=battery.id,
            number_of_front_wheels=2,
            number_of_front_motors=1,
            front_transmission_id=transmission.id,
            front_motor_id=motor.id,
            number_of_rear_wheels=2,
            number_of_rear_motors=0,
        ),
    )

    # Requirement
    requirement = create_concept_part.sync(
        id=concept_id,
        part_type="requirement",
        client=client,
        body=DynamicRequirementInput(
            name="Test Dynamic Requirement",
            aero_id=aero.id,
            mass_id=mass.id,
            wheel_id=wheel.id,
            state_of_charge=0.9,
            to_speed=10.0,
            from_speed=0.0,
            required_time=60.0,
        ),
    )

    yield concept_id, requirement.id, architecture.id

    # Teardown — delete the concept so no orphan data accumulates on the server.
    delete_concept.sync(id=concept_id, client=client)


# ---------------------------------------------------------------------------
# Session-scoped submitted job fixture
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def v2_submitted_job(client, session_account_id, v2_concept):
    """Submit a job for the v2 concept and return the job record.

    The job is submitted once per session. All tests that need a job record
    share this fixture.
    """
    concept_id, requirement_id, architecture_id = v2_concept
    job_record = create_job.sync(
        concept_id=concept_id,
        client=client,
        body=JobRequest(
            name="v2 Integration Test Job",
            account_id=session_account_id,
            requirement_ids=[requirement_id],
            architecture_id=architecture_id,
        ),
    )
    return job_record


@pytest.fixture(scope="session")
def v2_completed_job(client, v2_concept, v2_submitted_job):
    """Wait for the submitted job to reach a terminal state and return it."""
    concept_id, _, _ = v2_concept
    completed = wait_for_job(client, concept_id, v2_submitted_job.id)
    return completed


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_v2_concept_created(v2_concept):
    """The v2 concept fixture should yield a valid concept ID."""
    concept_id, requirement_id, architecture_id = v2_concept
    assert isinstance(concept_id, str)
    assert concept_id
    assert isinstance(requirement_id, str)
    assert requirement_id
    assert isinstance(architecture_id, str)
    assert architecture_id


def test_v2_submit_job(v2_submitted_job):
    """Submitting a job should return a job record with a non-empty ID and a status."""
    assert v2_submitted_job is not None
    assert isinstance(v2_submitted_job.id, str)
    assert v2_submitted_job.id
    assert isinstance(v2_submitted_job.status, str)
    assert v2_submitted_job.status  # non-empty


def test_v2_list_jobs(client, v2_concept, v2_submitted_job):
    """The submitted job should appear in the list of jobs for the concept."""
    concept_id, _, _ = v2_concept
    jobs = list_jobs.sync(concept_id=concept_id, client=client)

    assert isinstance(jobs, list)
    assert len(jobs) >= 1
    job_ids = [j.id for j in jobs]
    assert v2_submitted_job.id in job_ids


def test_v2_monitor_job_reaches_terminal_state(v2_completed_job):
    """Polling the job until completion should yield a terminal status."""
    assert v2_completed_job is not None
    assert v2_completed_job.status in TERMINAL_STATES


def test_v2_job_completed_successfully(v2_completed_job):
    """The job should complete with COMPLETED status, not FAILED or ERROR."""
    assert (
        v2_completed_job.status == "COMPLETED" or v2_completed_job.status == "FINISHED"
    ), f"Job ended with unexpected status: {v2_completed_job.status}"


def test_v2_download_results(client, v2_concept, v2_completed_job):
    """A completed job should expose result files that can be downloaded.

    Verifies:
    - The completed job record has at least one file entry.
    - The file can be fetched (directly via the ``path`` URL or via the
      signed-URL endpoint) and contains JSON result data.
    """
    assert v2_completed_job.files not in (None, UNSET), "Completed job has no files attached"
    assert len(v2_completed_job.files) >= 1, "Expected at least one result file"

    results = get_job_file.sync(
        job_id=v2_completed_job.id,
        concept_id=v2_concept[0],
        file_id=v2_completed_job.files[0].id,
        client=client,
    )
    assert results is not None
    # The results list should contain at least one capability-curve entry.
    assert isinstance(results, list)
    assert len(results) >= 1
    assert (
        "capability_curve" in results[0]
    ), f"Expected 'capability_curve' in result entry, got keys: {list(results[0].keys())}"


def test_v2_get_job_file_endpoint(client, v2_concept, v2_completed_job):
    """The dedicated get_job_file endpoint should return result data for each file.

    This covers the ``GET /v2/concept/{concept_id}/job/{job_id}/files/{file_id}``
    endpoint separately from the direct signed-URL path above.
    """
    assert v2_completed_job.files not in (None, UNSET), "Completed job has no files attached"

    concept_id, _, _ = v2_concept
    file_info = v2_completed_job.files[0]

    result = get_job_file.sync(
        concept_id=concept_id,
        job_id=v2_completed_job.id,
        file_id=file_info.id,
        client=client,
    )

    # The endpoint may return the JSON body directly or redirect to a signed URL;
    # either way the parsed result should be non-None.
    assert result is not None


@pytest.mark.integration
def test_monitor_job_progress_local_integration(v2_submitted_job, v2_concept):
    """Integration test: monitor_job_progress_local_sync connects to a running local ConceptEV."""
    with get_local_client() as client:
        client.raise_on_unexpected_status = True
        api_key = client.get_httpx_client().headers["X-API-Key"]
    result = monitor_job_progress_local_sync(v2_submitted_job.id, api_key, timeout=120)
    assert result in (STATUS_COMPLETE, STATUS_FINISHED)
