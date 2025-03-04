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
Bulk Job Submit.
================

Example Script to bulk submit jobs to the ConceptEV API.
This example copies the template into a project and runs a number of jobs with different
combinations of components.
The combinations of components are specified in a CSV file format.
"""

# %%
# Perform Required imports
# ------------------------

import datetime

import pandas as pd

from ansys.conceptev.core import app
from ansys.conceptev.core.exceptions import ResponseError

# %%
# Set up inputs.
# ------------------------
# Change the following variables to match your data.
# The current filename for combinations can be used as an example.
# The current base_concept_id is a template concept that will be copied.
# Component Order is dictionary that maps the column names in the combinations file to the
# component names in the API.
filename = "resources/combinations.csv"  # See example file for format.
base_concept_id = "2465235f-ad2e-4923-9125-e2e69ccf5816"  # Truck template.
component_order = {
    "front_transmission_id": "Front Transmission",
    "front_motor_id": "Front Motor",
    "front_inverter_id": "Front Inverter",
    "rear_transmission_id": "Rear Transmission",
    "rear_motor_id": "Rear Motor",
    "rear_inverter_id": "Rear Inverter",
    "battery_id": "Battery",
    "front_clutch_id": "Front Clutch",
    "rear_clutch_id": "Rear Clutch",
}


def update_architecture(components, combo, base_architecture):
    # Update Architecture to match the new combinations.
    arch = {key: components[combo[value]] for key, value in component_order.items()}
    arch["number_of_front_wheels"] = base_architecture["number_of_front_wheels"]
    arch["number_of_front_motors"] = base_architecture["number_of_front_motors"]
    arch["number_of_rear_wheels"] = base_architecture["number_of_rear_wheels"]
    arch["number_of_rear_motors"] = base_architecture["number_of_rear_motors"]
    arch["wheelbase"] = base_architecture["wheelbase"]
    return arch


# %%
# Create a client and create a new project from template.
# -------------------------------------------------------
# Authenticate and get a token
# Create an API client.
# Get the account ID and HPC ID.
# Copy the template into a new project.
# Add a clutch to the concept.
# Get the component IDs for the new concept.
# Get the architecture for the new concept.

msal_app = app.auth.create_msal_app()
token = app.auth.get_ansyId_token(msal_app)
# Use API client for the Ansys ConceptEV service
with app.get_http_client(token) as client:
    client.timeout = 200  # Extend timeout for uploading files.
    accounts = app.get_account_ids(token)
    account_id = accounts["conceptev_saas@ansys.com"]
    hpc_id = app.get_default_hpc(token, account_id)

    project = app.create_new_project(
        client, account_id, hpc_id, f"New Project {datetime.datetime.now()}"
    )
    project_id = project["projectId"]
    design_instance_id = app.create_design_instance(
        project_id, f"New Concept {datetime.datetime.now()}", token
    )
    app.copy_concept(base_concept_id, design_instance_id, client)
    base_concept_id = design_instance_id
    app.post(
        client,
        "/components",
        data={
            "item_type": "component",
            "name": "Disconnect Clutch",
            "mass": 0,
            "moment_of_inertia": 0,
            "cost": 0,
            "component_type": "ClutchInput",
            "efficiency": "95",
            "switch_energy": "10",
            "engaged_power": 0,
        },
        params={"design_instance_id": base_concept_id},
    )
    base_components = app.get_component_id_map(client, base_concept_id)

    base_concept = app.get(client, f"/concepts/{base_concept_id}")
    base_architecture = app.get(
        client,
        f"/architectures/{base_concept['architecture_id']}",
        params={"design_instance_id": base_concept_id},
    )

# %%
# Read combinations from a csv file and check they match the combinations file.
# -----------------------------------------------------------------------------
# Read combinations from a csv file.
# Get the component types from the component_order dictionary.
# Turn them into set.
# Check that the component types are in the combinations file.
# Get the component names from the combinations.
# Check the component names are in the base components.

combinations = pd.read_csv(filename, na_filter=False)
combinations = combinations.to_dict("records")

# Check the component types are in the header of the combinations file.
component_types = set(component_order.values())
component_types_from_combo_header = set(combinations[0].keys())
assert component_types <= component_types_from_combo_header, component_types.difference(
    component_types_from_combo_header
)
# Check the component names in the combinations file are in the base components.
component_names_from_combo = set([value for combo in combinations for value in combo.values()])
component_names_from_base = set(base_components.keys())
assert (
    component_names_from_combo <= component_names_from_base
), component_names_from_combo.difference(component_names_from_base)

# %%
# Submit jobs for each combination.
# ---------------------------------
# Create a new design instance with title.
# Create an output list to store the created designs.
# Copy the base Concept into that new design instance.
# Get the component IDs for the new design instance as they change when copied.
# Change the base concept to use the new components.
# Update the architecture on the server.
# Update the local concept instance with the new architecture id.
# Create and submit a job using the new concept (with the new architecture).

with app.get_http_client(token) as client:
    created_designs = []
    # Submit jobs for each combination
    for combo in combinations:
        try:
            # Create a new design instance with title.
            title = f"F_{combo['Front Motor']}_R_{combo['Rear Motor']} {datetime.datetime.now()}"
            design_instance_id = app.create_design_instance(project_id, title=title, token=token)

            # Copy base Concept into that new design instance.
            concept = app.copy_concept(base_concept_id, design_instance_id, client)
            print(f"ID of the cloned concept: {concept['id']}")
            # Save that in output list.
            created_designs.append(
                {
                    "Project Name": title,
                    "Design Instance Id": design_instance_id,
                    "Concept_ID": concept["id"],
                },
            )
            # Get the component IDs for the new design instance as they change when copied.
            params = {"design_instance_id": design_instance_id}
            components = app.get_component_id_map(client, design_instance_id)
            # Change the base concept to use the new components.
            updated_architecture = update_architecture(components, combo, base_architecture)
            # Update the architecture on the server.
            created_arch = app.post(client, "/architectures", data=updated_architecture)
            print(f"Created architecture: {created_arch}\n")

            # Update the local concept instance with the new architecture id.
            concept["architecture_id"] = created_arch["id"]

            # Create and submit a job using the new concept (with the new architecture)
            job_info = app.create_submit_job(
                client,
                concept,
                account_id,
                hpc_id,
                job_name=f"cli_job: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}",
            )
            print(f"Submitted job for combination {combo}: {job_info}")
        except ResponseError as err:
            print(f"Failed to submit job for combination {combo}: {err}")
            continue  # If one job fails to submit keep trying the other jobs.
# %%
# Save the list of created designs to a file.
# -------------------------------------------
# Create a pandas dataframe.
# Export to Excel.
all_results = pd.DataFrame(created_designs)
all_results.to_excel("created_designs.xlsx")

# %%
# Delete the extra project on the server.
# ---------------------------------------
# Delete the project on the server.
#
# .. warning::
#    This will delete the project and all its contents.
#    Only needed for keep test environment clean.

with app.get_http_client(token) as client:
    for concept in created_designs:
        client.params = client.params.set("design_instance_id", concept["Design Instance Id"])
        app.delete(client, "concepts", id=concept["Concept_ID"])
    app.delete_project(project_id, token)
    print(f"Deleted project {project_id}")
