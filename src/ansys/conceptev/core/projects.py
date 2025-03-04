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

"""Projects/OCM Specific functionality."""

import datetime

import httpx

from ansys.conceptev.core.exceptions import (
    AccountsError,
    DesignError,
    ProductIdsError,
    ProjectError,
    UserDetailsError,
)
from ansys.conceptev.core.settings import settings

OCM_URL = settings.ocm_url
ACCOUNT_NAME = settings.account_name


def get_product_id(token: str) -> str:
    """Get the product ID."""
    products = httpx.get(OCM_URL + "/product/list", headers={"Authorization": token})
    if products.status_code != 200:
        raise ProductIdsError(f"Failed to get product id.")

    product_id = [
        product["productId"] for product in products.json() if product["productName"] == "CONCEPTEV"
    ][0]
    return product_id


def get_user_id(token):
    """Get the user ID."""
    user_details = httpx.post(OCM_URL + "/user/details", headers={"Authorization": token})
    if user_details.status_code not in (200, 204):
        raise UserDetailsError(f"Failed to get a user details on OCM {user_details}.")
    user_id = user_details.json()["userId"]
    return user_id


def get_account_ids(token: str) -> dict:
    """Get account IDs."""
    response = httpx.post(url=OCM_URL + "/account/list", headers={"authorization": token})
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
    response = httpx.post(
        url=OCM_URL + "/account/hpc/default",
        json={"accountId": account_id},
        headers={"authorization": token},
    )
    if response.status_code != 200:
        raise AccountsError(f"Failed to get accounts {response}.")
    return response.json()["hpcId"]


def get_project_ids(name: str, account_id: str, token: str) -> dict:
    """Get projects."""
    response = httpx.post(
        url=OCM_URL + "/project/list/page",
        json={"accountId": account_id, "filterByName": name, "pageNumber": 0, "pageSize": 1000},
        headers={"Authorization": token},
    )
    if response.status_code != 200:
        raise ProjectError(f"Failed to get projects {response}.")

    projects = response.json()["projects"]
    return {project["projectTitle"]: project["projectId"] for project in projects}


def create_new_project(
    client: httpx.Client,
    account_id: str,
    hpc_id: str,
    title: str,
    project_goal: str = "Created from the CLI",
) -> dict:
    """Create a project."""
    token = client.headers["Authorization"]
    project_data = {
        "accountId": account_id,
        "hpcId": hpc_id,
        "projectTitle": title,
        "projectGoal": project_goal,
    }
    created_project = httpx.post(
        OCM_URL + "/project/create", headers={"Authorization": token}, json=project_data
    )
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
    created_design = httpx.post(
        OCM_URL + "/design/create", headers={"Authorization": token}, json=design_data
    )

    if created_design.status_code not in (200, 204):
        raise DesignError(f"Failed to create a design on OCM {created_design.content}.")
    return created_design.json()
