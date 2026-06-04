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
Bulk Job Submit
===============

Example script to bulk-submit jobs to the local ConceptEV v2 API.

This example reads a list of component combinations from a CSV file and, for
each combination, creates a new concept on the server, assembles it with the
chosen components, and submits a job.  The resulting concept IDs and job IDs
are written to an Excel file for later result retrieval.

The combinations CSV must contain a column per component role matching the
``component_order`` dictionary below, with component names as values.

The ``base_concept_id`` is an existing concept on the server whose components
will be referenced when building each variant.
"""

# %%
# Perform Required imports
# ------------------------

import datetime

import pandas as pd

from ansys.conceptev.core.app import get_local_client
from ansys.conceptev.core.generated.api.concept_v2 import (
    create_concept,
    create_concept_part,
    delete_concept,
    get_concept,
    create_job,
)
from ansys.conceptev.core.generated.models import (
    ArchitectureInput,
    ConceptInput,
)
from ansys.conceptev.core.generated.models.job_request import JobRequest

# %%
# Set up inputs
# -------------
# Change the following variables to match your data.
# The current filename for combinations can be used as an example.
# The ``base_concept_id`` must be the ID of an existing concept on the server
# that contains the components referenced in the combinations file.
# ``component_order`` maps CSV column names → architecture field names.

filename = "resources/combinations.csv"  # See example file for format.
base_concept_id = "2465235f-ad2e-4923-9125-e2e69ccf5816"  # Existing concept on the server.
component_order = {
    "front_transmission_id": "Front Transmission",
    "front_motor_id": "Front Motor",
    "rear_transmission_id": "Rear Transmission",
    "rear_motor_id": "Rear Motor",
    "battery_id": "Battery",
}


# %%
# Helper: build a component name → ID map from a concept
# -------------------------------------------------------


def get_component_id_map(concept) -> dict[str, str]:
    """Return {component_name: component_id} from a ConceptOutput."""
    result = {}
    if concept.components:
        for comp in concept.components:
            result[comp.name] = comp.id
    return result


# %%
# Load the base concept and validate the combinations file
# --------------------------------------------------------

combinations = pd.read_csv(filename, na_filter=False).to_dict("records")

# Validate that every required column exists.
required_columns = set(component_order.values())
file_columns = set(combinations[0].keys()) if combinations else set()
assert required_columns <= file_columns, (
    f"Missing columns in combinations file: {required_columns - file_columns}"
)

with get_local_client() as client:
    base_concept = get_concept.sync(id=base_concept_id, client=client)
    base_component_map = get_component_id_map(base_concept)

    # Validate that every component name in the file exists in the base concept.
    combo_component_names = {v for row in combinations for v in row.values() if v}
    assert combo_component_names <= set(base_component_map.keys()), (
        f"Unknown components in combinations: "
        f"{combo_component_names - set(base_component_map.keys())}"
    )

    # Identify the requirement IDs to run (all requirements from the base concept).
    requirement_ids = [r.id for r in (base_concept.requirements or [])]

    # %%
    # Submit jobs for each combination
    # ---------------------------------
    # For each row in the combinations CSV:
    # 1. Create a new concept.
    # 2. Add an architecture referencing the chosen components.
    # 3. Submit a job.

    created_designs = []
    for combo in combinations:
        title = (
            f"FM_{combo['Front Motor']}_RM_{combo['Rear Motor']}_"
            f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )
        try:
            # 1. Create a new concept.
            concept = create_concept.sync(
                client=client,
                body=ConceptInput(name=title),
            )
            concept_id = concept.id

            # 2. Build the architecture referencing the chosen component IDs.
            arch_kwargs = {
                field: base_component_map[combo[label]]
                for field, label in component_order.items()
                if combo.get(label)
            }
            # battery_id is required by ArchitectureInput.
            battery_id = arch_kwargs.pop("battery_id")
            created_arch = create_concept_part.sync(
                id=concept_id,
                part_type="architecture",
                client=client,
                body=ArchitectureInput(
                    battery_id=battery_id,
                    number_of_front_wheels=base_concept.architectures[0].number_of_front_wheels
                    if base_concept.architectures
                    else 2,
                    number_of_front_motors=base_concept.architectures[0].number_of_front_motors
                    if base_concept.architectures
                    else 1,
                    number_of_rear_wheels=base_concept.architectures[0].number_of_rear_wheels
                    if base_concept.architectures
                    else 2,
                    number_of_rear_motors=base_concept.architectures[0].number_of_rear_motors
                    if base_concept.architectures
                    else 0,
                    **arch_kwargs,
                ),
            )

            # 3. Submit a job.
            job_record = create_job.sync(
                concept_id=concept_id,
                client=client,
                body=JobRequest(
                    name=f"bulk_job: {title}",
                    requirement_ids=requirement_ids,
                    architecture_id=created_arch.id,
                ),
            )
            print(f"Submitted job {job_record.id} for concept {concept_id} ({title})")

            created_designs.append(
                {
                    "Title": title,
                    "Concept ID": concept_id,
                    "Architecture ID": created_arch.id,
                    "Job ID": job_record.id,
                }
            )
        except Exception as err:
            print(f"Failed for combination {combo}: {err}")
            continue

# %%
# Save the list of created designs to a file
# ------------------------------------------

all_results = pd.DataFrame(created_designs)
all_results.to_excel("created_designs.xlsx", index=False)
print(f"Saved {len(created_designs)} designs to created_designs.xlsx")

# %%
# Clean up: delete all created concepts
# --------------------------------------
#
# .. warning::
#    This permanently removes all concepts created above from the server.
#    Comment out this section if you want to keep them.

with get_local_client() as client:
    for design in created_designs:
        delete_concept.sync(id=design["Concept ID"], client=client)
        print(f"Deleted concept {design['Concept ID']}")
    print("Cleanup complete.")
