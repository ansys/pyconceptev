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

import json
from unittest.mock import AsyncMock, patch

import pytest

from ansys.conceptev.core.progress import (
    STATUS_COMPLETE,
    STATUS_ERROR,
    STATUS_FINISHED,
    check_status,
    connect_to_ocm,
    monitor_job_messages,
    monitor_job_progress,
    parse_message,
    ssl_context,
)


@pytest.mark.asyncio
async def test_connect_to_ocm():
    user_id = "test_user"
    token = "test_token"
    expected_uri = (
        f"wss://sockets.prod.portal.onscale.com/socket/user?userId={user_id}&Authorization={token}"
    )

    with patch("ansys.conceptev.core.progress.connect") as mock_connect:
        connect_to_ocm(user_id, token)
        mock_connect.assert_called_with(expected_uri, ssl=ssl_context)


def test_parse_message():
    job_id = "test_job"
    status_message = json.dumps(
        {"jobId": job_id, "messagetype": "status", "status": STATUS_COMPLETE}
    )
    progress_message = json.dumps({"jobId": job_id, "messagetype": "progress", "progress": 50})

    assert parse_message(status_message, job_id) == STATUS_COMPLETE
    assert parse_message(progress_message, job_id) is None


class AsyncContextManager:

    def __init__(self, items):
        self.items = items

    async def __aenter__(self):
        return AsyncIterator(self.items)

    async def __aexit__(self, exc_type, exc, tb):
        pass


class AsyncIterator:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        else:
            raise StopAsyncIteration


@pytest.mark.asyncio
async def test_monitor_job_messages():
    job_id = "test_job"
    user_id = "test_user"
    token = "test_token"
    status_message = json.dumps(
        {"jobId": job_id, "messagetype": "status", "status": STATUS_COMPLETE}
    )

    with patch("ansys.conceptev.core.progress.connect_to_ocm") as mock_connect:
        mock_connect.return_value = AsyncContextManager([status_message])
        result = await monitor_job_messages(job_id, user_id, token)
        assert result == STATUS_COMPLETE


def test_check_status():
    assert check_status(STATUS_COMPLETE) is True
    assert check_status(STATUS_FINISHED) is True
    with pytest.raises(Exception, match="Job Failed"):
        check_status(STATUS_ERROR)
    assert check_status("unknown_status") is False


def test_monitor_job_progress():
    job_id = "test_job"
    user_id = "test_user"
    token = "test_token"

    with patch(
        "ansys.conceptev.core.progress.monitor_job_messages", new_callable=AsyncMock
    ) as mock_monitor:
        mock_monitor.return_value = STATUS_COMPLETE
        result = monitor_job_progress(job_id, user_id, token)
        mock_monitor.assert_called_with(job_id, user_id, token)
        assert result == STATUS_COMPLETE
