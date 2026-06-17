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

from pathlib import Path

from ansys.conceptev.core.settings import Settings

INTEGRATION_CONFIG_DIR = Path(__file__).resolve().parents[2] / "tests" / "integration"


def test_settings(monkeypatch):
    # pydantic-settings resolves "./config.toml" relative to CWD at instantiation time.
    # Changing CWD to tests/integration/ makes it pick up the dev-environment config.toml.
    monkeypatch.chdir(INTEGRATION_CONFIG_DIR)
    monkeypatch.setenv("ACCOUNT_NAME", "borked")
    settings = Settings()
    assert settings.job_timeout == 3600  # from config.toml
    assert settings.ocm_url == "https://dev.portal.onscale.com/api"  # from ./config.toml
    assert settings.account_name == "borked"  # from environment variable
