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

"""Progress monitoring with websockets."""

import asyncio
import json

from websockets.asyncio.client import connect

STATUS_COMPLETE = "complete"
STATUS_FINISHED = "FINISHED"
STATUS_ERROR = "FAILED"


def connect_to_ocm(user_id: str, token: str):
    """Connect to the OnScale Cloud Messaging service."""
    uri = (
        f"wss://sockets.prod.portal.onscale.com/socket/user?userId={user_id}&Authorization={token}"
    )
    return connect(uri)


def parse_message(message: str, job_id: str):
    """Parse the message and return the status or progress."""
    message_data = json.loads(message)

    if message_data.get("jobId", "Unknown") == job_id:
        message_type = message_data.get("messagetype", None)
        if message_type == "status":
            status = message_data.get("status", None)
            print(f"Status:{status}")
            return status
        elif message_type == "progress":
            progress = message_data.get("progress", None)
            print(f"Progress:{progress}")


async def monitor_job_messages(job_id: str, user_id: str, token: str):
    """Monitor job messages and return the status when complete."""
    websocket_client = connect_to_ocm(user_id, token)
    async with websocket_client as websocket:
        async for message in websocket:
            status = parse_message(message, job_id)
            if check_status(status):
                return status


def check_status(status: str):
    """Check if the status is complete or finished."""
    if status == STATUS_COMPLETE or status == STATUS_FINISHED:
        return True
    elif status == STATUS_ERROR:
        raise Exception("Job Failed")
    else:
        return False


def monitor_job_progress(job_id: str, user_id: str, token: str, already_async: bool = False):
    """Monitor job progress and return the status when complete."""
    if already_async:
        loop = asyncio.get_event_loop()
        task = loop.create_task(monitor_job_messages(job_id, user_id, token))
        result = loop.run_until_complete(task)
    else:
        result = asyncio.run(monitor_job_messages(job_id, user_id, token))
    return result
