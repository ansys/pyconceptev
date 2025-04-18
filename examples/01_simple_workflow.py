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
"""
Simple workflow
===============

This example shows how to use PyConcentEV to perform basic operations.
- Required imports
- Define example data
- Get a token from Ansys ID
- Use API client for the Ansys ConceptEV service
"""

# %%
# Perform Required imports
# ------------------------

import datetime
from pathlib import Path

import matplotlib.pyplot as plt

from ansys.conceptev.core import app

# %%
# Define example data
# ---------------------
# You can obtain example data from the schema sections of the API documentation.

MOTOR_LAB_FILE = Path("resources") / "e9.lab"
MOTOR_LOSS_MAP_FILE = Path("resources") / "e9.xlsx"
AERO_1 = {
    "name": "New Aero Config",
    "drag_coefficient": 0.3,
    "cross_sectional_area": 2,
    "config_type": "aero",
}

AERO_2 = {
    "name": "Second Aero Configuration",
    "drag_coefficient": 0.6,
    "cross_sectional_area": 3,
    "config_type": "aero",
}

MASS = {
    "name": "New Mass Config",
    "mass": 3000,
    "config_type": "mass",
}

WHEEL = {
    "name": "New Wheel Config",
    "rolling_radius": 0.3,
    "config_type": "wheel",
}

TRANSMISSION = {
    "gear_ratios": [5],
    "headline_efficiencies": [0.95],
    "max_torque": 500,
    "max_speed": 2000,
    "static_drags": [0.5],
    "friction_ratios": [60],
    "windage_ratios": [40],
    "component_type": "TransmissionLossCoefficients",
}

BATTERY = {
    "capacity": 86400000,
    "charge_acceptance_limit": 0,
    "component_type": "BatteryFixedVoltages",
    "internal_resistance": 0.1,
    "name": "New Battery",
    "voltage_max": 400,
    "voltage_mid": 350,
    "voltage_min": 300,
}

motor_data = {"name": "e9", "component_type": "MotorLabID", "inverter_losses_included": False}

# %%
# Use API client for the Ansys ConceptEV service
# ----------------------------------------------
# Use the API client to perform basic operations on the Ansys ConceptEV service.
# Such as:
# - Check api connection is healthy.
# - Get the account ID and HPC ID.
# - Create a new project.
# - Create a new concept within that project.


with app.get_http_client() as client:
    health = app.get(client, "/health")
    print(f"API is healthy: {health}\n")
    token = app.get_token(client)
    account_id = app.get_account_id(token)

    hpc_id = app.get_default_hpc(token, account_id)
    product_id = app.get_product_id(token)
    # Uncomment to print HPC ID
    # print(f"HPC ID: {hpc_id}\n")
    # Create a project
    project = app.create_new_project(
        client, account_id, hpc_id, f"New Project +{datetime.datetime.now()}"
    )
    print(f"ID of the created project: {project['projectId']}")

    # Create a concept with that project

    concept = app.create_new_concept(
        client, project["projectId"], product_id, f"New Concept +{datetime.datetime.now()}"
    )
    print(f"ID of the created concept: {concept['id']}")

# %%
# Perform basic operations
# ------------------------
# Perform basic operations on the design instance associated with the new project.
# Such as:
# - Create configurations.
# - Create components.
# - Create architectures.
# - Create requirements.
# - Create and submit a job.
# - Read the results and show the result in your browser.

design_instance_id = concept["design_instance_id"]

