# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
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

# # Get Results workflow
#
# This example shows how to use PyConcentEV to get a list of result parameters
# from a list of design_instance_ids
# These lists are provided in design_instance_ids.csv

# Perform required imports.

import json

import httpx
import pandas as pd

from ansys.conceptev.core import app, auth

# INPUTS
filename = "resources/design_instance_ids.csv"
short_results = True  # For results created after 15/11/2024 improved performance.

get_results_off_server = True  # Turn to false to read from file. See script for details.
# -------Limitations -------------------------#
# If short results is true it gets in User Units
# If short results not true and if you have large results file
# it will probably timeout with a gateway error.
# Assumes first job in list for each project is the result we want. Assumes no "re-calculation".
# Assumes name of Drive Cycle Requirements "UDDS_50%" and "HWFET_50%"
# Assumes a 2 motor architecture
#


# -----------TO DO --------------------#
# Merge cells on headers
# Units not outputted to excel
# Non same component order
# Front/rear clutch?
# progress bar
# save each result file after download so it does not have to download everything
# and if it breaks on one file it does not stop the whole thing


# ------------------------------#


def get_job_info(token, job_id):
    ocm_url = auth.config["OCM_URL"]
    response = httpx.post(
        url=f"{ocm_url}/job/load", headers={"authorization": token}, json={"jobId": job_id}
    )
    response = app.process_response(response)
    job_info = {
        "job_id": job_id,
        "simulation_id": response["simulations"][0]["simulationId"],
        "job_name": response["jobName"],
        "docker_tag": response["dockerTag"],
    }
    return job_info


def get_design_title(token, design_instance_id):
    ocm_url = auth.config["OCM_URL"]
    response = httpx.post(
        url=f"{ocm_url}/design/instance/load",
        headers={"authorization": token},
        json={"designInstanceId": design_instance_id},
    )
    response = app.process_response(response)
    design = httpx.post(
        url=f"{ocm_url}/design/load",
        headers={"authorization": token},
        json={"designId": response["designId"]},
    )
    design = app.process_response(design)
    return design["designTitle"]


def get_component_map(client, design_instance_id):
    components = client.get(f"/concepts/{design_instance_id}/components")
    components = app.process_response(components)
    return {component["id"]: component["name"] for component in components}


def get_project_results(client, design_instance_id, token):
    client.params = {"design_instance_id": design_instance_id}
    concept = app.get(client, "/concepts", id=design_instance_id)

    job_id = concept["jobs_ids"][0]  # get ONLY the first id from each project.
    job_info = get_job_info(token, job_id)
    results = app.read_results(
        client, job_info, calculate_units=short_results, filtered=short_results
    )
    # Need to get, Project Name, Component Name, Cost
    arch_id = concept["architecture_id"]
    architecture = app.get(client, f"/architectures/{arch_id}")
    project_results = {
        "architecture": architecture,
        "cost": architecture["components_cost"],
        "design_instance_id": design_instance_id,
        "component_map": get_component_map(client, design_instance_id),
        "design_name": get_design_title(token, design_instance_id),
        "results": results,
    }
    return project_results


def get_results(design_instance_ids):

    msal_app = auth.create_msal_app()
    token = auth.get_ansyId_token(msal_app)

    with app.get_http_client(token) as client:
        client.timeout = 2000
        project_results = [
            get_project_results(client, design_instance_id, token)
            for design_instance_id in design_instance_ids
        ]
    return project_results


def get_component_name(project_result, name):
    name = project_result["component_map"].get(project_result["architecture"][name], "")
    return name


def get_drive_cycle_result(project_result, name):
    """Assumes the first requirement in a concept with the matching name is the one we want."""
    requirement = [
        result for result in project_result["results"] if result["requirement"]["name"] == name
    ][0]
    return requirement


