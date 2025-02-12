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
import os
from pathlib import Path
from typing import Annotated

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from pydantic import AfterValidator, EmailStr, HttpUrl, WebsocketUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

RESOURCE_DIRECTORY = Path(__file__).parents[0].joinpath("resources")

SECRETS_DIR = RESOURCE_DIRECTORY

HttpUrlString = Annotated[HttpUrl, AfterValidator(str)]
WebSocketUrlString = Annotated[WebsocketUrl, AfterValidator(str)]


class Settings(BaseSettings):
    """Settings."""

    ocm_url: HttpUrlString
    ocm_socket_url: WebSocketUrlString
    conceptev_url: HttpUrlString
    client_id: str
    authority: HttpUrlString
    scope: HttpUrlString
    job_timeout: int
    conceptev_username: EmailStr | None = None  # Only works in testing environment
    conceptev_password: str | None = None  # Only works in testing environment
    account_name: str | None
    model_config = SettingsConfigDict(
        env_file=[
            os.environ.get("PYCONCEPTEV_SETTINGS", RESOURCE_DIRECTORY / "config.toml"),
            "./config.toml",
        ],
        secrets_dir=[RESOURCE_DIRECTORY, "."],
    )


def load_settings(toml_file) -> Settings:
    """Load settings."""
    with open(toml_file, "rb") as f:
        settings_data = tomllib.load(f)
    return Settings.model_validate(settings_data)


settings = Settings()
