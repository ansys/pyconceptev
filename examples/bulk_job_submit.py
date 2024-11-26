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

import datetime

import httpx
import pandas as pd

from ansys.conceptev.core import app, auth

# Inputs
filename = "resources/combinations.csv"
base_concept_id = "a05c7f7d-4c77-48d9-98d2-19b1244718d5"  # Replace with your base concept ID

component_order = {
    "front_transmission_id": "Front Transmission",
    "front_motor_id": "Front Motor",
    "front_inverter_id": "Front Inverter",
    "rear_transmission_id": "Rear Transmission",
    "rear_motor_id": "Rear Motor",
    "rear_inverter_id": "Rear Inverter",
    "battery_id": "Battery",
    "clutch_id": "Clutch",
}


def get_component_id_map(client, design_instance_id):
    components = client.get(f"/concepts/{design_instance_id}/components")
    components = app.process_response(components)
    return {component["name"]: component["id"] for component in components}


def add_clutch(arch, combo):
    if "IPM" in combo["Front Motor"]:
        arch["front_clutch_id"] = arch.pop("clutch_id")
    elif "IPM" in combo["Rear Motor"]:
        arch["rear_clutch_id"] = arch.pop("clutch_id")
    elif not ("IPM" in combo["Front Motor"]) and not ("IPM" in combo["Rear Motor"]):
        arch.pop("clutch_id")
        pass
    else:
        raise Exception("Don't know how to add clutch.")
    return arch


def update_architecture(components, combo):
    # Update Architecture
    arch = {key: components[combo[value]] for key, value in component_order.items()}
    arch = add_clutch(arch, combo)
    arch["number_of_front_wheels"] = 2
    arch["number_of_front_motors"] = 1
    arch["number_of_rear_wheels"] = 2
    arch["number_of_rear_motors"] = 1
    return arch


def create_design_instance(project_id, title):
    osm_url = auth.config["OCM_URL"]

    product_id = app.get_product_id(token)

    design_data = {
        "projectId": project_id,
        "productId": product_id,
        "designTitle": title,
    }
    created_design = httpx.post(
        osm_url + "/design/create", headers={"Authorization": token}, json=design_data
    )

    if created_design.status_code not in (200, 204):
        raise Exception(f"Failed to create a design on OCM {created_design.content}.")

    design_instance_id = created_design.json()["designInstanceList"][0]["designInstanceId"]
    return design_instance_id


def copy_concept(base_concept_id, design_instance_id):
    copy = {
        "old_design_instance_id": base_concept_id,
        "new_design_instance_id": design_instance_id,
        "copy_jobs": False,
    }
    # Clone the base concept
    params = {"design_instance_id": design_instance_id, "populated": False}
    client.params = params
    concept = app.post(client, "/concepts:copy", data=copy)
    return concept


def get_project_id(design_instance_id: str) -> str:
    """Get the project ID from the design instance ID."""
    osm_url = auth.config["OCM_URL"]
    project_id = httpx.post(
        osm_url + f"/design/instance/load",
        json={"designInstanceId": design_instance_id},
        headers={"Authorization": token},
    )
    if project_id.status_code != 200:
        raise Exception(f"Failed to get project ID from OCM {project_id.content}.")
    return project_id.json()["projectId"]


# Read combinations from a csv file.
combinations = pd.read_csv(filename)
combinations = combinations.to_dict("records")
# Authenticate and get a token
msal_app = app.auth.create_msal_app()
token = app.auth.get_ansyId_token(msal_app)

# Use API client for the Ansys ConceptEV service
with app.get_http_client(token) as client:
    client.timeout = 200
    accounts = app.get_account_ids(token)
    account_id = accounts["conceptev_saas@ansys.com"]
    hpc_id = app.get_default_hpc(token, account_id)
    base_components = get_component_id_map(client, base_concept_id)
    # Check component headers are correct
    component_types = set(component_order.values())
    component_types_from_combo_header = set(combinations[0].keys())
    assert component_types <= component_types_from_combo_header, component_types.difference(
        component_types_from_combo_header
    )
    # check combinations are in ref project
    component_names_from_combo = set([value for combo in combinations for value in combo.values()])
    component_names_from_base = set(base_components.keys())
    assert (
        component_names_from_combo <= component_names_from_base
    ), component_names_from_combo.difference(component_names_from_base)
    # Create a new project and copy Ref in as Ref.
    ref_project_id = get_project_id(base_concept_id)
    created_designs = []
    # Submit jobs for each combination
    for combo in combinations:
        try:
            title = f"F_{combo['Front Motor']}_R_{combo['Rear Motor']}"
            design_instance_id = create_design_instance(ref_project_id, title=title)
            created_designs.append(
                {"Project Name": title, "Design Instance Id": design_instance_id}
            )
            concept = copy_concept(base_concept_id, design_instance_id)
            print(f"ID of the cloned concept: {concept['id']}")
            params = {"design_instance_id": design_instance_id}
            components = get_component_id_map(client, design_instance_id)
            updated_architecture = update_architecture(components, combo)

            # Update the architecture

            created_arch = app.post(client, "/architectures", data=updated_architecture)
            print(f"Created architecture: {created_arch}\n")
            concept["architecture_id"] = created_arch["id"]
            # Create and submit a job
            job_info = app.create_submit_job(
                client,
                concept,
                account_id,
                hpc_id,
                job_name=f"cli_job: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}",
            )
            print(f"Submitted job for combination {combo}: {job_info}")
        except Exception as err:
            # This is bad practice as the above code could raise a more serious error.
            # But this way it shouldn't break the whole loop if one job fails.
            print(f"Failed to submit job for combination {combo}: {err}")
            continue
    all_results = pd.DataFrame(created_designs)
    all_results.to_excel("created_designs.xlsx")
