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
import httpx
from msal_extensions import (
    FilePersistence,
    FilePersistenceWithDataProtection,
    KeychainPersistence,
    LibsecretPersistence,
)
import pytest
from pytest_httpx import HTTPXMock
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

    def acquire_token_interactive(self, scopes):
        return {"access_token": "mock_token"}

    def acquire_token_by_username_password(self, username, password, scopes):
        return {"access_token": "mock_token_password"}


@pytest.fixture
def mockPublcClientCreation(mocker: MockerFixture) -> None:
    mocker.patch("ansys.conceptev.core.auth.PublicClientApplication", MockApp)


@pytest.fixture
def mockCache(mocker: MockerFixture) -> None:
    mocker.patch(
        "ansys.conceptev.core.auth.PublicClientApplication.get_accounts", return_value=["account"]
    )


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


def test_create_msal_app_try_token(mockPublcClientCreation, mocker) -> None:
    """Test Creating MSAL App."""
    mocker.patch("ansys.conceptev.core.auth.USERNAME", None)
    mocker.patch("ansys.conceptev.core.auth.PASSWORD", None)
    app = auth.create_msal_app()
    assert isinstance(app, MockApp)
    token = auth.get_ansyId_token(app)
    assert token == "mock_token"


def test_create_msal_app_try_token_cache(mockPublcClientCreation, mockCache, mocker) -> None:
    """Test Creating MSAL App with cache"""
    mocker.patch("ansys.conceptev.core.auth.USERNAME", None)
    mocker.patch("ansys.conceptev.core.auth.PASSWORD", None)
    app = auth.create_msal_app()
    assert isinstance(app, MockApp)
    token = auth.get_ansyId_token(app)
    assert token == "mock_cached_token"


def test_create_msal_app_password(mockPublcClientCreation, mocker) -> None:
    """Test Creating MSAL App."""
    mocker.patch("ansys.conceptev.core.auth.USERNAME", "something")
    mocker.patch("ansys.conceptev.core.auth.PASSWORD", "something")
    app = auth.create_msal_app()
    assert isinstance(app, MockApp)
    token = auth.get_ansyId_token(app)
    assert token == "mock_token_password"


def test_auth_initialization_creates_msal_app(mocker):
    mock_create_msal_app = mocker.patch("ansys.conceptev.core.auth.create_msal_app")
    auth_instance = auth.AnsysIDAuth()
    assert auth_instance.app == mock_create_msal_app.return_value


def test_auth_flow_adds_authorization_header(mocker, httpx_mock: HTTPXMock):
    mock_get_ansyId_token = mocker.patch(
        "ansys.conceptev.core.auth.get_ansyId_token", return_value="auth_class_token"
    )
    auth_instance = auth.AnsysIDAuth()
    httpx_mock.add_response(url=f"http://example.com")
    client = httpx.Client(auth=auth_instance)
    response = client.get("http://example.com")
    assert response.request.headers["Authorization"] == "auth_class_token"
