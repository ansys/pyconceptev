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

"""Progress monitoring with websockets."""

import asyncio
import datetime
import json
import logging
import os
import ssl
import sys
from pathlib import Path

import certifi
import httpx
from msal import PublicClientApplication
from websockets.asyncio.client import connect

from ansys.conceptev.core.auth import get_ansyId_token
from ansys.conceptev.core.settings import settings

if sys.version_info >= (3, 11):
    import asyncio as async_timeout
else:
    import async_timeout

STATUS_COMPLETE = "COMPLETED"
STATUS_FINISHED = "FINISHED"
STATUS_ERROR = "FAILED"
OCM_SOCKET_URL = settings.ocm_socket_url
JOB_TIMEOUT = settings.job_timeout

logger = logging.getLogger(__name__)
# Optional file path for capturing progress messages from subprocesses where
# stdout is suppressed (e.g. optiSLang integration plugin).  Set the
# CONCEPTEV_PROGRESS_LOG environment variable to an absolute file path before
# launching the subprocess and the messages will be appended there.
_PROGRESS_LOG_FILE = os.environ.get("CONCEPTEV_PROGRESS_LOG")


def _log(message: str) -> None:
    """Log a progress message via the standard logger and optionally to a file."""
    logger.info(message)
    if _PROGRESS_LOG_FILE:
        try:
            Path(_PROGRESS_LOG_FILE).parent.mkdir(parents=True, exist_ok=True)
            with open(_PROGRESS_LOG_FILE, "a", encoding="utf-8") as fh:
                fh.write(f"{datetime.datetime.now()}: {message}\n")
        except OSError:
            pass
    else:
        print(message)


def generate_ssl_context() -> ssl.SSLContext:
    """Generate SSL context for secure websocket connection."""
    # Try using truststore for system certificates if available
    if not settings.ssl_cert_file:
        try:
            import truststore

            return truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        except ImportError:
            pass

    # Use configured cert file or fall back to certifi's default bundle
    cert_file = settings.ssl_cert_file or certifi.where()

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(cert_file)
    return context


ssl_context = generate_ssl_context()


def connect_to_ocm(user_id: str, token: str):
    """Connect to the OnScale Cloud Messaging service."""
    uri = f"{OCM_SOCKET_URL}/user?userId={user_id}&Authorization={token}"
    return connect(uri, ssl=ssl_context)


def get_status(message: str, job_id: str):
    """Parse the message and return the status or progress."""
    message_data = json.loads(message)

    if message_data.get("jobId", "Unknown") == job_id:
        message_type = next(
            (v for k, v in message_data.items() if k.lower() == "messagetype"), None
        )
        if message_type and message_type.lower() == "status":
            status = message_data.get("status", None)
            if status:
                _log(f"Status:{status}")
                return status.upper()
        elif message_type and message_type.lower() == "progress":
            progress = message_data.get("progress", None)
            _log(f"Progress:{progress}")
        elif message_type and message_type.lower() == "error":
            error = message_data.get("message", None)
            _log(f"Error:{error}")


def get_values(message: str, job_id: str) -> dict:
    """Parse the message and return the calculated values."""
    message_data = json.loads(message)

    if message_data.get("jobId", "Unknown") == job_id:
        message_type = next(
            (v for k, v in message_data.items() if k.lower() == "messagetype"), None
        )
        if message_type and message_type.lower() == "progress" and message_data.get("progress", None) == 1:
            calculated_values = message_data.get("calculated_values", None)
            _log(f"Calculated Values:{calculated_values}")
            return calculated_values


async def get_job_messages(
    job_id: str, user_id: str, token: str, app: PublicClientApplication, timeout=JOB_TIMEOUT
):
    """Get job messages and error on timeout."""
    try:
        async with async_timeout.timeout(timeout):
            while True:
                websocket_client = connect_to_ocm(user_id, token)
                async with websocket_client as websocket:
                    _log("Connected to OCM Websockets.")
                    # Guard: re-poll REST in case the job completed while connecting.
                    _r = httpx.Client(
                        base_url=settings.ocm_url,
                        verify=ssl_context,
                        headers={"Authorization": token},
                    ).post("/job/load", json={"jobId": job_id})
                    if _r.status_code == 200:
                        _d = _r.json()
                        _s = _d.get("finalStatus") or _d.get("lastStatus")
                        if _s and check_status(_s.upper()):
                            return
                    async for message in websocket:
                        yield message
                token = get_ansyId_token(app)
    except TimeoutError as err:
        raise Exception(
            f"Timeout Error: Job ({job_id}) is taking too long to complete (>{timeout} seconds)."
        ) from err


async def monitor_job_messages(
    job_id: str, user_id: str, token: str, app: PublicClientApplication, timeout=JOB_TIMEOUT
):
    """Monitor job messages and return the status when complete."""
    async for message in get_job_messages(job_id, user_id, token, app, timeout):
        status = get_status(message, job_id)
        if check_status(status):
            return status


async def get_calculated_values(
    job_id: str, user_id: str, token: str, app: PublicClientApplication, timeout=JOB_TIMEOUT
):
    """Get Calculated Values."""
    async for message in get_job_messages(job_id, user_id, token, app, timeout):
        values = get_values(message, job_id)
        if values is not None:
            return values


def check_status(status: str):
    """Check if the status is complete or finished."""
    if status is None:
        return False
    s = status.upper()
    if s in (STATUS_COMPLETE, STATUS_FINISHED):
        return True
    if s == STATUS_ERROR:
        raise Exception("Job Failed")
    return False


def monitor_job_progress(
    job_id: str, user_id: str, token: str, app: PublicClientApplication, timeout=JOB_TIMEOUT
):
    """Monitor job progress and return the status when complete."""
    result = asyncio.run(monitor_job_messages(job_id, user_id, token, app, timeout))
    return result


if __name__ == "__main__":
    """Monitor a single job progress."""
    from ansys.conceptev.core.app import get_user_id
    from ansys.conceptev.core.auth import create_msal_app

    job_id = "ae3f3b4b-91d8-4cdd-8fa3-25eb202a561e"  # Replace with your job ID
    msal_app = create_msal_app()
    token = get_ansyId_token(msal_app)
    user_id = get_user_id(token)
    monitor_job_progress(job_id, user_id, token, msal_app, timeout=1)
