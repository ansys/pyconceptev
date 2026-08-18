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

import importlib.util
from pathlib import Path
import types


def _load_patch_openapi_module() -> types.ModuleType:
    script_path = Path(__file__).resolve().parents[2] / "scripts" / "patch_openapi.py"
    spec = importlib.util.spec_from_file_location("patch_openapi", script_path)
    assert spec is not None and spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_fix_oas31_binary_upload_markers_direct_property() -> None:
    patch_openapi = _load_patch_openapi_module()
    spec = {
        "components": {
            "schemas": {
                "Body_create_file_item": {
                    "type": "object",
                    "properties": {
                        "file": {
                            "type": "string",
                            "contentMediaType": "application/octet-stream",
                            "title": "File",
                        }
                    },
                }
            }
        }
    }

    changes = patch_openapi.fix_oas31_binary_upload_markers(spec)

    file_prop = spec["components"]["schemas"]["Body_create_file_item"]["properties"]["file"]
    assert file_prop["type"] == "string"
    assert file_prop["format"] == "binary"
    assert "contentMediaType" not in file_prop
    assert len(changes) == 1


def test_fix_oas31_binary_upload_markers_optional_and_nested() -> None:
    patch_openapi = _load_patch_openapi_module()
    spec = {
        "components": {
            "schemas": {
                "Body_update_file_item": {
                    "type": "object",
                    "properties": {
                        "file": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "contentMediaType": "application/octet-stream",
                                },
                                {"type": "null"},
                            ]
                        }
                    },
                },
                "Container": {
                    "type": "object",
                    "properties": {
                        "files": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "contentMediaType": "application/octet-stream",
                            },
                        }
                    },
                },
            }
        }
    }

    changes = patch_openapi.fix_oas31_binary_upload_markers(spec)

    any_of_branch = spec["components"]["schemas"]["Body_update_file_item"]["properties"]["file"][
        "anyOf"
    ][0]
    assert any_of_branch["format"] == "binary"
    assert "contentMediaType" not in any_of_branch

    array_items = spec["components"]["schemas"]["Container"]["properties"]["files"]["items"]
    assert array_items["format"] == "binary"
    assert "contentMediaType" not in array_items
    assert len(changes) == 2


def test_fix_oas31_binary_upload_markers_noop_non_octet_stream() -> None:
    patch_openapi = _load_patch_openapi_module()
    spec = {
        "components": {
            "schemas": {
                "HtmlBlob": {
                    "type": "object",
                    "properties": {
                        "doc": {
                            "type": "string",
                            "contentMediaType": "text/html",
                        }
                    },
                }
            }
        }
    }

    changes = patch_openapi.fix_oas31_binary_upload_markers(spec)

    doc_prop = spec["components"]["schemas"]["HtmlBlob"]["properties"]["doc"]
    assert doc_prop["contentMediaType"] == "text/html"
    assert "format" not in doc_prop
    assert changes == []


def test_patch_pipeline_applies_binary_normalization() -> None:
    patch_openapi = _load_patch_openapi_module()
    spec = {
        "openapi": "3.1.0",
        "components": {
            "schemas": {
                "Body_create_file_item": {
                    "type": "object",
                    "properties": {
                        "file": {
                            "type": "string",
                            "contentMediaType": "application/octet-stream",
                        }
                    },
                }
            }
        },
        "paths": {},
    }

    patched, changes = patch_openapi.patch(spec)

    assert (
        spec["components"]["schemas"]["Body_create_file_item"]["properties"]["file"].get("format")
        is None
    )
    patched_file_prop = patched["components"]["schemas"]["Body_create_file_item"]["properties"][
        "file"
    ]
    assert patched_file_prop["format"] == "binary"
    assert "contentMediaType" not in patched_file_prop
    assert any("Normalized binary upload marker" in change for change in changes)
