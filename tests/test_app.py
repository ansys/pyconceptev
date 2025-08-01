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
import pytest
from pytest_httpx import HTTPXMock

from ansys.conceptev.core import app
from ansys.conceptev.core.auth import AnsysIDAuth
from ansys.conceptev.core.exceptions import ResponseError
from ansys.conceptev.core.progress import (
    STATUS_COMPLETE,
    STATUS_ERROR,
    STATUS_FINISHED,
    check_status,
)
from ansys.conceptev.core.settings import settings

conceptev_url = settings.conceptev_url
ocm_url = settings.ocm_url


@pytest.fixture
def client():
    fake_token = "value1"
    design_instance_id = "123"
    client = app.get_http_client(fake_token, design_instance_id=design_instance_id)
    return client


def test_get_http_client():
    fake_token = "value1"
    design_instance_id = "123"
    client = app.get_http_client(fake_token, design_instance_id=design_instance_id)
    assert isinstance(client, httpx.Client)
    assert client.headers["authorization"] == fake_token
    assert str(client.base_url).strip("/") == conceptev_url.strip("/")
    assert client.params["design_instance_id"] == design_instance_id


def test_get_http_client_auth():
    design_instance_id = "123"
    client = app.get_http_client(design_instance_id=design_instance_id)
    assert isinstance(client, httpx.Client)
    assert isinstance(client.auth, AnsysIDAuth)
    assert str(client.base_url).strip("/") == conceptev_url.strip("/")
    assert client.params["design_instance_id"] == design_instance_id


def test_process_response():
    fake_response = httpx.Response(status_code=200, content='{"hello":"again"}')
    content = app.process_response(fake_response)
    assert content == fake_response.json()
    fake_str_response = httpx.Response(status_code=200, content="hello")
    content = app.process_response(fake_str_response)
    assert content == fake_str_response.content
    fake_failure = httpx.Response(status_code=400, content='{"hello":"again"}')
    with pytest.raises(Exception) as e:
        content = app.process_response(fake_failure)
    assert e.value.args[0].startswith("Response Failed:")


def test_get(httpx_mock: HTTPXMock, client: httpx.Client):
    example_results = [{"name": "aero_mock_response"}, {"name": "aero_mock_response2"}]
    httpx_mock.add_response(
        url=f"{conceptev_url}/configurations?design_instance_id=123",
        method="get",
        json=example_results,
    )

    results = app.get(client, "/configurations")
    assert results == example_results


def test_post(httpx_mock: HTTPXMock, client: httpx.Client):
    example_aero = {"name": "aero_mock_response"}
    httpx_mock.add_response(
        url=f"{conceptev_url}/configurations?design_instance_id=123",
        method="post",
        match_json=example_aero,
        json=example_aero,
    )

    results = app.post(client, "/configurations", example_aero)
    assert results == example_aero


def test_delete(httpx_mock: HTTPXMock, client: httpx.Client):
    httpx_mock.add_response(
        url=f"{conceptev_url}/configurations/456?design_instance_id=123",
        method="delete",
        status_code=204,
    )
    httpx_mock.add_response(
        url=f"{conceptev_url}/configurations/489?design_instance_id=123",
        method="delete",
        status_code=404,
    )

    app.delete(client, "/configurations", "456")
    with pytest.raises(Exception) as e:
        app.delete(client, "/configurations", "489")
    assert e.value.args[0].startswith("Failed to delete from")


def test_create_new_project(httpx_mock: HTTPXMock, client: httpx.Client):
    client.params = []
    project_id = "project_id_123"
    account_id = "account_id_123"
    hpc_id = "hpc_id_123"
    title = "Testing Title"
    mocked_project = {"projectId": project_id}

    project_data = {
        "accountId": account_id,
        "hpcId": hpc_id,
        "projectTitle": title,
        "projectGoal": "Created from the CLI",
    }

    httpx_mock.add_response(
        url=f"{ocm_url}/project/create", method="post", match_json=project_data, json=mocked_project
    )

    value = app.create_new_project(client, account_id, hpc_id, title)
    assert value == mocked_project


