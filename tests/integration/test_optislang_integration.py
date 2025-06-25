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

# Optislang Integration Test
# A poor mans integration test for the optislang integration.
# Looks at conceptev/utils/api_helper.py to see pyconceptev usage within ConceptEV integration.

from ansys.conceptev.core import auth, exceptions


def test_exceptions():
    """Example Exception Usage in api_helper"""
    try:
        raise exceptions.ResponseError("This is a test error")
    except exceptions.ResponseError as e:
        assert e.args[0].lower()


def test_auth_app():
    """Test that the optislang integration works."""
    msal_app = auth.create_msal_app()
    token = auth.get_ansyId_token(msal_app)


# def test_app():
#    app.get_http_client(token, design_instance_id)
#     client = app.get_http_client(token)
#     concept = app.get(client, "/concepts", id=design_instance_id, params={"populated": False})
#     concept["configurations"] = app.get(client, f"/concepts/{design_instance_id}/configurations")
#     concept["components"] = app.get(client, f"/concepts/{design_instance_id}/components")
#     concept["requirements"] = app.get(client, f"/concepts/{design_instance_id}/requirements")
#     arch_id = concept['architecture_id']
#     concept["architecture"] = app.get(
#         client,
#         f"/architectures/{arch_id}",
#         params={"design_instance_id": design_instance_id}
#     )
#     concept_data = app.get_concept(client, design_instance_id)
#     data_types ?????
#     posted_data = app.post(client, f"/{data_type}", data=data)
#     accounts = app.get_account_ids(token)
#     hpc_id = app.get_default_hpc(token, account_id)
#     job_info = app.create_submit_job(
#         client,
#         concept_data,
#         account_id,
#         hpc_id,
#         job_name
#     )
#     job_results = app.read_results(
#         client,
#         job_info,
#         calculate_units=calculate_units,
#         filtered=filtered_results,
#     )
#     app.post(client, "/jobs:error_file", data=data)
#     health = app.get(client, "/health")
#     app.create_new_project(
#         client, account_id, hpc_id, f"{project_name}"
#     )
#     concept_data = app.create_new_concept(
#         client,
#         project_id,
#         title=title,
#     )
#     accounts = app.get_account_ids(token)
#     app.get_project_ids(re.escape(project_name), account_id, token)
#     created_component = app.post_component_file(client, str(filepath), component_type)
