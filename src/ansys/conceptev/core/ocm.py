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

"""Projects/OCM Specific functionality."""

from collections import defaultdict
import datetime
import json
import re

import httpx

import ansys.conceptev.core.auth as auth
from ansys.conceptev.core.exceptions import (
    AccountsError,
    DesignError,
    ProductIdsError,
    ProjectError,
    ResponseError,
    UserDetailsError,
)
from ansys.conceptev.core.progress import generate_ssl_context
from ansys.conceptev.core.responses import process_response
from ansys.conceptev.core.settings import settings

OCM_URL = settings.ocm_url
ACCOUNT_NAME = settings.account_name


def create_ocm_client(token) -> httpx.Client:
    """Create an OCM client."""
    client = httpx.Client(
        base_url=OCM_URL,
        verify=generate_ssl_context(),
        headers={
            "Authorization": token,
        },
    )
    return client


def get_product_id(token: str) -> str:
    """Get the product ID."""
    products = create_ocm_client(token).get("/product/list")
    if products.status_code != 200:
        raise ProductIdsError(f"Failed to get product id.")
    product_id = [
        product["productId"] for product in products.json() if product["productName"] == "CONCEPTEV"
    ][0]
    return product_id


def get_user_id(token):
    """Get the user ID."""
    user_details = create_ocm_client(token).post("/user/details")
    if user_details.status_code not in (200, 204):
        raise UserDetailsError(f"Failed to get a user details on OCM {user_details}.")
    user_id = user_details.json()["userId"]
    return user_id


def get_account_ids(token: str) -> dict:
    """Get account IDs."""
    response = create_ocm_client(token).post("/account/list")
    if response.status_code != 200:
        raise AccountsError(f"Failed to get accounts {response}.")
    accounts = {
        account["account"]["accountName"]: account["account"]["accountId"]
        for account in response.json()
    }
    return accounts


def get_account_id(token: str) -> str:
    """Get the account ID from OCM using name from config file."""
    accounts = get_account_ids(token)
    account_id = accounts[ACCOUNT_NAME]
    return account_id


def get_default_hpc(token: str, account_id: str) -> dict:
    """Get the default HPC ID."""
    response = create_ocm_client(token).post(
        "/account/hpc/default",
        json={"accountId": account_id},
    )
    if response.status_code != 200:
        raise AccountsError(f"Failed to get accounts {response}.")
    return response.json()["hpcId"]


def create_new_project(
    client: httpx.Client,
    account_id: str,
    hpc_id: str,
    title: str,
    project_goal: str = "Created from the CLI",
) -> dict:
    """Create a project."""
    token = auth.get_token(client)
    project_data = {
        "accountId": account_id,
        "hpcId": hpc_id,
        "projectTitle": title,
        "projectGoal": project_goal,
    }
    created_project = create_ocm_client(token).post("/project/create", json=project_data)
    if created_project.status_code != 200 and created_project.status_code != 204:
        raise ProjectError(f"Failed to create a project {created_project}.")

    return created_project.json()


def create_new_design(
    client: httpx.AsyncClient, project_id: str, product_id: str = None, title: str = None
) -> dict:
    """Create a new design on OCM."""
    if title is None:
        title = f"CLI concept {datetime.datetime.now()}"

    token = client.headers["Authorization"]
    if product_id is None:
        product_id = get_product_id(token)

    design_data = {
        "projectId": project_id,
        "productId": product_id,
        "designTitle": title,
    }
    created_design = create_ocm_client(token).post("/design/create", json=design_data)

    if created_design.status_code not in (200, 204):
        raise DesignError(f"Failed to create a design on OCM {created_design.content}.")
    return created_design.json()


def get_or_create_project(client: httpx.Client, account_id: str, hpc_id: str, title: str) -> dict:
    """Get or create a project."""
    stored_errors = []
    options = [title, re.escape(title), title.split(maxsplit=1)[0]]
    for search_string in options:
        try:
            projects = get_project_ids(search_string, account_id, client.headers["Authorization"])
            project_id = projects[title][0]
            return project_id
        except (ProjectError, KeyError, IndexError) as err:
            stored_errors.append(err)

    project = create_new_project(client, account_id, hpc_id, title)
    project_id = project["projectId"]

    return project_id


