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
"""Settings specification and reading."""
from enum import Enum
import os
from pathlib import Path
from typing import Annotated

from pydantic import AfterValidator, EmailStr, HttpUrl, WebsocketUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

RESOURCE_DIRECTORY = Path(__file__).parents[0].joinpath("resources")
if os.environ.get("PYCONCEPTEV_SETTINGS"):
    TOML_FILE = Path(os.environ["PYCONCEPTEV_SETTINGS"])
else:
    TOML_FILE = RESOURCE_DIRECTORY / "config.toml"
SECRETS_DIR = RESOURCE_DIRECTORY

HttpUrlString = Annotated[HttpUrl, AfterValidator(str)]
WebSocketUrlString = Annotated[WebsocketUrl, AfterValidator(str)]


class Environment(str, Enum):
    """Environments."""

    testing = "testing"
    development = "development"
    production = "production"


class Settings(BaseSettings):
    """Settings."""

    ocm_url: HttpUrlString
    ocm_socket_url: WebSocketUrlString
    conceptev_url: HttpUrlString
    client_id: str
    authority: HttpUrlString
    scope: HttpUrlString
    job_timeout: int
    environment: Environment
    conceptev_username: EmailStr | None  # Only works in testing environment
    conceptev_password: str | None  # Only works in testing environment
    model_config = SettingsConfigDict(
        env_file=[TOML_FILE, "./config.toml"], secrets_dir=RESOURCE_DIRECTORY
    )


settings = Settings()
