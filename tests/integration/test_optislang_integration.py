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

import re

import httpx
import jwt

# Optislang Integration Test
# A poor mans integration test for the optislang integration.
# Looks at conceptev/utils/api_helper.py to see pyconceptev usage within ConceptEV integration.
import pytest

from ansys.conceptev.core import app, auth, exceptions


@pytest.fixture
def msal_app():
    """Fixture to create a MSAL PublicClientApplication instance."""
    return auth.create_msal_app()


@pytest.fixture
def token(msal_app):
    """Fixture to get a valid AnsysID token."""
    token = auth.get_ansyId_token(msal_app)
    return token


@pytest.fixture
def client(token):
    """Fixture to provide a client for testing."""
    with app.get_http_client(token) as client:
        yield client


@pytest.fixture
def design_instance_id():
    """Fixture to provide a design instance ID for testing."""
    return "8cdea42d-fb8a-4499-a6f9-a188f2454afa"


@pytest.fixture
def client_with_design_instance(design_instance_id, token):
    """Fixture to provide a client with a design instance ID for testing."""
    with app.get_http_client(token, design_instance_id) as client:
        yield client


@pytest.fixture
def accounts(token):
    """Fixture to get accounts."""
    accounts = app.get_account_ids(token)
    return accounts


@pytest.fixture
def concept_data(client_with_design_instance, design_instance_id):
    """Fixture to get concept data."""
    concept_data = app.get_concept(client_with_design_instance, design_instance_id)
    return concept_data


@pytest.fixture
def account_id(accounts):
    """Fixture to provide an account ID for testing."""
    return accounts[auth.settings.account_name]


@pytest.fixture
def hpc_id(token, account_id):
    """Fixture to get the HPC ID."""
    hpc_id = app.get_default_hpc(token, account_id)
    return hpc_id


@pytest.fixture
def job_info(client_with_design_instance, concept_data, account_id, hpc_id):
    """Submit a job to the HPC."""
    job_info = app.create_submit_job(
        client_with_design_instance,
        concept_data,
        account_id,
        hpc_id,
    )
    return job_info


@pytest.fixture
def read_results(client_with_design_instance, job_info):
    """Read results from the job."""
    read_results = app.read_results(
        client_with_design_instance,
        job_info,
        calculate_units=False,
        filtered=True,
    )
    return read_results


@pytest.fixture
def console_log(job_info, client_with_design_instance):
    console_log = app.post(client_with_design_instance, "/jobs:error_file", data=job_info)
    return console_log


@pytest.fixture
def project_name():
    """Project name fixture."""
    return "Integration Test from pyconceptev"


@pytest.fixture
def created_project(client, account_id, hpc_id, token, project_name):

    created_project = app.create_new_project(client, account_id, hpc_id, f"{project_name}")
    yield created_project
    app.delete_project(created_project["projectId"], token)


@pytest.fixture
def project_id(created_project):
    """Fixture to provide a project ID for testing."""
    return created_project["projectId"]


@pytest.fixture
def created_concept(client, project_id):
    concept_data = app.create_new_concept(
        client,
        project_id,
        title="ConceptEV Integration Test",
    )
    return concept_data


@pytest.fixture
def account_ids(token):
    """Fixture to get accounts."""
    account_ids = app.get_account_ids(token)
    return account_ids


@pytest.fixture
def project_ids(project_name, created_project, account_id, token):
    """Fixture to get project IDs."""
    project_ids = app.get_project_ids(re.escape(project_name), account_id, token)
    return project_ids


def test_exceptions():
    """Example Exception Usage in api_helper"""
    try:
        raise exceptions.ResponseError("This is a test error")
    except exceptions.ResponseError as e:
        assert e.args[0].lower()


def test_msal_app(msal_app):
    """Test that the MSAL PublicClientApplication is created."""
    assert isinstance(msal_app, auth.PublicClientApplication)
    assert msal_app.client_id == auth.client_id
    assert msal_app.authority.authorization_endpoint == auth.authority + "/oauth2/v2.0/authorize"