def test_create_concept(httpx_mock: HTTPXMock, client: httpx.Client):
    design_id = "design_id_123"
    design_instance_id = "design_instance_123"
    project_id = "project_id_123"
    user_id = "user_id_123"
    mocked_concept = {"name": "new_mocked_concept"}

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
    project_id = "project_id_123"
    product_id = "123"
    mocked_design = {
        "designId": design_id,
        "designInstanceList": [{"designInstanceId": design_instance_id}],
        "projectId": project_id,
        "productId": product_id,
    }
    mocked_user = {"userId": user_id}
    httpx_mock.add_response(
        url=f"{ocm_url}/product/list",
        method="get",
        json=[{"productId": product_id, "productName": "CONCEPTEV"}],
    )
    concept_title = "CLI concept"
    design_data = {
        "projectId": project_id,
        "productId": product_id,
        "designTitle": concept_title,
    }
    httpx_mock.add_response(
        url=f"{ocm_url}/design/create", method="post", match_json=design_data, json=mocked_design
    )
    httpx_mock.add_response(url=f"{ocm_url}/user/details", method="post", json=mocked_user)

    httpx_mock.add_response(
        url=f"{conceptev_url}/concepts?design_instance_id={design_instance_id}",
        method="post",
        match_json=concept_data,
        json=mocked_concept,
    )
    value = app.create_new_concept(client, project_id, title=concept_title)
    assert value == mocked_concept


def test_get_concept_ids(httpx_mock: HTTPXMock, client: httpx.Client):
    client.params = []
    mocked_concepts = [
        {"name": "start", "id": "1"},
        {"name": "pie", "id": "3.17"},
        {"name": "end", "id": "ragnorok"},
    ]
    httpx_mock.add_response(url=f"{conceptev_url}/concepts", method="get", json=mocked_concepts)
    returned_concepts = app.get_concept_ids(client)
    for concept in mocked_concepts:
        assert returned_concepts[concept["name"]] == concept["id"]


def test_get_account_ids(httpx_mock: HTTPXMock):
    token = "123"
    mocked_accounts = [
        {"account": {"accountName": "account 1", "accountId": "al;kjasdf"}},
        {"account": {"accountName": "account 2", "accountId": "asdhalkjh"}},
    ]
    httpx_mock.add_response(
        url=f"{ocm_url}/account/list",
        method="post",
        headers={"authorization": token},
        json=mocked_accounts,
        status_code=200,
    )
    returned_account = app.get_account_ids(token)
    for account in mocked_accounts:
        assert (
            returned_account[account["account"]["accountName"]] == account["account"]["accountId"]
        )


def test_get_default_hpc(httpx_mock: HTTPXMock):
    mocked_account = {"accountId": "567"}
    mocked_hpc = {"hpcId": "345"}
    token = "123"
    httpx_mock.add_response(
        url=f"{ocm_url}/account/hpc/default",
        method="post",
        headers={"authorization": token},
        match_json=mocked_account,
        json=mocked_hpc,
        status_code=200,
    )
    hpc_id = app.get_default_hpc(token, mocked_account["accountId"])
    assert hpc_id == mocked_hpc["hpcId"]


def test_create_submit_job(httpx_mock: HTTPXMock, client: httpx.Client):
    account_id = "123"
    hpc_id = "456"
    job_name = "789"
    concept = {
        "requirements_ids": "abc",
        "architecture_id": "def",
        "id": "ghi",
        "design_instance_id": "jkl",
    }
    job_input = {
        "job_name": job_name,
        "requirement_ids": concept["requirements_ids"],
        "architecture_id": concept["architecture_id"],
        "concept_id": concept["id"],
        "design_instance_id": concept["design_instance_id"],
    }
    mocked_job = ({"job": "data"}, {"stuff": "in file"})
    httpx_mock.add_response(
        url=f"{conceptev_url}/jobs?design_instance_id=123&account_id={account_id}",
        match_json=job_input,
        json=mocked_job,
    )
    mocked_info = "job info"
    mocked_job_start = {
        "job": mocked_job[0],
        "uploaded_file": mocked_job[1],
        "account_id": account_id,
        "hpc_id": hpc_id,
        "docker_tag": "default",
        "extra_memory": False,
    }
    httpx_mock.add_response(
        url=f"{conceptev_url}/jobs:start?design_instance_id=123&account_id={account_id}",
        match_json=mocked_job_start,
        json=mocked_info,
    )
    job_info = app.create_submit_job(client, concept, account_id, hpc_id, job_name)
    assert job_info == mocked_info