with app.get_http_client(design_instance_id=design_instance_id) as client:

    # Create configurations
    created_aero = app.post(client, "/configurations", data=AERO_1)
    created_aero2 = app.post(client, "/configurations", data=AERO_2)
    created_mass = app.post(client, "/configurations", data=MASS)
    created_wheel = app.post(client, "/configurations", data=WHEEL)

    # Read all aero configurations
    configurations = app.get(
        client, f"/concepts/{design_instance_id}/configurations", params={"config_type": "aero"}
    )
    # Uncomment to print configurations
    # print(f"List of configurations: {configurations}\n")

    # Get a specific aero configuration
    aero = app.get(client, "/configurations", id=created_aero["id"])
    print(f"First created areo configuration: {aero}\n")

    # Create component
    created_transmission = app.post(client, "/components", data=TRANSMISSION)

    # Create component from file
    motor_lab = app.post_component_file(client, MOTOR_LAB_FILE, "motor_lab_file")
    motor_data["data_id"] = motor_lab[0]
    motor_data["max_speed"] = motor_lab[1]

    created_motor_lab = app.post(client, "/components", data=motor_data)
    print(f"Created motor: {created_motor_lab}\n")

    # Create loss map motor component from file
    client.timeout = 2000
    motor_loss_map = app.post_component_file(client, MOTOR_LOSS_MAP_FILE, "motor_torque_grid_file")
    loss_map_motor_data = {
        "name": "e9_loss_map",
        "component_type": "MotorLossMapID",
        "poles": 8,
        "data_id": motor_loss_map[0],
    }

    created_motor = app.post(client, "/components", data=loss_map_motor_data)
    print(f"Created motor: {created_motor}\n")

    # Extend client timeout to get loss map from the motor
    client.timeout = 2000
    motor_loss_map = app.post(
        client,
        "/components:get_display_data",
        data={},
        params={"component_id": created_motor_lab["id"]},
    )

    # Show a figure of the loss map from the motor in you browser
    x = motor_loss_map["currents"]
    y = motor_loss_map["phase_advances"]
    z = motor_loss_map["losses_total"]

    fig, ax = plt.subplots()
    im = ax.pcolormesh(x, y, z)
    ax.set_xlabel("Currents (A)")
    ax.set_ylabel("Phase Advances (deg)")
    fig.colorbar(im, ax=ax, label="Total Losses (W)")
    plt.show()

    created_battery = app.post(client, "/components", data=BATTERY)

    # Create an architecture
    architecture = {
        "number_of_front_wheels": 2,
        "number_of_front_motors": 1,
        "front_transmission_id": created_transmission["id"],
        "front_motor_id": created_motor["id"],
        "number_of_rear_wheels": 2,
        "number_of_rear_motors": 0,
        "battery_id": created_battery["id"],
    }
    created_arch = app.post(client, "/architectures", data=architecture)
    print(f"Created architecture: {created_arch}\n")

    # Create a requirement
    requirement = {
        "speed": 10,
        "acceleration": 1,
        "aero_id": created_aero["id"],
        "mass_id": created_mass["id"],
        "wheel_id": created_wheel["id"],
        "state_of_charge": 0.9,
        "requirement_type": "static_acceleration",
        "name": "Static Requirement 1",
    }
    created_requirement = app.post(client, "requirements", data=requirement)
    print(f"Created requirement: {created_requirement}")

    # Create and submit a job
    concept = app.get(client, "/concepts", id=design_instance_id, params={"populated": True})
    job_info = app.create_submit_job(client, concept, account_id, hpc_id)

    # Read and plot the results
    results = app.read_results(client, job_info, calculate_units=False, filtered=True)
    x = results[0]["capability_curve"]["speeds"]
    y = results[0]["capability_curve"]["torques"]

    fig, ax = plt.subplots()
    fig = ax.scatter(x, y, label="Capability Curve")
    ax.set_xlabel("Speed (rad/s)")
    ax.set_ylabel("Torque (Nm)")
    plt.show()


# %%
# Delete the extra project on the server.
# ---------------------------------------
# Delete the project on the server.
#
# .. warning::
#    This will delete the project and all its contents.
#    Only needed for keep test environment clean.

with app.get_http_client() as client:

    client.params = client.params.set("design_instance_id", concept["design_instance_id"])
    app.delete(client, "concepts", id=concept["id"])
    app.delete_project(concept["project_id"], token)
    print(f"Deleted project {concept['project_id']}")