def test_auth_app(token):
    """Test that the optislang integration works."""
    assert isinstance(token, str)
    claims = jwt.decode(token, options={"verify_signature": False})
    # Step 1: Fetch JWKS
    jwks = httpx.get(auth.settings.authority + "/discovery/v2.0/keys").json()

    # Step 2: Get headers from token to find correct kid
    unverified_header = jwt.get_unverified_header(token)
    kid = unverified_header["kid"]
    key = next(k for k in jwks["keys"] if k["kid"] == kid)
    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
    algorithm = unverified_header["alg"]
    jwt.decode(token, public_key, verify=True, algorithms=algorithm, options={"verify_aud": False})


def test_client(client, token):
    """Test that the client can make a request."""
    assert str(client.base_url).strip("/") == auth.settings.conceptev_url
    assert client.headers["Authorization"] == f"{token}"


def test_client_design_instance(client_with_design_instance, token, design_instance_id):
    """Test that the client can make a request with a design instance."""
    assert str(client_with_design_instance.base_url).strip("/") == auth.settings.conceptev_url
    assert client_with_design_instance.headers["Authorization"] == f"{token}"
    assert client_with_design_instance.params["design_instance_id"] == design_instance_id
    # Additional checks can be added here for specific endpoints or data


def test_health(client):
    """Test the health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["name"] == "ConceptEV"


def test_authorised(client):
    """Test the health endpoint."""
    response = client.get("/authenticated_user")
    assert response.status_code == 200


def test_get_concept(client, client_with_design_instance, design_instance_id, concept_data):
    """Test getting a concept and getting ids."""
    concept = app.get(client, "/concepts", id=design_instance_id, params={"populated": False})
    concept["configurations"] = app.get(
        client_with_design_instance, f"/concepts/{design_instance_id}/configurations"
    )
    concept["components"] = app.get(
        client_with_design_instance, f"/concepts/{design_instance_id}/components"
    )
    concept["requirements"] = app.get(
        client_with_design_instance, f"/concepts/{design_instance_id}/requirements"
    )
    arch_id = concept["architecture_id"]
    concept["architecture"] = app.get(
        client_with_design_instance,
        f"/architectures/{arch_id}",
        params={"design_instance_id": design_instance_id},
    )
    assert concept == concept_data


def test_accounts(accounts, token):
    """Test accounts endpoint."""
    assert isinstance(accounts, dict)
    assert auth.settings.account_name in accounts


def test_hpc_endpoint(hpc_id):

    assert isinstance(hpc_id, str)
    assert len(hpc_id) > 0, "HPC ID should not be empty"


def test_submit_job(job_info):
    assert isinstance(job_info, dict)
    assert "job_id" in job_info
    return job_info


def test_read_results(read_results):
    """Test reading results from the job."""
    assert isinstance(read_results, list)
    assert read_results[0]["feasible"] == True
    assert len(read_results) > 0, "Results should not be empty"


def test_console_log(read_results, console_log):
    """Test reading the console log."""
    assert isinstance(console_log, str)
    assert len(console_log) > 0, "Console log should not be empty"


def test_create_project(created_project):
    """Test creating a project."""
    assert isinstance(created_project, dict)
    assert "projectId" in created_project
    assert created_project["projectTitle"] == "Integration Test from pyconceptev"


def test_created_concept(created_concept, project_id):
    """Test creating a concept."""
    assert isinstance(created_concept, dict)
    assert created_concept["project_id"] == project_id
    assert "design_instance_id" in created_concept


def test_get_accounts(account_ids, account_id):
    """Test getting accounts."""
    assert isinstance(account_ids, dict)
    assert auth.settings.account_name in account_ids
    assert account_id in account_ids.values()


def test_project_ids(project_ids, project_id, project_name):
    """Test project ids"""
    assert isinstance(project_ids, dict)
    assert project_name in project_ids
    assert isinstance(project_ids[project_name], list)
    assert project_id in project_ids[project_name]


#     data_types ?????
#     posted_data = app.post(client, f"/{data_type}", data=data)

#     created_component = app.post_component_file(client, str(filepath), component_type)