def create_design_instance(project_id, title, token, product_id=None, return_design_id=False):
    """Create a design instance on OCM."""
    if product_id is None:
        product_id = get_product_id(token)

    design_data = {
        "projectId": project_id,
        "productId": product_id,
        "designTitle": title,
    }
    created_design = create_ocm_client(token).post("/design/create", json=design_data)

    if created_design.status_code not in (200, 204):
        raise Exception(f"Failed to create a design on OCM {created_design.content}.")

    design_instance_id = created_design.json()["designInstanceList"][0]["designInstanceId"]
    if return_design_id:
        return design_instance_id, created_design.json()["designId"]
    return design_instance_id


def get_job_file(token, job_id, filename, simulation_id=None, encrypted=False):
    """Get the job file from the OnScale Cloud Manager."""
    encrypted_part = "decrypted/" if encrypted else ""
    if simulation_id is not None:
        path = f"/job/files/{encrypted_part}{job_id}/{simulation_id}/{filename}"
    else:
        path = f"/job/files/{encrypted_part}{job_id}/{filename}"
    response = create_ocm_client(token).get(
        url=path, headers={"accept": "application/octet-stream"}
    )
    if response.status_code != 200:
        raise ResponseError(f"Failed to get file {response}.")

    return json.loads(response.content)


def get_job_info(token, job_id):
    """Get the job info from the OnScale Cloud Manager."""
    response = create_ocm_client(token).post(url=f"/job/load", json={"jobId": job_id})
    response = process_response(response)
    job_info = {
        "job_id": job_id,
        "simulation_id": response["simulations"][0]["simulationId"],
        "job_name": response["jobName"],
        "docker_tag": response["dockerTag"],
    }
    return job_info


def get_design_of_job(token, job_id):
    """Get the job info from the OnScale Cloud Manager."""
    response = create_ocm_client(token).post(url="/job/load", json={"jobId": job_id})
    response = process_response(response)
    return response["designInstanceId"]


def get_design_title(token, design_instance_id):
    """Get the design Title from the OnScale Cloud Manager."""
    response = create_ocm_client(token).post(
        url="/design/instance/load",
        json={"designInstanceId": design_instance_id},
    )
    response = process_response(response)
    design = create_ocm_client(token).post(
        url="/design/load",
        json={"designId": response["designId"]},
    )
    design = process_response(design)
    return design["designTitle"]


def get_status(job_info: dict, token: str) -> str:
    """Get the status of the job."""
    response = create_ocm_client(token).post(
        url="/job/load",
        json={"jobId": job_info["job_id"]},
    )
    processed_response = process_response(response)
    if "finalStatus" in processed_response and processed_response["finalStatus"] is not None:
        status = processed_response["finalStatus"].upper()
    elif "lastStatus" in processed_response and processed_response["lastStatus"] is not None:
        status = processed_response["lastStatus"].upper()
    else:
        raise ResponseError(f"Failed to get job status {processed_response}.")
    return status


def get_project_ids(name: str, account_id: str, token: str) -> dict:
    """Get projects."""
    response = create_ocm_client(token).post(
        url="/project/list/page",
        json={"accountId": account_id, "filterByName": name, "pageNumber": 0, "pageSize": 1000},
    )
    processed_response = process_response(response)
    projects = processed_response["projects"]
    project_dict = defaultdict(list)
    for project in projects:
        project_dict[project["projectTitle"]].append(project["projectId"])
    return project_dict


def get_project_id(name: str, account_id: str, token: str) -> str:
    """Get project ID."""
    projects = get_project_ids(name, account_id, token)
    if not projects:
        raise ProjectError(f"Project with name {name} not found.")
    if len(projects) > 1:
        raise ProjectError(f"Multiple projects found with name {name}.")
    return projects[name][0]


def delete_project(project_id, token):
    """Delete a project."""
    ocm_delete_init = create_ocm_client(token).request(
        method="DELETE",
        url="/project/delete/init",
        json={"projectId": project_id},
        timeout=20,
    )
    ocm_delete_init = process_response(ocm_delete_init)
    ocm_delete = create_ocm_client(token).request(
        method="DELETE",
        url="/project/delete/execute",
        json={"projectId": project_id, "hash": ocm_delete_init["hash"]},
        timeout=20,
    )
    ocm_delete = process_response(ocm_delete)
    return ocm_delete
