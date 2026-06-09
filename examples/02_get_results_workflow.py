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
"""
Get Results workflow
====================

This example shows how to use the v2 PyConceptEV client to submit jobs for a
list of concept IDs loaded from a CSV file and then collect and export the
results to Excel.

The concept IDs are provided in ``resources/design_instance_ids.csv``.

.. warning::
    Assumes a front and rear motor architecture.
    Assumes a specific drive cycle result is available.
    Assumes the first completed job in each concept is the result we want.
"""

# %%
# Perform required imports
# ------------------------

import json
import time

import matplotlib.pyplot as plt
import pandas as pd

from ansys.conceptev.core.app import get_local_client
from ansys.conceptev.core.generated.api.concept_v2 import (
    create_job,
    get_concept,
    get_job,
    list_jobs,
)
from ansys.conceptev.core.generated.models.job_request import JobRequest

# %%
# Inputs
# ------
# Change the following variables to match your data.

get_results_off_server = True  # Generates an output file that can be read later.
output_filename = "results.xlsx"  # Output filename for results.

# %%
# Helper functions
# ----------------


def wait_for_job(client, concept_id: str, job_id: str, poll_interval: int = 5) -> object:
    """Poll the job endpoint until it reaches a terminal state and return the record."""
    terminal_states = {"COMPLETED", "FAILED", "ERROR"}
    while True:
        job = get_job.sync(
            concept_id=concept_id,
            job_id=job_id,
            client=client,
        )
        if job.status in terminal_states:
            return job
        print(f"  Job {job_id} status: {job.status} — waiting {poll_interval}s…")
        time.sleep(poll_interval)


def get_results_for_concept(client, concept_id: str) -> dict:
    """Return results for the first completed job of a concept."""
    concept = get_concept.sync(id=concept_id, client=client)

    jobs = list_jobs.sync(
        concept_id=concept_id, client=client
    )
    if not jobs:
        raise RuntimeError(f"No jobs found for concept {concept_id}")

    # Use the first job; wait if still running.
    job = wait_for_job(client, concept_id, jobs[0].id)

    results = None
    if job.status == "COMPLETED" and job.files:
        import httpx as _httpx  # noqa: PLC0415

        results_url = job.files[0].path
        results = _httpx.get(results_url).json()

    return {
        "concept_id": concept_id,
        "concept_name": concept.name,
        "job_id": job.id,
        "results": results,
    }


# %%
# Load concept IDs and collect results
# ------------------------------------

concept_ids_df = pd.read_csv("resources/design_instance_ids.csv")
concept_ids = concept_ids_df["design_instance_id"].tolist()

if get_results_off_server:
    with get_local_client() as client:
        all_results = [get_results_for_concept(client, cid) for cid in concept_ids]

    with open("project_results.json", "w") as f:
        json.dump(all_results, f)
else:
    with open("project_results.json") as f:
        all_results = json.load(f)

# %%
# Build output DataFrame and export to Excel
# ------------------------------------------

output_rows = []
for result in all_results:
    if result["results"] is None:
        continue
    row = {
        "Concept ID": result["concept_id"],
        "Concept Name": result["concept_name"],
        "Job ID": result["job_id"],
    }
    # Extend here to extract specific result fields, for example:
    # row["total_tractive_power"] = result["results"][0]["requirement"]["total_tractive_power"]
    output_rows.append(row)

df = pd.DataFrame(output_rows)
print(df)

if output_rows:
    plt.figure()
    plt.bar(df["Concept Name"], range(len(df)))
    plt.xlabel("Concept Name")
    plt.ylabel("Index")
    plt.tight_layout()
    plt.show()

df.to_excel(output_filename, index=False)
print(f"Results written to {output_filename}")
