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

"""Authentication for AnsysID."""

import logging
import re
from urllib.parse import parse_qs, urlparse

import httpx
from msal import PublicClientApplication
from msal_extensions import FilePersistence, build_encrypted_persistence, token_cache
from pydantic import SecretStr

from ansys.conceptev.core.exceptions import TokenError
from ansys.conceptev.core.settings import settings

logger = logging.getLogger(__name__)
scope = settings.scope
client_id = settings.client_id
authority = settings.authority
PAT_TOKEN = settings.ansys_uat_pat
# Verified-working redirect URI for this app registration (see Ansys's get_token.py
# reference script) - used for both the PAT authorize request and its token exchange.
PAT_REDIRECT_URI = "https://login.microsoftonline.com/common/oauth2/nativeclient"


def _split_authority_policy(full_authority: str) -> tuple[str, str | None]:
    """Split a B2C authority URL into its (tenant base, policy) parts.

    MSAL's authority has the policy embedded in the path
    (``https://host/tenant/POLICY``), but the plain OAuth2 authorize endpoint
    expects the policy as a ``p=`` query parameter against the tenant-only path
    (``https://host/tenant/oauth2/v2.0/authorize?p=POLICY``).
    """
    parsed = urlparse(full_authority)
    parts = parsed.path.strip("/").split("/")
    if len(parts) < 2:
        return full_authority, None
    policy = parts[-1]
    base_path = "/".join(parts[:-1])
    return f"{parsed.scheme}://{parsed.netloc}/{base_path}", policy


_AUTHORIZE_BASE, _AUTHORIZE_POLICY = _split_authority_policy(authority)


def _extract_error_detail(body: str) -> str | None:
    """Pull a human-readable detail out of a B2C HTML error page, if present."""
    match = re.search(r'"Detail"\s*:\s*"([^"]+)"', body)
    return match.group(1) if match else None


def _build_pat_authorize_request(pat_value: str, *, prompt_none: bool = False) -> httpx.Request:
    """Build the PAT authorize request, mirroring Ansys's verified ``get_token.py``.

    The policy is sent as a ``p=`` query parameter (not embedded in the path),
    and the full resource scope is requested up front, same as that script.
    """
    params = {
        "client_id": client_id,
        "nonce": "defaultNonce",
        "redirect_uri": PAT_REDIRECT_URI,
        "scope": f"openid offline_access {scope}",
        "response_type": "code",
        "id_token_hint": pat_value,
    }
    if _AUTHORIZE_POLICY:
        params["p"] = _AUTHORIZE_POLICY
    if prompt_none:
        params["prompt"] = "none"
    return httpx.Request("GET", f"{_AUTHORIZE_BASE}/oauth2/v2.0/authorize", params=params)


def _acquire_token_by_pat(app: PublicClientApplication, pat: SecretStr) -> dict:
    """Exchange a PAT for a token, per Ansys's documented PAT authentication flow.

    See: https://developer.synopsys.com/docs/ansys-id-sso/pat-authentication-guide
    The PAT is passed as an ``id_token_hint`` to the B2C authorize endpoint to
    obtain an authorization code (not usable as a bearer token itself), which
    MSAL then exchanges — and caches — for a normal access token.
    """
    request = _build_pat_authorize_request(pat.get_secret_value())
    # httpx logs the full request URL at INFO level, which would otherwise leak the PAT
    # (embedded in the query string) to logs/log-capturing test runners.
    httpx_logger = logging.getLogger("httpx")
    previous_level = httpx_logger.level
    httpx_logger.setLevel(logging.WARNING)
    try:
        # Default httpx timeout (5s) is too tight for some CI runners' network path
        # to the identity provider.
        with httpx.Client(timeout=30) as client:
            response = client.send(request, follow_redirects=False)
    finally:
        httpx_logger.setLevel(previous_level)
    location = response.headers.get("location")
    if not location:
        detail = _extract_error_detail(response.text) or "no additional detail available"
        raise TokenError(
            f"PAT exchange failed: AnsysID returned HTTP {response.status_code} without a "
            f"redirect. Detail: {detail}"
        )
    params = parse_qs(urlparse(location).query)
    if "code" not in params:
        error_description = params.get("error_description", ["Unknown error"])[0]
        raise TokenError(f"PAT exchange failed: {error_description}")
    return app.acquire_token_by_authorization_code(
        code=params["code"][0], scopes=[scope], redirect_uri=PAT_REDIRECT_URI
    )


def create_msal_app(cache_filepath="token_cache.bin") -> PublicClientApplication:
    """Create MSAL App with a persistent cache."""
    persistence = build_persistence(cache_filepath)
    cache = token_cache.PersistedTokenCache(persistence)
    app = PublicClientApplication(client_id=client_id, authority=authority, token_cache=cache)
    return app


def build_persistence(location, fallback_to_plaintext=True):
    """Create Persistent Cache."""
    try:
        return build_encrypted_persistence(location)
    except Exception:
        if not fallback_to_plaintext:
            raise
        logger.exception("Encryption unavailable. Opting in to plain text.")
    return FilePersistence(location)


def get_ansyId_token(app, force=False, allow_interactive=True) -> str:
    """Get token from AnsysID.

    Tries silent (cached), then the configured Ansys UAT PAT exchange, then
    interactive sign-in, in that order. Set ``allow_interactive=False`` to
    prevent the interactive fallback, e.g. in automated/CI contexts where no
    human is available to complete it.
    """
    result = None
    accounts = app.get_accounts()
    if accounts and not force:
        # Assuming the end user chose this one
        chosen = accounts[0]
        # Now let's try to find a token in cache for this account
        logger.info("Trying to acquire token silently")
        result = app.acquire_token_silent(scopes=[scope], account=chosen)
    if not result and PAT_TOKEN:
        logger.info("Trying to exchange the configured Ansys UAT PAT for a token")
        result = _acquire_token_by_pat(app, PAT_TOKEN)
    if not result and allow_interactive:
        logger.info("Trying to acquire token interactively")
        result = app.acquire_token_interactive(scopes=[scope])

    if result and "access_token" in result:
        return result["access_token"]
    if result is None:
        raise Exception("Failed to get token: no non-interactive credentials were available.")
    error = result.get("error")
    error_description = result.get("error_description")
    correlation_id = result.get("error_description")
    raise Exception(f"Failed to get token {error}, {error_description}, {correlation_id}.")


class AnsysIDAuth(httpx.Auth):
    """Custom Auth implementation for httpx.

    This class is used to authenticate requests to AnsysID using MSAL.
    """

    def __init__(self, cache_filepath="token_cache.bin"):
        """Initialize the AnsysIDAuth class."""
        app = create_msal_app(cache_filepath=cache_filepath)
        self.app = app

    def auth_flow(self, request):
        """Send the request, with a custom `Authentication` header."""
        token = get_ansyId_token(self.app)
        request.headers["Authorization"] = token
        response = yield request
        if response.status_code == 401:
            logger.info("Token expired or rejected (401). Refreshing token and retrying.")
            token = get_ansyId_token(self.app, force=True)
            request.headers["Authorization"] = token
            yield request


def get_token(client: httpx.Client) -> str:
    """Get the token from the client."""
    if client.auth is not None and client.auth.app is not None:
        return get_ansyId_token(client.auth.app)
    elif client.headers is not None and "Authorization" in client.headers:
        return client.headers["Authorization"]
    raise TokenError("App not found in client.")
