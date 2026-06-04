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
"""
Simple workflow
===============

This example shows how to use PyConceptEV to perform basic operations using
the v2 API against a locally running ConceptEV service.

- Required imports
- Define example data
- Connect to the local ConceptEV service
- Create a concept
- Add configurations, components, architecture, and requirements
- Submit a job and plot the results
"""

# %%
# Perform Required imports
# ------------------------

import time
from pathlib import Path

import matplotlib.pyplot as plt

from ansys.conceptev.core.app import get_local_client
from ansys.conceptev.core.generated.api.concept_v2 import (
    create_concept,
    create_concept_part,
    create_file_item,
    create_job,
    delete_concept,
    get_component_display_data,
    get_job,
)
from ansys.conceptev.core.generated.models import (
    AeroInput,
    ArchitectureInput,
    BatteryFixedVoltagesInput,
    BodyCreateFileV2ConceptIdFilesPost,
    ConceptInput,
    DynamicRequirementInput,
    MassInput,
    MotorLabInput,
    TransmissionLossCoefficientsInput,
    WheelInput,
)
from ansys.conceptev.core.generated.models.job_request import JobRequest

# %%
# Define example data
# ---------------------
# You can obtain example data from the schema sections of the API documentation.

MOTOR_LAB_FILE = Path("resources") / "e9.lab"

# %%
# Connect to the local ConceptEV service and create a concept
# ------------------------------------------------------------
# Create a client that connects to the locally running ConceptEV service at
# http://127.0.0.1:8080/api.  No authentication is required for the local server.

