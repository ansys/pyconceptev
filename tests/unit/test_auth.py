# Copyright (C) 2023 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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
from pydantic import SecretStr
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

    def acquire_token_by_authorization_code(self, code, scopes, redirect_uri):
        return {"access_token": f"mock_pat_token_for_{code}"}


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
    mocker.patch("ansys.conceptev.core.auth.PAT_TOKEN", None)
    app = auth.create_msal_app()
    assert isinstance(app, MockApp)
    token = auth.get_ansyId_token(app)
    assert token == "mock_token"


def test_create_msal_app_try_token_cache(mockPublcClientCreation, mockCache, mocker) -> None:
    """Test Creating MSAL App with cache"""
    mocker.patch("ansys.conceptev.core.auth.PAT_TOKEN", None)
    app = auth.create_msal_app()
    assert isinstance(app, MockApp)
    token = auth.get_ansyId_token(app)
    assert token == "mock_cached_token"


def test_get_ansyId_token_exchanges_pat_for_access_token(
    mockPublcClientCreation, mocker, httpx_mock: HTTPXMock
) -> None:
    """A configured PAT is exchanged for an access token (not used as a bearer token itself)."""
    mocker.patch("ansys.conceptev.core.auth.PAT_TOKEN", SecretStr("fake-test-pat"))
    httpx_mock.add_response(
        status_code=302,
        headers={"location": "https://example.com/redirect?code=fake-auth-code"},
    )
    app = auth.create_msal_app()
    token = auth.get_ansyId_token(app)
    assert token == "mock_pat_token_for_fake-auth-code"


def test_get_ansyId_token_force_true_skips_cache_and_uses_pat(
    mockPublcClientCreation, mockCache, mocker, httpx_mock: HTTPXMock
) -> None:
    """``force=True`` (used on the 401 retry in ``AnsysIDAuth.auth_flow``) must skip
    the cached/silent token and re-exchange the PAT for a fresh one, rather than
    reusing a token that was possibly just rejected."""
    mocker.patch("ansys.conceptev.core.auth.PAT_TOKEN", SecretStr("fake-test-pat"))
    mock_silent = mocker.patch.object(MockApp, "acquire_token_silent")
    httpx_mock.add_response(
        status_code=302,
        headers={"location": "https://example.com/redirect?code=fake-auth-code"},
    )
    app = auth.create_msal_app()

    token = auth.get_ansyId_token(app, force=True)

    assert token == "mock_pat_token_for_fake-auth-code"
    mock_silent.assert_not_called()


def test_get_ansyId_token_pat_exchange_without_redirect_raises(
    mockPublcClientCreation, mocker, httpx_mock: HTTPXMock
) -> None:
    """A missing redirect (e.g. an invalid/expired PAT) should fail loudly, not silently
    fall through to interactive, and should surface the provider's error detail."""
    mocker.patch("ansys.conceptev.core.auth.PAT_TOKEN", SecretStr("fake-test-pat"))
    httpx_mock.add_response(status_code=200, text='{"Detail":"PAT is expired"}')
    app = auth.create_msal_app()

    with pytest.raises(auth.TokenError, match="PAT exchange failed.*PAT is expired"):
        auth.get_ansyId_token(app, allow_interactive=False)


def test_split_authority_policy_extracts_policy() -> None:
    """MSAL's authority (policy embedded in the path) should split into a bare
    tenant base and the policy name."""
    base, policy = auth._split_authority_policy("https://host/tenant/POLICY")
    assert base == "https://host/tenant"
    assert policy == "POLICY"


def test_split_authority_policy_without_policy_segment() -> None:
    """A tenant-only authority (no policy segment) has nothing to split out."""
    base, policy = auth._split_authority_policy("https://host/tenant")
    assert base == "https://host/tenant"
    assert policy is None


def test_build_pat_authorize_request_includes_policy_and_full_scope() -> None:
    """The authorize request should send the policy as ``p=`` and the full resource
    scope up front, matching Ansys's verified ``get_token.py`` reference script."""
    request = auth._build_pat_authorize_request("my-pat-value")
    params = dict(request.url.params)
    assert params["p"] == auth._AUTHORIZE_POLICY
    assert params["scope"] == f"openid offline_access {auth.scope}"
    assert params["id_token_hint"] == "my-pat-value"
    assert params["redirect_uri"] == auth.PAT_REDIRECT_URI
    assert params["response_type"] == "code"
    assert "prompt" not in params
    assert str(request.url).startswith(f"{auth._AUTHORIZE_BASE}/oauth2/v2.0/authorize")


def test_build_pat_authorize_request_prompt_none() -> None:
    """``prompt=none`` should only be included when explicitly requested."""
    request = auth._build_pat_authorize_request("my-pat-value", prompt_none=True)
    assert dict(request.url.params)["prompt"] == "none"


def test_extract_error_detail_found() -> None:
    """A B2C HTML error page embeds a JSON-ish \"Detail\" field to surface."""
    body = '<html>...{"Title":"Error","Detail":"The id_token_hint is expired."}...</html>'
    assert auth._extract_error_detail(body) == "The id_token_hint is expired."


