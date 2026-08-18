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

"""
Get Results workflow (v2 API)
==============================

This example shows how to use the v2 PyConceptEV generated client to collect
results for a local study it creates itself and export them to Excel.

The example connects to a local ConceptEV server, starting it automatically
when needed.

The study and job are deleted after their results are retrieved.
"""

# %%
# Perform required imports
# ------------------------

import time

from local_v2_study import create_local_study, submit_local_job
import matplotlib.pyplot as plt
import pandas as pd

from ansys.conceptev.core.app import get_local_client
from ansys.conceptev.core.generated.api.concept_v2 import delete_concept, get_job, get_job_file

# %%
# Inputs
# ------
# Change the following variables to match your data.

output_filename = "results.xlsx"  # Output filename for results.

# %%
# Helper functions
# ----------------


def wait_for_job(client, concept_id: str, job_id: str, poll_interval: int = 5) -> object:
    """Poll the job endpoint until it reaches a terminal state and return the record."""
    terminal_states = {"COMPLETED", "FINISHED", "FAILED", "ERROR"}
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


def get_results_for_job(client, concept_id: str, job_id: str) -> dict:
    """Wait for a local job and return its results."""
    job = wait_for_job(client, concept_id, job_id)

    results = None
    if job.status in {"COMPLETED", "FINISHED"} and job.files:
        results = get_job_file.sync(
            concept_id=concept_id,
            job_id=job.id,
            file_id=job.files[0].id,
            client=client,
        )

    return {
        "concept_id": concept_id,
        "concept_name": "Local Results Study",
        "job_id": job.id,
        "results": results,
    }


# %%
# Create a local study and collect results
# -----------------------------------------

with get_local_client() as client:
    concept_id = None
    try:
        concept_id, requirement_id, architecture_id = create_local_study(
            client, "Local Results Study"
        )
        job = submit_local_job(
            client,
            concept_id,
            requirement_id,
            architecture_id,
            "Local Results Job",
        )
        all_results = [get_results_for_job(client, concept_id, job.id)]
    finally:
        if concept_id is not None:
            delete_concept.sync(id=concept_id, client=client)

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