def test_put(httpx_mock: HTTPXMock, client: httpx.Client):
    example_aero = {"name": "aero_mock_response"}
    mocked_id = "345"
    httpx_mock.add_response(
        url=f"{conceptev_url}/configurations/{mocked_id}?design_instance_id=123",
        method="put",
        match_json=example_aero,
        json=example_aero,
    )

    results = app.put(client, "/configurations", mocked_id, example_aero)
    assert results == example_aero


def test_get_project_id(httpx_mock: HTTPXMock):
    name = "poject_name"
    account_id = "123"
    token = "456"
    project_id = "789"
    example_data = {"projects": [{"projectId": project_id, "projectTitle": name}]}
    httpx_mock.add_response(
        url=ocm_url + "/project/list/page",
        method="post",
        match_json={
            "filterByName": name,
            "accountId": account_id,
            "pageNumber": 0,
            "pageSize": 1000,
        },
        headers={"authorization": token},
        json=example_data,
    )
    result = app.get_project_ids(name, account_id, token)
    assert result == {name: [project_id]}
    result = app.get_project_id(name, account_id, token)
    assert result == project_id


def test_read_file(mocker):
    file_data = "Simple Data"
    mocked_file_data = mocker.mock_open(read_data=file_data)
    mocker.patch("builtins.open", mocked_file_data)
    results = app.read_file("filename")
    assert results == file_data


@pytest.fixture
def mock_job_results(mocker):
    mocker.patch("ansys.conceptev.core.app.job_status")


def test_read_results(httpx_mock: HTTPXMock, client: httpx.Client):
    example_job_info = {"job": "mocked_job", "job_id": "123"}
    example_results = {"results": "returned"}
    httpx_mock.add_response(
        url=f"{conceptev_url}/utilities:data_format_version?design_instance_id=123",
        method="get",
        json=3,
    )
    httpx_mock.add_response(
        url=f"{conceptev_url}/jobs:result?design_instance_id=123&"
        f"results_file_name=output_file_v3.json&calculate_units=true",
        method="post",
        match_json=example_job_info,
        json=example_results,
    )
    httpx_mock.add_response(
        url=ocm_url + "/user/details", method="post", json={"userId": "user_123"}
    )
    httpx_mock.add_response(
        url=ocm_url + "/job/load",
        method="post",
        json={"finalStatus": "COMPLETED", "jobStatus": [{"jobStatus": "complete"}]},
    )
    results = app.read_results(client, example_job_info)
    assert example_results == results


def test_post_file(mocker, httpx_mock: HTTPXMock, client: httpx.Client):
    file_data = "Simple Data"
    file_post_response_data = {"file": "read"}
    component_file_type = "File Type"
    mocked_file_data = mocker.mock_open(read_data=file_data)

    mocker.patch("builtins.open", mocked_file_data)

    filename = "filename"
    httpx_mock.add_response(
        url=f"{conceptev_url}/components:upload?design_instance_id=123"
        f"&component_file_type={component_file_type}",
        method="post",
        json=file_post_response_data,
    )

    result = app.post_component_file(client, filename, component_file_type)
    assert result == file_post_response_data


def test_successful_create(httpx_mock: HTTPXMock, client: httpx.Client):
    mocked_account_id, mocked_hpc_id = "123", "456"
    name = "some name"
    first_word = name.split()[0]
    escaped = re.escape(name)
    for search_string in [name, escaped, first_word]:
        httpx_mock.add_response(
            url=f"{ocm_url}/project/list/page",
            method="post",
            match_json={
                "filterByName": search_string,
                "accountId": mocked_account_id,
                "pageNumber": 0,
                "pageSize": 1000,
            },
            json={"projects": []},
        )

    httpx_mock.add_response(
        url=f"{ocm_url}/project/create",
        method="post",
        match_json={
            "accountId": mocked_account_id,
            "hpcId": mocked_hpc_id,
            "projectTitle": name,
            "projectGoal": "Created from the CLI",
        },
        json={"projectId": "789"},
    )
    results = app.get_or_create_project(client, mocked_account_id, mocked_hpc_id, "some name")
    assert results == "789"


