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

"""Simple API client for the Ansys ConceptEV service."""

import datetime
from json import JSONDecodeError
import os
from typing import Literal

import dotenv
import httpx

from ansys.conceptev.core import auth
from ansys.conceptev.core.progress import check_status, monitor_job_progress

dotenv.load_dotenv()

Router = Literal[
    "/architectures",
    "/components",
    "/components:from_file",  # extra
    "/components:upload",
    "/components:upload_file",
    "/components:calculate_loss_map",
    "/configurations",
    "/configurations:calculate_forces",
    "/requirements",
    "/requirements:calculate_examples",
    "/jobs",
    "/jobs:start",
    "/jobs:status",
    "/jobs:result",
    "/concepts",
    "/drive_cycles",
    "/drive_cycles:from_file",
    "/drive_cycles:upload_file",
    "/health",
    "/utilities:data_format_version",
]

PRODUCT_ACCESS_ROUTES = [
    "/components:upload_file",
    "/components:from_file",  # extra
    "/drive_cycles:upload_file",
    "/jobs",
    "/jobs:start",
]

JOB_TIMEOUT = auth.config["JOB_TIMEOUT"]
app = auth.create_msal_app()


def get_token() -> str:
    """Get token from OCM."""
    username = os.environ["CONCEPTEV_USERNAME"]
    password = os.environ["CONCEPTEV_PASSWORD"]
    ocm_url = auth.config["OCM_URL"]
    response = httpx.post(
        url=ocm_url + "/auth/login/", json={"emailAddress": username, "password": password}
    )
    if response.status_code != 200:
        raise Exception(f"Failed to get token {response.content}")
    return response.json()["accessToken"]


def get_http_client(token: str, design_instance_id: str | None = None) -> httpx.Client:
    """Get an HTTP client.

    The HTTP client creates and maintains the connection, which is more performant than
    re-creating this connection for each call.
    """
    base_url = auth.config["CONCEPTEV_URL"]
    params = None
    if design_instance_id:
        params = {"design_instance_id": design_instance_id}
    return httpx.Client(headers={"Authorization": token}, params=params, base_url=base_url)


def process_response(response) -> dict:
    """Process a response.

    Check the value returned from the API and raise an error if the process is not successful.
    """
    if response.status_code == 200 or response.status_code == 201:  # Success
        try:
            return response.json()
        except JSONDecodeError:
            return response.content
    raise Exception(f"Response Failed:{response.content}")


def get(
    client: httpx.Client, router: Router, id: str | None = None, params: dict | None = None
) -> dict:
    """Send a GET request to the base client.

    This HTTP verb performs the ``GET`` request and adds the route to the base client.
    """
    if id:
        path = "/".join([router, id])
    else:
        path = router
    response = client.get(url=path, params=params)
    return process_response(response)


def post(
    client: httpx.Client,
    router: Router,
    data: dict,
    params: dict = {},
    account_id: str | None = None,
) -> dict:
    """Send a POST request to the base client.

    This HTTP verb performs the ``POST`` request and adds the route to the base client.
    """
    params = check_product_access(router, account_id, params)

    response = client.post(url=router, json=data, params=params)
    return process_response(response)


def check_product_access(router: Router, account_id: str | None, params: dict) -> dict:
    """Check account_id is there for product access."""
    if router in PRODUCT_ACCESS_ROUTES:
        if not account_id:
            raise Exception(f"Account ID is required for {router}.")
        params = params | {"account_id": account_id}
    return params


def delete(client: httpx.Client, router: Router, id: str, account_id: str | None = None) -> dict:
    """Send a DELETE request to the base client.

    This HTTP verb performs the ``DELETE`` request and adds the route to the base client.
    """
    params = check_product_access(router, account_id, {})
    path = "/".join([router, id])
    response = client.delete(url=path, params=params)
    if response.status_code != 204:
        raise Exception(f"Failed to delete from {router} with ID:{id}.")