if __name__ == "__main__":

    # Get Results off server
    if get_results_off_server:
        design_instance_ids = pd.read_csv(filename, header=None)[0]
        project_results = get_results(design_instance_ids)
        with open("project_results.json", "w") as f:
            json.dump(project_results, f)
    else:
        with open("project_results.json", "r") as f:
            project_results = json.load(f)
    # Create data we want.

    output_results = []
    for project_result in project_results:
        # UDDS
        UDDS_result = get_drive_cycle_result(project_result, "UDDS_50%")
        Range_UDDS = UDDS_result["vehicle_range"]
        UDDS_efficiency = UDDS_result["efficiency"]
        UDDS_Component_Loss = UDDS_result["total_values"]["loss_by_component"]
        # HWFET
        HWFET_result = get_drive_cycle_result(project_result, "HWFET_50%")
        Range_HWFET_50 = HWFET_result["vehicle_range"]
        HWFET_50_efficiency = HWFET_result["efficiency"]
        HWFET_50_Component_Loss = HWFET_result["total_values"]["loss_by_component"]

        # Component Names
        front_tranmsission_name = (
            get_component_name(project_result, "front_transmission_id") + " (Front)"
        )
        front_motor_name = get_component_name(project_result, "front_motor_id") + " (Front)"
        front_inverter_name = get_component_name(project_result, "front_inverter_id") + " (Front)"
        front_disconnect_clutch_name = (
            get_component_name(project_result, "front_clutch_id") + " (Front)"
        )
        rear_transmission_name = (
            get_component_name(project_result, "rear_transmission_id") + " (Rear)"
        )
        rear_motor_name = get_component_name(project_result, "rear_motor_id") + " (Rear)"
        rear_inverter_name = get_component_name(project_result, "rear_inverter_id") + " (Rear)"
        rear_disconnect_clutch_name = (
            get_component_name(project_result, "rear_clutch_id") + " (Rear)"
        )
        battery_name = get_component_name(project_result, "battery_id")

        # todo check front/rear

        # Each row of Excel
        output_results.append(
            {
                "Project Name": project_result["design_name"],
                "Design Instance Id": project_result["design_instance_id"],
                "Front Transmission": front_tranmsission_name,
                "Front Motor": front_motor_name,
                "Front Inverter": front_inverter_name,
                "Rear Transmission": rear_inverter_name,
                "Rear Motor": rear_motor_name,
                "Rear Inverter": rear_inverter_name,
                "Battery": battery_name,
                "Cost": project_result["cost"],
                "Range UDDS": Range_UDDS,
                "Range HWFET": Range_HWFET_50,
                "UDDS efficiency": UDDS_efficiency,
                "HWFET efficiency": HWFET_50_efficiency,
                "Weighted Efficiency": (0.6 * UDDS_efficiency + 0.4 * HWFET_50_efficiency) * -1.0,
                ("UDDS Losses", "Battery"): UDDS_Component_Loss[battery_name],
                ("UDDS Losses", "Front disconnect clutch"): UDDS_Component_Loss.get(
                    front_disconnect_clutch_name, None
                ),
                ("UDDS Losses", "Front transmission"): UDDS_Component_Loss[front_tranmsission_name],
                ("UDDS Losses", "Front inverter"): UDDS_Component_Loss[front_inverter_name],
                ("UDDS Losses", "Front motor"): UDDS_Component_Loss[front_motor_name],
                ("UDDS Losses", "Rear disconnect clutch"): UDDS_Component_Loss.get(
                    rear_disconnect_clutch_name, None
                ),
                ("UDDS Losses", "Rear transmission"): UDDS_Component_Loss[rear_transmission_name],
                ("UDDS Losses", "Rear inverter"): UDDS_Component_Loss[rear_inverter_name],
                ("UDDS Losses", "Rear motor"): UDDS_Component_Loss[rear_motor_name],
                ("HWFET Losses", "Battery"): HWFET_50_Component_Loss[battery_name],
                ("HWFET Losses", "Front disconnect clutch"): HWFET_50_Component_Loss.get(
                    front_disconnect_clutch_name, None
                ),
                ("HWFET Losses", "Front transmission"): HWFET_50_Component_Loss[
                    front_tranmsission_name
                ],
                ("HWFET Losses", "Front inverter"): HWFET_50_Component_Loss[front_inverter_name],
                ("HWFET Losses", "Front motor"): HWFET_50_Component_Loss[front_motor_name],
                ("HWFET Losses", "Rear disconnect clutch"): HWFET_50_Component_Loss.get(
                    rear_disconnect_clutch_name, None
                ),
                ("HWFET Losses", "Rear transmission"): HWFET_50_Component_Loss[
                    rear_transmission_name
                ],
                ("HWFET Losses", "Rear inverter"): HWFET_50_Component_Loss[rear_inverter_name],
                ("HWFET Losses", "Rear motor"): HWFET_50_Component_Loss[rear_motor_name],
            }
        )
    all_results = pd.DataFrame(output_results)
    all_results.to_excel("output.xlsx")