with get_local_client() as client:

    # Create a new concept (study) on the server.
    concept = create_concept.sync(
        client=client,
        body=ConceptInput(name="Simple Workflow Study"),
    )
    print(f"Created concept with ID: {concept.id}\n")
    concept_id = concept.id

    # %%
    # Add configurations
    # ------------------
    # Create aero, mass, and wheel configurations and attach them to the concept.

    created_aero = create_concept_part.sync(
        id=concept_id,
        part_type="configuration",
        client=client,
        body=AeroInput(
            name="New Aero Config",
            drag_coefficient=0.3,
            cross_sectional_area=2.0,
        ),
    )
    print(f"Created aero config with ID: {created_aero.id}\n")

    created_aero2 = create_concept_part.sync(
        id=concept_id,
        part_type="configuration",
        client=client,
        body=AeroInput(
            name="Second Aero Configuration",
            drag_coefficient=0.6,
            cross_sectional_area=3.0,
        ),
    )

    created_mass = create_concept_part.sync(
        id=concept_id,
        part_type="configuration",
        client=client,
        body=MassInput(name="New Mass Config", mass=3000.0),
    )
    print(f"Created mass config with ID: {created_mass.id}\n")

    created_wheel = create_concept_part.sync(
        id=concept_id,
        part_type="configuration",
        client=client,
        body=WheelInput(name="New Wheel Config", rolling_radius=0.3),
    )
    print(f"Created wheel config with ID: {created_wheel.id}\n")

    # %%
    # Add components
    # --------------
    # Create a transmission component.

    created_transmission = create_concept_part.sync(
        id=concept_id,
        part_type="component",
        client=client,
        body=TransmissionLossCoefficientsInput(
            name="New Transmission",
            gear_ratios=[5.0],
            headline_efficiencies=[0.95],
            max_torque=500.0,
            max_speed=2000.0,
            static_drags=[0.5],
            friction_ratios=[60.0],
        ),
    )
    print(f"Created transmission with ID: {created_transmission.id}\n")

    # %%
    # Upload a motor lab file and create a motor component
    # ----------------------------------------------------
    # Upload the .lab file to obtain a file ID and the extracted max speed.
    # Then create a MotorLabInput component that references that file.

    with open(MOTOR_LAB_FILE, "rb") as f:
        file_response = create_file_item.sync(
            id=concept_id,
            client=client,
            body=BodyCreateFileV2ConceptIdFilesPost(file=f.read().decode("latin-1")),
            name=MOTOR_LAB_FILE.name,
            component_file_type="motor_lab_file",
        )
    print(f"Uploaded motor lab file, file ID: {file_response.id}\n")

    lab_data_id = file_response.id
    max_speed = file_response.calculated_values["max_speed"]

    created_motor = create_concept_part.sync(
        id=concept_id,
        part_type="component",
        client=client,
        body=MotorLabInput(
            name="e9",
            lab_data_id=lab_data_id,
            max_speed=max_speed,
        ),
    )
    print(f"Created motor with ID: {created_motor.id}\n")

    # %%
    # Get display data (loss map) for the motor
    # -----------------------------------------
    # Retrieve and plot the motor loss map.

    loss_map = get_component_display_data.sync(
        id=concept_id,
        part_id=created_motor.id,
        client=client,
        body=None,
    )

    if loss_map is not None and hasattr(loss_map, "currents"):
        x = loss_map.currents
        y = loss_map.phase_advances
        z = loss_map.losses_total

        fig, ax = plt.subplots()
        im = ax.pcolormesh(x, y, z)
        ax.set_xlabel("Currents (A)")
        ax.set_ylabel("Phase Advances (deg)")
        fig.colorbar(im, ax=ax, label="Total Losses (W)")
        plt.show()

    # %%
    # Add battery component
    # ---------------------

    created_battery = create_concept_part.sync(
        id=concept_id,
        part_type="component",
        client=client,
        body=BatteryFixedVoltagesInput(
            name="New Battery",
            voltage_max=400.0,
            voltage_min=300.0,
            capacity=86400000.0,
            charge_acceptance_limit=0.0,
            internal_resistance_charge=0.1,
            internal_resistance_discharge=0.1,
        ),
    )
    print(f"Created battery with ID: {created_battery.id}\n")

    # %%
    # Create an architecture
    # ----------------------
    # Wire together motor, transmission, and battery into a front-motor architecture.

    created_arch = create_concept_part.sync(
        id=concept_id,
        part_type="architecture",
        client=client,
        body=ArchitectureInput(
            battery_id=created_battery.id,
            number_of_front_wheels=2,
            number_of_front_motors=1,
            front_transmission_id=created_transmission.id,
            front_motor_id=created_motor.id,
            number_of_rear_wheels=2,
            number_of_rear_motors=0,
        ),
    )
    print(f"Created architecture with ID: {created_arch.id}\n")

    # %%
    # Create a requirement
    # --------------------
    # Add a dynamic (acceleration) requirement referencing the configurations above.

    created_requirement = create_concept_part.sync(
        id=concept_id,
        part_type="requirement",
        client=client,
        body=DynamicRequirementInput(
            name="Dynamic Requirement 1",
            aero_id=created_aero.id,
            mass_id=created_mass.id,
            wheel_id=created_wheel.id,
            state_of_charge=0.9,
        ),
    )
    print(f"Created requirement with ID: {created_requirement.id}\n")

    # %%
    # Submit a job and poll until complete
    # -------------------------------------
    # Create a job that runs the requirement against the architecture.

    job_record = create_job.sync(
        concept_id=concept_id,
        client=client,
        body=JobRequest(
            name="Simple Workflow Job",
            requirement_ids=[created_requirement.id],
            architecture_id=created_arch.id,
        ),
    )
    print(f"Submitted job with ID: {job_record.id}, status: {job_record.status}\n")

    # Poll until the job reaches a terminal state.
    terminal_states = {"COMPLETED", "FAILED", "ERROR"}
    while job_record.status not in terminal_states:
        time.sleep(5)
        job_record = get_job.sync(
            concept_id=concept_id,
            job_id=job_record.id,
            client=client,
        )
        print(f"Job status: {job_record.status}")

    print(f"Job finished with status: {job_record.status}\n")

    # %%
    # Plot capability curve from results
    # -----------------------------------
    # Read the results from the completed job and display a capability curve.

    if job_record.status == "COMPLETED" and job_record.output_urls:
        import httpx as _httpx  # noqa: PLC0415

        results_url = job_record.output_urls[0]
        results = _httpx.get(results_url).json()
        x = results[0]["capability_curve"]["speeds"]
        y = results[0]["capability_curve"]["torques"]

        fig, ax = plt.subplots()
        ax.scatter(x, y, label="Capability Curve")
        ax.set_xlabel("Speed (rad/s)")
        ax.set_ylabel("Torque (Nm)")
        plt.show()

    # %%
    # Clean up
    # --------
    # Delete the concept from the server when finished.

    delete_concept.sync(id=concept_id, client=client)
    print(f"Deleted concept {concept_id}")
