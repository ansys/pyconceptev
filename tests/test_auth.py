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

import os

import httpx
from msal_extensions import (
    FilePersistence,
    FilePersistenceWithDataProtection,
    KeychainPersistence,
    LibsecretPersistence,
)
import pytest
from pytest_mock import MockerFixture

from ansys.conceptev.core import auth


class MockApp:
    def __init__(self, client_id, authority, token_cache):
        self.client_id = client_id
        self.authority = authority
        self.token_cahce = token_cache

    def get_accounts(self):
        return []

    def acquire_token_silent(self, scopes, account):
        return {"access_token": "mock_cached_token"}

    def acquire_token_interactive(self, scopes, timeout):
        return {"access_token": "mock_token"}


@pytest.fixture
def mockPublcClientCreation(mocker: MockerFixture) -> None:
    mocker.patch("ansys.conceptev.core.auth.PublicClientApplication", MockApp)


@pytest.fixture
def mockCache(mocker: MockerFixture) -> None:
    mocker.patch(
        "ansys.conceptev.core.auth.PublicClientApplication.get_accounts", return_value=["account"]
    )


@pytest.mark.skip  # Not mocked
def test_integration(clean_file) -> None:
    """Test Creating a token from AnsysID."""
    app = auth.create_msal_app()
    token = auth.get_ansyId_token(app)
    results = httpx.get(url=os.environ["ocm_url"] + "/auth", headers={"Authorization": token})

    assert results.status_code == 200


def test_create_build_persistance() -> None:
    """Test Creating MSAL App."""
    cache = auth.build_persistence("token_cache.bin")
    assert isinstance(
        cache,
        (
            FilePersistenceWithDataProtection,
            KeychainPersistence,
            LibsecretPersistence,
            FilePersistence,
        ),
    )


def test_create_msal_app_try_token(mockPublcClientCreation) -> None:
    """Test Creating MSAL App."""
    app = auth.create_msal_app()
    assert isinstance(app, MockApp)
    token = auth.get_ansyId_token(app)
    assert token == "mock_token"


def test_create_msal_app_try_token_cache(mockPublcClientCreation, mockCache) -> None:
    """Test Creating MSAL App."""
    app = auth.create_msal_app()
    assert isinstance(app, MockApp)
    token = auth.get_ansyId_token(app)
    assert token == "mock_cached_token"