def put(client: httpx.Client, router: Router, id: str, data: dict) -> dict:
    """Put/update from the client at the specific route.

    An HTTP verb that performs the ``PUT`` request and adds the route to the base client.
    """
    path = "/".join([router, id])
    response = client.put(url=path, json=data)
    return process_response(response)


def create_new_project(
    client: httpx.Client,
    account_id: str,
    hpc_id: str,
    title: str,
    project_goal: str = "Created from the CLI",
) -> dict:
    """Create a project."""
    osm_url = auth.config["OCM_URL"]
    token = client.headers["Authorization"]
    project_data = {
        "accountId": account_id,
        "hpcId": hpc_id,
        "projectTitle": title,
        "projectGoal": project_goal,
    }
    created_project = httpx.post(
        osm_url + "/project/create", headers={"Authorization": token}, json=project_data
    )
    if created_project.status_code != 200 and created_project.status_code != 204:
        raise Exception(f"Failed to create a project {created_project}.")

    return created_project.json()


def create_new_concept(
    client: httpx.Client,
    project_id: str,
    title: str = f"CLI concept {datetime.datetime.now()}",
) -> dict:
    """Create a concept within an existing project."""
    osm_url = auth.config["OCM_URL"]
    token = client.headers["Authorization"]
    product_id = get_product_id(token)

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

    user_id = get_user_id(token)

    design_instance_id = created_design.json()["designInstanceList"][0]["designInstanceId"]
    concept_data = {
        "capabilities_ids": [],
        "components_ids": [],
        "configurations_ids": [],
        "design_id": created_design.json()["designId"],
        "design_instance_id": design_instance_id,
        "drive_cycles_ids": [],
        "jobs_ids": [],
        "name": "Branch 1",
        "project_id": project_id,
        "requirements_ids": [],
        "user_id": user_id,
    }

    query = {
        "design_instance_id": created_design.json()["designInstanceList"][0]["designInstanceId"],
    }

    created_concept = post(client, "/concepts", data=concept_data, params=query)
    return created_concept


def get_product_id(token: str) -> str:
    """Get the product ID."""
    osm_url = auth.config["OCM_URL"]
    products = httpx.get(osm_url + "/product/list", headers={"Authorization": token})
    if products.status_code != 200:
        raise Exception(f"Failed to get product id.")

    product_id = [
        product["productId"] for product in products.json() if product["productName"] == "CONCEPTEV"
    ][0]
    return product_id


def get_user_id(token):
    """Get the user ID."""
    osm_url = auth.config["OCM_URL"]
    user_details = httpx.post(osm_url + "/user/details", headers={"Authorization": token})
    if user_details.status_code not in (200, 204):
        raise Exception(f"Failed to get a user details on OCM {user_details}.")
    user_id = user_details.json()["userId"]
    return user_id


def get_concept_ids(client: httpx.Client) -> dict:
    """Get concept IDs."""
    concepts = get(client, "/concepts")
    return {concept["name"]: concept["id"] for concept in concepts}


def get_account_ids(token: str) -> dict:
    """Get account IDs."""
    ocm_url = auth.config["OCM_URL"]
    response = httpx.post(url=ocm_url + "/account/list", headers={"authorization": token})
    if response.status_code != 200:
        raise Exception(f"Failed to get accounts {response}.")
    accounts = {
        account["account"]["accountName"]: account["account"]["accountId"]
        for account in response.json()
    }
    return accounts


def get_default_hpc(token: str, account_id: str) -> dict:
    """Get the default HPC ID."""
    ocm_url = auth.config["OCM_URL"]
    response = httpx.post(
        url=ocm_url + "/account/hpc/default",
        json={"accountId": account_id},
        headers={"authorization": token},
    )
    if response.status_code != 200:
        raise Exception(f"Failed to get accounts {response}.")
    return response.json()["hpcId"]


