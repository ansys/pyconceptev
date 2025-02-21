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

"""Authentication for AnsysID."""

import logging

from msal import PublicClientApplication
from msal_extensions import FilePersistence, build_encrypted_persistence, token_cache

from ansys.conceptev.core.settings import settings

logger = logging.getLogger(__name__)
scope = settings.scope
client_id = settings.client_id
authority = settings.authority
USERNAME = settings.conceptev_username
PASSWORD = settings.conceptev_password


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
    except:
        if not fallback_to_plaintext:
            raise
        logger.exception("Encryption unavailable. Opting in to plain text.")
    return FilePersistence(location)


def get_ansyId_token(app) -> str:
    """Get token from AnsysID."""
    result = None
    accounts = app.get_accounts()
    if accounts:
        # Assuming the end user chose this one
        chosen = accounts[0]
        # Now let's try to find a token in cache for this account
        logger.info("Trying to acquire token silently")
        result = app.acquire_token_silent(scopes=[scope], account=chosen)
    if not result and USERNAME and PASSWORD:
        logger.info("Trying to acquire token with username and password")
        result = app.acquire_token_by_username_password(
            username=USERNAME, password=PASSWORD, scopes=[scope]
        )
    if not result:
        logger.info("Trying to acquire token interactively")
        result = app.acquire_token_interactive(scopes=[scope])

    if "access_token" in result:
        return result["access_token"]
    error = result.get("error")
    error_description = result.get("error_description")
    correlation_id = result.get("error_description")
    raise Exception(f"Failed to get token {error}, {error_description}, {correlation_id}.")
