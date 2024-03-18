"""Integration Tests.

These should test the deployed api's match out cli client.
"""
import datetime
import os
from pathlib import Path

import dotenv
import plotly.graph_objects as go
import pytest

from ansys.conceptev.core import main

dotenv.load_dotenv()
DATADIR = Path(__file__).parents[0]
# Example data can be got from the schema sections of the api docs.

aero1 = {
    "name": "New Aero Config",
    "drag_coefficient": 0.3,
    "cross_sectional_area": 2,
    "config_type": "aero",
}

aero2 = {
    "name": "Second Aero Configuration",
    "drag_coefficient": 0.6,
    "cross_sectional_area": 3,
    "config_type": "aero",
}
mass = {
    "name": "New Mass Config",
    "mass": 3000,
    "config_type": "mass",
}

wheel = {
    "name": "New Wheel Config",
    "rolling_radius": 0.3,
    "config_type": "wheel",
}

transmission = {
    "gear_ratios": [5],
    "headline_efficiencies": [0.95],
    "max_torque": 500,
    "max_speed": 2000,
    "static_drags": [0.5],
    "friction_ratios": [60],
    "windage_ratios": [40],
    "component_type": "TransmissionLossCoefficients",
}

motor_file_name = str(DATADIR.joinpath("e9.lab"))

motor_data = {"name": "e9", "component_type": "MotorLabID", "inverter_losses_included": False}
battery = {
    "capacity": 86400000,
    "charge_acceptance_limit": 0,
    "component_type": "BatteryFixedVoltages",
    "internal_resistance": 0.1,
    "name": "New Battery",
    "voltage_max": 400,
    "voltage_mid": 350,
    "voltage_min": 300,
}


def set_env(env):
    environments = {
        "dev": {
            "CONCEPTEV_URL": "https://dev-conceptev.awsansys3np.onscale.com/api/",
            "OCM_URL": "https://test.portal.onscale.com/api",
            "CONCEPTEV_USERNAME": "philip.usher@ansys.com",
            "CONCEPTEV_PASSWORD": os.environ["CONCEPTEV_PASSWORD_DEV"],
        },
        # OCM Test = ConceptEV Dev
        "test": {
            "CONCEPTEV_URL": "https://test-conceptev.awsansys3np.onscale.com/api/",
            "OCM_URL": "https://dev.portal.onscale.com/api",
            "CONCEPTEV_USERNAME": "philip.usher@ansys.com",
            "CONCEPTEV_PASSWORD": os.environ["CONCEPTEV_PASSWORD_TEST"],
        },
        "prod": {
            "CONCEPTEV_URL": "https://conceptev.ansys.com/api/",
            "OCM_URL": "https://prod.portal.onscale.com/api",
            "CONCEPTEV_USERNAME": "philip.usher@ansys.com",
            "CONCEPTEV_PASSWORD": os.environ["CONCEPTEV_PASSWORD_PROD"],
        },
    }

    config = environments[env]
    os.environ["CONCEPTEV_USERNAME"] = config["CONCEPTEV_USERNAME"]
    os.environ["CONCEPTEV_URL"] = config["CONCEPTEV_URL"]
    os.environ["OCM_URL"] = config["OCM_URL"]
    os.environ["CONCEPTEV_PASSWORD"] = config["CONCEPTEV_PASSWORD"]


@pytest.mark.integration
@pytest.mark.parametrize("env", ["dev", "test", "prod"])
def test_happy_path(env):
    set_env(env)
    token = main.get_token()

    with main.get_http_client(token) as client:  # Create a client to talk to the api
        health = main.get(client, "/health")  # Check the api is healthy
        print(health)
        concepts = main.get(client, "/concepts")  # Get a list of concepts
        print(concepts)

        accounts = main.get_account_ids(token)
        account_id = accounts["conceptev_saas@ansys.com"]
        hpc_id = main.get_default_hpc(token, account_id)
        created_concept = main.create_new_project(
            client, account_id, hpc_id, f"New Project +{datetime.datetime.now()}"
        )  # Create a new concept.

    concept_id = created_concept["id"]  # get the id of the newly created concept.
    design_instance_id = created_concept["design_instance_id"]
    with main.get_http_client(
        token, design_instance_id
    ) as client:  # get client with concept id embedded in
        ### Basic Post(create) and get(read) operations on Configurations

        created_aero = main.post(client, "/configurations", data=aero1)  # create an aero
        created_aero2 = main.post(client, "/configurations", data=aero2)  # create an aero
        created_mass = main.post(client, "/configurations", data=mass)
        created_wheel = main.post(client, "/configurations", data=wheel)

        configurations = main.get(
            client, "/configurations", params={"config_type": "aero"}
        )  # read all aeros
        print(configurations)

        aero = main.get(
            client, "/configurations", id=created_aero["id"]
        )  # get a particular aero configuration
        print(aero)

        ### Create Components
        created_transmission = main.post(
            client, "/components", data=transmission
        )  # create transmission

        motor_loss_map = main.post_component_file(
            client,
            motor_file_name,
            "motor_lab_file"
            # create motor from file
        )
        motor_data["data_id"] = motor_loss_map[0]
        motor_data["max_speed"] = motor_loss_map[1]
        created_motor = main.post(client, "/components", data=motor_data)
        print(created_motor)
        client.timeout = 2000  # Needed as these calculations will take a long time.
        motor_loss_map = main.post(
            client,
            "/components:get_display_data",
            data={},
            params={"component_id": created_motor["id"]},
        )  # get loss map from motor

        x = motor_loss_map["currents"]
        y = motor_loss_map["phase_advances"]
        z = motor_loss_map["losses_total"]
        fig = go.Figure(data=go.Contour(x=x, y=y, z=z))
        fig.show()

        created_battery = main.post(client, "/components", data=battery)  # create battery

        ### Architecture
        architecture = {
            "number_of_front_wheels": 1,
            "number_of_front_motors": 1,
            "front_transmission_id": created_transmission["id"],
            "front_motor_id": created_motor["id"],
            "number_of_rear_wheels": 0,
            "number_of_rear_motors": 0,
            "battery_id": created_battery["id"],
        }
        created_arch = main.post(client, "/architectures", data=architecture)  # create arch

        # Requirements
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
        created_requirement = main.post(client, "requirements", data=requirement)

        ### Submit job
        concept = main.get(client, "/concepts", id=design_instance_id, params={"populated": True})

        job_info = main.create_submit_job(client, concept, account_id, hpc_id)

        ## Read results needs an api update
        results = main.read_results(client, job_info, calculate_units=False)
        x = results[0]["capability_curve"]["speeds"]
        y = results[0]["capability_curve"]["torques"]

        fig = go.Figure(data=go.Scatter(x=x, y=y))
        fig.show()
