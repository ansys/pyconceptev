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

"""Simple API client for the Ansys ConceptEV service."""
import datetime
from typing import Literal

import httpx
from tenacity import retry, retry_if_result, stop_after_delay, wait_random_exponential

from ansys.conceptev.core import auth
from ansys.conceptev.core.auth import get_token
from ansys.conceptev.core.exceptions import DeleteError, ProductAccessError, ResultsError
from ansys.conceptev.core.ocm import (
    create_design_instance,
    create_new_project,
    delete_project,
    get_account_id,
    get_account_ids,
    get_default_hpc,
    get_design_of_job,
    get_design_title,
    get_job_file,
    get_job_info,
    get_or_create_project,
    get_product_id,
    get_project_id,
    get_project_ids,
    get_status,
    get_user_id,
)
from ansys.conceptev.core.progress import check_status, generate_ssl_context, monitor_job_progress
from ansys.conceptev.core.responses import is_gateway_error, process_response
from ansys.conceptev.core.settings import settings

__all__ = [
    get_or_create_project,
    create_new_project,
    create_design_instance,
    get_product_id,
    get_user_id,
    get_account_id,
    get_account_ids,
    get_default_hpc,
    get_job_file,
    get_job_info,
    get_design_of_job,
    get_design_title,
    get_status,
    get_project_ids,
    get_project_id,
    delete_project,
    get_token,
]

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

JOB_TIMEOUT = settings.job_timeout
OCM_URL = settings.ocm_url
BASE_URL = settings.conceptev_url
ACCOUNT_NAME = settings.account_name
app = auth.create_msal_app()


def get_http_client(
    token: str | None = None,
    design_instance_id: str | None = None,
    cache_filepath: str = "token_cache.bin",
) -> httpx.Client:
    """Get an HTTP client.

    The HTTP client creates and maintains the connection, which is more performant than
    re-creating this connection for each call.
    """
    httpx_auth = auth.AnsysIDAuth(cache_filepath=cache_filepath) if token is None else None
    params = {"design_instance_id": design_instance_id} if design_instance_id else None
    header = {"Authorization": token} if token else None

    client = httpx.Client(
        headers=header,
        auth=httpx_auth,
        params=params,
        base_url=BASE_URL,
        verify=generate_ssl_context(),
    )
    client.send = retry(
        retry=retry_if_result(is_gateway_error),
        wait=wait_random_exponential(multiplier=1, max=60),
        stop=stop_after_delay(10),
    )(client.send)
    return client


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
            raise ProductAccessError(f"Account ID is required for {router}.")
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
        raise DeleteError(f"Failed to delete from {router} with ID:{id}.")


def put(client: httpx.Client, router: Router, id: str, data: dict) -> dict:
    """Put/update from the client at the specific route.

    An HTTP verb that performs the ``PUT`` request and adds the route to the base client.
    """
    path = "/".join([router, id])
    response = client.put(url=path, json=data)
    return process_response(response)


def create_new_concept(
    client: httpx.Client,
    project_id: str,
    product_id: str | None = None,
    title: str | None = None,
) -> dict:
    """Create a concept within an existing project."""
    if title is None:
        title = f"CLI concept {datetime.datetime.now()}"

    token = auth.get_token(client)
    if product_id is None:
        product_id = get_product_id(token)

    design_instance_id, design_id = create_design_instance(
        project_id, title, token, product_id, return_design_id=True
    )

    user_id = get_user_id(token)

    concept_data = {
        "capabilities_ids": [],
        "components_ids": [],
        "configurations_ids": [],
        "design_id": design_id,
        "design_instance_id": design_instance_id,
        "drive_cycles_ids": [],
        "jobs_ids": [],
        "name": "Branch 1",
        "project_id": project_id,
        "requirements_ids": [],
        "user_id": user_id,
    }

    query = {
        "design_instance_id": design_instance_id,
    }

    created_concept = post(client, "/concepts", data=concept_data, params=query)
    return created_concept


def get_concept_ids(client: httpx.Client) -> dict:
    """Get concept IDs."""
    concepts = get(client, "/concepts")
    return {concept["name"]: concept["id"] for concept in concepts}


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
    token = auth.get_token(client)
    user_id = get_user_id(token)
    initial_status = get_status(job_info, token)
    if check_status(initial_status):  # Job already completed
        return get_results(client, job_info, calculate_units, filtered)
    else:  # Job is still running
        if msal_app is None:
            msal_app = auth.create_msal_app()
        monitor_job_progress(job_id, user_id, token, msal_app, timeout)  # Wait for completion

        token = auth.get_ansyId_token(msal_app)
        client.headers["Authorization"] = token  # Update the token
        return get_results(client, job_info, calculate_units, filtered)


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


def copy_concept(base_concept_id, design_instance_id, client):
    """Copy the reference concept to the new design instance."""
    copy = {
        "old_design_instance_id": base_concept_id,
        "new_design_instance_id": design_instance_id,
        "copy_jobs": False,
    }
    # Clone the base concept
    params = {"design_instance_id": design_instance_id, "populated": False}
    client.params = params
    concept = post(client, "/concepts:copy", data=copy)
    return concept


def create_submit_job(
    client,
    concept: dict,
    account_id: str,
    hpc_id: str,
    job_name: str | None = None,
    docker_tag: str = "default",
    extra_memory: bool = False,
) -> dict:
    """Create and then submit a job."""
    if job_name is None:
        job_name = f"cli_job: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}"
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
        "docker_tag": docker_tag,
        "extra_memory": extra_memory,
    }
    job_info = post(client, "/jobs:start", data=job_start, account_id=account_id)
    return job_info


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
    if response.status_code == 502 or response.status_code == 504:
        raise ResultsError(
            f"Request timed out {response}. "
            f"Please try using either calculate_units=False or filtered=True."
        )
    return process_response(response)


def get_component_id_map(client, design_instance_id):
    """Get a map of component name to component id."""
    ###TODO move to results file so its self contained.
    components = client.get(f"/concepts/{design_instance_id}/components")
    components = process_response(components)
    components.append({"name": "N/A", "id": None})
    return {component["name"]: component["id"] for component in components}
