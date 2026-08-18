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
Bulk Job Submit (v2 API)
========================

Example script to bulk-submit jobs to a local ConceptEV v2 API.

This example creates local studies with varying vehicle masses and submits a
job for each. The resulting concept IDs and job IDs are written to an Excel
file.
"""

# %%
# Perform Required imports
# ------------------------

import datetime

from local_v2_study import create_local_study, submit_local_job
import pandas as pd

from ansys.conceptev.core.app import get_local_client
from ansys.conceptev.core.generated.api.concept_v2 import delete_concept

# %%
# Set up inputs
# -------------
# Change these masses to define the local studies to submit.
vehicle_masses = [1800.0, 2200.0]

with get_local_client() as client:
    # %%
    # Submit jobs for each local study
    # ---------------------------------

    created_designs = []
    for index, mass in enumerate(vehicle_masses, start=1):
        title = f"Local Bulk Study {index}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        try:
            concept_id, requirement_id, architecture_id = create_local_study(
                client, title, mass=mass
            )
            job_record = submit_local_job(
                client,
                concept_id,
                requirement_id,
                architecture_id,
                f"Local Bulk Job {index}",
            )
            print(f"Submitted job {job_record.id} for concept {concept_id} ({title})")

            created_designs.append(
                {
                    "Title": title,
                    "Concept ID": concept_id,
                    "Architecture ID": architecture_id,
                    "Job ID": job_record.id,
                }
            )
        except Exception as err:
            print(f"Failed to submit local study {index}: {err}")
            continue

    # %%
    # Clean up
    # --------
    # Delete the studies before exiting the client context. This is required
    # when ``get_local_client`` started an in-memory local server.

    for design in created_designs:
        delete_concept.sync(id=design["Concept ID"], client=client)
        print(f"Deleted concept {design['Concept ID']}")
    print("Cleanup complete.")

# %%
# Save the list of created designs to a file
# ------------------------------------------

all_results = pd.DataFrame(created_designs)
all_results.to_excel("created_designs.xlsx", index=False)
print(f"Saved {len(created_designs)} designs to created_designs.xlsx")