def test_extract_error_detail_missing() -> None:
    """When there's no recognizable detail, return None rather than guessing."""
    assert auth._extract_error_detail("<html>some unrelated page</html>") is None


def test_get_ansyId_token_without_interactive_fallback_raises(mockPublcClientCreation, mocker):
    """When no non-interactive credentials are available, don't fall back to an
    interactive browser sign-in (e.g. so CI doesn't hang)."""
    mocker.patch("ansys.conceptev.core.auth.PAT_TOKEN", None)
    mock_interactive = mocker.patch.object(MockApp, "acquire_token_interactive")
    app = auth.create_msal_app()

    with pytest.raises(Exception, match="no non-interactive credentials"):
        auth.get_ansyId_token(app, allow_interactive=False)

    mock_interactive.assert_not_called()


def test_auth_initialization_creates_msal_app(mocker):
    mock_create_msal_app = mocker.patch("ansys.conceptev.core.auth.create_msal_app")
    auth_instance = auth.AnsysIDAuth()
    assert auth_instance.app == mock_create_msal_app.return_value


def test_auth_flow_adds_authorization_header(mocker, httpx_mock: HTTPXMock):
    mocker.patch("ansys.conceptev.core.auth.get_ansyId_token", return_value="auth_class_token")
    auth_instance = auth.AnsysIDAuth()
    httpx_mock.add_response(url="http://example.com")
    client = httpx.Client(auth=auth_instance)
    response = client.get("http://example.com")
    assert response.request.headers["Authorization"] == "auth_class_token"


def test_auth_flow_retries_on_401_with_fresh_token(mocker, httpx_mock: HTTPXMock):
    """When the server returns 401, auth_flow should force-refresh the token and retry."""
    mock_get_ansyId_token = mocker.patch(
        "ansys.conceptev.core.auth.get_ansyId_token",
        side_effect=["expired_token", "fresh_token"],
    )
    auth_instance = auth.AnsysIDAuth()
    httpx_mock.add_response(url="http://example.com", status_code=401)
    httpx_mock.add_response(url="http://example.com", status_code=200)

    client = httpx.Client(auth=auth_instance)
    response = client.get("http://example.com")

    assert response.status_code == 200
    assert mock_get_ansyId_token.call_count == 2
    # Second call must use force=True to bypass the MSAL cache
    assert mock_get_ansyId_token.call_args_list[1] == mocker.call(auth_instance.app, force=True)
    assert response.request.headers["Authorization"] == "fresh_token"


def test_auth_flow_does_not_retry_on_other_errors(mocker, httpx_mock: HTTPXMock):
    """Non-401 errors should not trigger a token refresh retry."""
    mock_get_ansyId_token = mocker.patch(
        "ansys.conceptev.core.auth.get_ansyId_token", return_value="auth_class_token"
    )
    auth_instance = auth.AnsysIDAuth()
    httpx_mock.add_response(url="http://example.com", status_code=403)

    client = httpx.Client(auth=auth_instance)
    response = client.get("http://example.com")

    assert response.status_code == 403
    assert mock_get_ansyId_token.call_count == 1


def test_auth_flow_token_expires_mid_sequence(mocker, httpx_mock: HTTPXMock):
    """When a token expires mid-sequence, the failing request retries with a fresh token
    and all subsequent requests in the sequence also use the fresh token."""
    # Requests 1 & 2 succeed with the original token.
    # Request 3 gets a 401 (token just expired), then retries with a fresh token.
    # Request 4 should use the now-cached fresh token.
    token_sequence = [
        "original_token",  # req 1 – initial fetch
        "original_token",  # req 2 – initial fetch
        "original_token",  # req 3 – initial fetch (will be rejected)
        "fresh_token",  # req 3 – force-refresh after 401
        "fresh_token",  # req 4 – silent fetch (MSAL cache now holds fresh token)
    ]
    mock_get_ansyId_token = mocker.patch(
        "ansys.conceptev.core.auth.get_ansyId_token", side_effect=token_sequence
    )
    auth_instance = auth.AnsysIDAuth()

    httpx_mock.add_response(url="http://example.com", status_code=200)  # req 1
    httpx_mock.add_response(url="http://example.com", status_code=200)  # req 2
    httpx_mock.add_response(url="http://example.com", status_code=401)  # req 3 – token expired
    httpx_mock.add_response(url="http://example.com", status_code=200)  # req 3 – retry
    httpx_mock.add_response(url="http://example.com", status_code=200)  # req 4

    client = httpx.Client(auth=auth_instance)
    responses = [client.get("http://example.com") for _ in range(4)]

    assert [r.status_code for r in responses] == [200, 200, 200, 200]
    assert mock_get_ansyId_token.call_count == 5
    # The force-refresh must have been triggered on the 4th call (req 3 retry)
    assert mock_get_ansyId_token.call_args_list[3] == mocker.call(auth_instance.app, force=True)
