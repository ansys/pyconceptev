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

# should this test against the deployed api?
from datetime import datetime
import re
import uuid

import httpx
import pytest

from ansys.conceptev.core.auth import create_msal_app, get_ansyId_token
import ansys.conceptev.core.ocm as ocm
from ansys.conceptev.core.settings import settings

OCM_URL = settings.ocm_url


def is_uuid(s: str):
    try:
        uuid.UUID(s)
        return True
    except ValueError:
        return False


@pytest.fixture()
def token():
    msal = create_msal_app()
    token = get_ansyId_token(msal)
    return token


def test_product_id(token):
    """Test product id from OCM."""
    product_id = ocm.get_product_id(token)
    assert product_id == "SAAS000040"


def test_get_user_id(token):
    """Test user id from OCM."""
    user_id = ocm.get_user_id(token)
    assert is_uuid(user_id)


def test_get_account_ids(token):
    """Test account ids from OCM."""
    account_ids = ocm.get_account_ids(token)
    assert account_ids
    for key, value in account_ids.items():
        assert isinstance(key, str)
        assert is_uuid(value)


def test_get_account_id(token):
    """Test account ids from OCM."""
    account_id = ocm.get_account_id(token)
    assert is_uuid(account_id)


@pytest.fixture()
def account_id(token):
    """Look up the test account ID dynamically."""
    return ocm.get_account_id(token)


@pytest.fixture()
def hpc_id(token, account_id):
    """Look up the default HPC ID dynamically."""
    return ocm.get_default_hpc(token, account_id)


@pytest.fixture()
def temp_project(token, account_id, hpc_id):
    """Create a temporary project for the duration of one test, then delete it."""
    client = httpx.Client(headers={"Authorization": token})
    project_name = f"OCM test project {datetime.now()}"
    project = ocm.create_new_project(client, account_id, hpc_id, project_name)
    yield project
    ocm.delete_project(project["projectId"], token)


def test_get_default_hpc(token, account_id):
    """Test default HPC from OCM using dynamically resolved account ID."""
    hpc_id = ocm.get_default_hpc(token, account_id)
    assert is_uuid(hpc_id)


def test_get_project_ids(token, account_id, temp_project):
    """Test project list from OCM by creating a project and then finding it."""
    project_name = temp_project["projectTitle"]
    project_ids = ocm.get_project_ids(re.escape(project_name), account_id, token)
    assert project_name in project_ids.keys()
    assert temp_project["projectId"] in project_ids[project_name]


def test_create_new_project(token, account_id, hpc_id):
    """Test create new project from OCM using dynamically resolved IDs."""
    project_name = f"hello {datetime.now()}"
    client = httpx.Client(headers={"Authorization": token})
    project = ocm.create_new_project(client, account_id, hpc_id, project_name)
    try:
        assert project["projectTitle"] == project_name
        now = datetime.now().timestamp()
        seconds_ago = now - (project["createDate"] / 1000)
        assert seconds_ago < 10
    finally:
        ocm.delete_project(project["projectId"], token)


def test_create_new_design(token, temp_project):
    """Test create new design from OCM using a dynamically created project."""
    product_id = "SAAS000040"
    project_id = temp_project["projectId"]

    client = httpx.Client(headers={"Authorization": token})
    design = ocm.create_new_design(client, project_id, product_id)

    now = datetime.now().timestamp()
    seconds_ago = now - (design["createDate"] / 1000)
    assert seconds_ago < 10
