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

"""
Local ConceptEV v2 study
========================

Helpers for self-contained local ConceptEV v2 examples.
"""

from pathlib import Path

from ansys.conceptev.core.generated.api.concept_v2 import (
    create_concept,
    create_concept_part,
    create_file_item,
    create_job,
)
from ansys.conceptev.core.generated.models import (
    AeroInput,
    ArchitectureInput,
    BatteryFixedVoltagesInput,
    BodyCreateFileItem,
    ConceptInput,
    MassInput,
    MotorLabInput,
    StaticRequirementInput,
    TransmissionLossCoefficientsInput,
    WheelInput,
)
from ansys.conceptev.core.generated.models.job_request import JobRequest
from ansys.conceptev.core.generated.types import File

MOTOR_LAB_FILE = Path(__file__).parent / "resources" / "e9.lab"


def create_local_study(client, name: str, mass: float = 2000.0) -> tuple[str, str, str]:
    """Create a complete local ConceptEV study and return its IDs."""
    concept = create_concept.sync(client=client, body=ConceptInput(name=name))
    concept_id = concept.id
    aero = create_concept_part.sync(
        id=concept_id,
        part_type="configuration",
        client=client,
        body=AeroInput(name="Aero", drag_coefficient=0.3, cross_sectional_area=2.0),
    )
    vehicle_mass = create_concept_part.sync(
        id=concept_id,
        part_type="configuration",
        client=client,
        body=MassInput(name="Mass", mass=mass),
    )
    wheel = create_concept_part.sync(
        id=concept_id,
        part_type="configuration",
        client=client,
        body=WheelInput(name="Wheel", rolling_radius=0.3),
    )
    transmission = create_concept_part.sync(
        id=concept_id,
        part_type="component",
        client=client,
        body=TransmissionLossCoefficientsInput(
            name="Transmission",
            gear_ratios=[5.0],
            headline_efficiencies=[0.95],
            max_torque=500.0,
            max_speed=2000.0,
            static_drags=[0.5],
            friction_ratios=[60.0],
        ),
    )
    with open(MOTOR_LAB_FILE, "rb") as motor_file:
        uploaded_file = create_file_item.sync(
            id=concept_id,
            client=client,
            body=BodyCreateFileItem(
                file=File(
                    payload=motor_file,
                    file_name=MOTOR_LAB_FILE.name,
                    mime_type="application/octet-stream",
                )
            ),
            name=MOTOR_LAB_FILE.name,
            component_file_type="motor_lab_file",
        )
    motor = create_concept_part.sync(
        id=concept_id,
        part_type="component",
        client=client,
        body=MotorLabInput(
            name="Motor",
            lab_data_id=uploaded_file.id,
            max_speed=uploaded_file.calculated_values["max_speed"],
        ),
    )
    battery = create_concept_part.sync(
        id=concept_id,
        part_type="component",
        client=client,
        body=BatteryFixedVoltagesInput(
            name="Battery",
            voltage_max=400.0,
            voltage_min=300.0,
            capacity=86400000.0,
            charge_acceptance_limit=0.0,
            internal_resistance_charge=0.1,
            internal_resistance_discharge=0.1,
        ),
    )
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
    requirement = create_concept_part.sync(
        id=concept_id,
        part_type="requirement",
        client=client,
        body=StaticRequirementInput(
            name="Requirement",
            aero_id=aero.id,
            mass_id=vehicle_mass.id,
            wheel_id=wheel.id,
            state_of_charge=0.9,
        ),
    )
    return concept_id, requirement.id, architecture.id


def submit_local_job(client, concept_id: str, requirement_id: str, architecture_id: str, name: str):
    """Submit a local job for a study."""
    return create_job.sync(
        concept_id=concept_id,
        client=client,
        body=JobRequest(
            name=name,
            requirement_ids=[requirement_id],
            architecture_id=architecture_id,
        ),
    )
