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

# should this test against the deployed api?
from datetime import datetime
import re

import httpx
import pytest

from ansys.conceptev.core.auth import create_msal_app, get_ansyId_token
import ansys.conceptev.core.ocm as ocm
from ansys.conceptev.core.settings import settings

OCM_URL = settings.ocm_url


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
    assert user_id == "95bb6bf9-0afd-4426-b736-7e1c8abd5a78"


def test_get_account_ids(token):
    """Test account ids from OCM."""
    account_ids = ocm.get_account_ids(token)
    assert account_ids == {
        "ConceptEv Test Account": "2a566ece-938d-4658-bae5-ffa387ac0547",
        "conceptev_testing@ansys.com": "108581c8-13e6-4b39-8051-5f8e61135aca",
    }


def test_get_account_id(token):
    """Test account ids from OCM."""
    account_id = ocm.get_account_id(token)
    assert account_id == "2a566ece-938d-4658-bae5-ffa387ac0547"


def test_get_default_hpc(token):
    """Test default HPC from OCM."""
    account_id = "2a566ece-938d-4658-bae5-ffa387ac0547"
    hpc_id = ocm.get_default_hpc(token, account_id)
    assert hpc_id == "3ded64e3-5a83-24a8-b6e4-9fc30f97a654"


def test_get_project_ids(token):
    """Test projects from OCM."""
    project_name = "New Project (with brackets)"

    account_id = "2a566ece-938d-4658-bae5-ffa387ac0547"
    project_ids = ocm.get_project_ids(re.escape(project_name), account_id, token)
    assert project_name in project_ids.keys()
    assert "00932037-a633-464c-8d05-28353d9bfc49" in project_ids[project_name]


def test_create_new_project(token):
    """Test create new project from OCM."""
    account_id = "2a566ece-938d-4658-bae5-ffa387ac0547"
    hpc_id = "23c70728-b930-d1eb-a0b1-dbf9ea0f6278"
    project_name = f"hello {datetime.now()}"
    client = httpx.Client(headers={"Authorization": token})
    project = ocm.create_new_project(client, account_id, hpc_id, project_name)
    assert project["projectTitle"] == project_name
    now = datetime.now().timestamp()
    seconds_ago = now - (project["createDate"] / 1000)
    assert seconds_ago < 10


def test_create_new_design(token):
    """Test create new project from OCM."""

    product_id = "SAAS000040"
    project_id = "fcafedf2-9cb6-4035-9c6c-2bd7602537f2"

    client = httpx.Client(headers={"Authorization": token})
    design = ocm.create_new_design(client, project_id, product_id)

    now = datetime.now().timestamp()
    seconds_ago = now - (design["createDate"] / 1000)
    assert seconds_ago < 10