def create_submit_job(
    client,
    concept: dict,
    account_id: str,
    hpc_id: str,
    job_name: str = "cli_job: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
) -> dict:
    """Create and then submit a job."""
    job_input = {
        "job_name": job_name,
        "requirement_ids": concept["requirements_ids"],
        "architecture_id": concept["architecture_id"],
        "concept_id": concept["id"],
        "design_instance_id": concept["design_instance_id"],
    }
    job, uploaded_file = post(client, "/jobs", data=job_input, account_id=account_id)
    job_start = {
        "job": job,
        "uploaded_file": uploaded_file,
        "account_id": account_id,
        "hpc_id": hpc_id,
    }
    job_info = post(client, "/jobs:start", data=job_start, account_id=account_id)
    return job_info


def read_file(filename: str) -> str:
    """Read a given file."""
    with open(filename, "r+b") as f:
        content = f.read()
    return content


def read_results(
    client,
    job_info: dict,
    calculate_units: bool = True,
    timeout: int = JOB_TIMEOUT,
    filtered: bool = False,
    msal_app: auth.PublicClientApplication | None = None,
) -> dict:
    """Read job results."""
    job_id = job_info["job_id"]
    token = client.headers["Authorization"]
    user_id = get_user_id(token)
    initial_status = get_status(job_info, token)
    if check_status(initial_status):  # Job already completed
        return get_results(client, job_info, calculate_units, filtered)
    else:  # Job is still running
        monitor_job_progress(job_id, user_id, token, timeout)  # Wait for completion
        if msal_app is None:
            msal_app = auth.create_msal_app()
        token = auth.get_ansyId_token(msal_app)
        client.headers["Authorization"] = token  # Update the token
        return get_results(client, job_info, calculate_units, filtered)


def get_results(
    client,
    job_info: dict,
    calculate_units: bool = True,
    filtered: bool = False,
):
    """Get the results."""
    version_number = get(client, "/utilities:data_format_version")
    if filtered:
        filename = f"filtered_output_v{version_number}.json"
    else:
        filename = f"output_file_v{version_number}.json"
    response = client.post(
        url="/jobs:result",
        json=job_info,
        params={
            "results_file_name": filename,
            "calculate_units": calculate_units,
        },
    )
    return process_response(response)


def get_status(job_info: dict, token: str) -> str:
    """Get the status of the job."""
    ocm_url = auth.config["OCM_URL"]
    response = httpx.post(
        url=ocm_url + "/job/load",
        json={"jobId": job_info["job_id"]},
        headers={"Authorization": token},
    )
    processed_response = process_response(response)
    initial_status = processed_response["jobStatus"][-1]["jobStatus"]
    return initial_status


def post_component_file(client: httpx.Client, filename: str, component_file_type: str) -> dict:
    """Send a POST request to the base client with a file.

    An HTTP verb that performs the ``POST`` request, adds the route to the base client,
    and then adds the file as a multipart form request.
    """
    path = "/components:upload"
    file_contents = read_file(filename)
    response = client.post(
        url=path, files={"file": file_contents}, params={"component_file_type": component_file_type}
    )
    return process_response(response)


def get_concept(client: httpx.Client, design_instance_id: str) -> dict:
    """Get the main parts of a concept."""
    concept = get(
        client, "/concepts", id=design_instance_id, params={"populated": False}
    )  # populated True is unsupported at this time.
    concept["configurations"] = get(client, f"/concepts/{design_instance_id}/configurations")
    concept["components"] = get(client, f"/concepts/{design_instance_id}/components")

    concept["requirements"] = get(client, f"/concepts/{design_instance_id}/requirements")

    concept["architecture"] = get(client, f"/concepts/{design_instance_id}/architecture")
    return concept


if __name__ == "__main__":
    token = get_token()

    with get_http_client(token) as client:  # Create a client to talk to the API
        health = get(client, "/health")  # Check that the API is healthy
        print(health)