search_strings = ["some name", re.escape("some name"), "some"]


@pytest.mark.parametrize("search_string", search_strings)
def test_successful_get(httpx_mock: HTTPXMock, client: httpx.Client, search_string):
    """Test get or create project."""

    mocked_account_id, mocked_hpc_id = "123", "456"
    for search_string_try in search_strings:
        if search_string_try == search_string:
            project_response = [{"projectId": "789", "projectTitle": "some name"}]
        else:
            project_response = []
        httpx_mock.add_response(
            url=f"{ocm_url}/project/list/page",
            method="post",
            match_json={
                "filterByName": search_string_try,
                "accountId": mocked_account_id,
                "pageNumber": 0,
                "pageSize": 1000,
            },
            json={"projects": project_response},
        )
        if search_string_try == search_string:
            break

    results = app.get_or_create_project(client, mocked_account_id, mocked_hpc_id, "some name")
    assert results == "789"


def test_get_job_file(httpx_mock: HTTPXMock):
    job_id = "123"
    file_name = "cev_job.json"
    token = "123"
    httpx_mock.add_response(
        url=f"{ocm_url}/job/files/{job_id}/{file_name}", method="get", content=b"""{"json":"1"}"""
    )
    results = app.get_job_file(token, job_id, file_name)
    assert results == {"json": "1"}


def test_get_concept(httpx_mock: HTTPXMock, client: httpx.Client):
    design_instance_id = "123"
    httpx_mock.add_response(
        url=f"{conceptev_url}/concepts/{design_instance_id}"
        f"?design_instance_id={design_instance_id}&populated=false",
        method="get",
        json={"name": "concept"},
    )
    httpx_mock.add_response(
        url=f"{conceptev_url}/concepts/{design_instance_id}/configurations"
        f"?design_instance_id={design_instance_id}",
        method="get",
        json=[{"name": "configurations"}],
    )
    httpx_mock.add_response(
        url=f"{conceptev_url}/concepts/{design_instance_id}/components"
        f"?design_instance_id={design_instance_id}",
        method="get",
        json=[{"name": "components"}],
    )
    httpx_mock.add_response(
        url=f"{conceptev_url}/concepts/{design_instance_id}/requirements"
        f"?design_instance_id={design_instance_id}",
        method="get",
        json=[{"name": "reequirements"}],
    )
    httpx_mock.add_response(
        url=f"{conceptev_url}/concepts/{design_instance_id}/architecture"
        f"?design_instance_id={design_instance_id}",
        method="get",
        json={"name": "architecture"},
    )
    response = app.get_concept(client, design_instance_id)
    assert response == {
        "name": "concept",
        "configurations": [{"name": "configurations"}],
        "components": [{"name": "components"}],
        "requirements": [{"name": "reequirements"}],
        "architecture": {"name": "architecture"},
    }


statuses = [STATUS_COMPLETE, STATUS_FINISHED, STATUS_ERROR, None]


@pytest.mark.parametrize("last_status", statuses)
@pytest.mark.parametrize("final_status", statuses)
def test_returns_final_status_when_present(mocker, final_status, last_status):
    job_info = {"job_id": "123"}
    token = "token"
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}
    if final_status is not None:
        mock_response.json.return_value["finalStatus"] = final_status
    if last_status is not None:
        mock_response.json.return_value["lastStatus"] = last_status
    mocker.patch("httpx.post", return_value=mock_response)

    if final_status is None and last_status is None:
        with pytest.raises(ResponseError) as exc:
            result = app.get_status(job_info, token)
        return True
    else:
        result = app.get_status(job_info, token)
        assert result in [final_status, last_status]


@pytest.mark.parametrize(
    "result,expected",
    [(STATUS_COMPLETE, True), (STATUS_FINISHED, True), (STATUS_ERROR, False), (None, False)],
)
def test_check_status(result, expected):
    if expected:
        assert check_status(result)
    elif result is STATUS_ERROR:
        with pytest.raises(Exception) as exc:
            check_status(result)
            assert "Job Failed" in str(exc.value) if result == STATUS_ERROR else True
    else:
        assert not check_status(result)
