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

"""Shared skip helpers for known, tracked integration-test issues.

Deliberately NOT named ``conftest`` or placed in a package-less directory that
would collide with another same-named module: ``tests/integration/conftest.py``
and ``tests/e2e/conftest.py`` are both imported as a top-level module literally
named ``conftest`` under pytest's default (package-less) import mode, so
``from conftest import X`` resolves ambiguously once both directories are
collected in the same session — this module exists to avoid that collision.
"""

import pytest

# ---------------------------------------------------------------------------
# KNOWN ISSUE (2026-10-27): the ConceptEV API rejects the ANSYS_UAT_PAT identity
# with a 401 "Key Not Found" — the ConceptEV API hasn't migrated to the new UAT
# environment/identity setup yet, so it doesn't recognize tokens issued through the
# new PAT-based auth flow. This is an environment-migration gap on the ConceptEV
# side, not a pyconceptev bug (confirmed: the same token works fine against the OCM API).
#
# TO RE-ENABLE: once the ConceptEV API has migrated to the new UAT environment,
# delete `_KNOWN_PROVISIONING_ISSUE_DETAIL`/`_skip_if_known_provisioning_issue` below
# and their call sites — the tests will then run and assert normally again.
# ---------------------------------------------------------------------------
_KNOWN_PROVISIONING_ISSUE_DETAIL = "Key Not Found"


def _skip_if_known_provisioning_issue(exc: Exception) -> None:
    """Skip (not fail) on the known ConceptEV API / UAT migration gap.

    Matches only the exact known error detail, so unrelated regressions still fail.
    """
    if _KNOWN_PROVISIONING_ISSUE_DETAIL in str(exc):
        pytest.skip(
            "Known issue: the ConceptEV API hasn't migrated to the new UAT environment "
            f"yet, so it rejects the ANSYS_UAT_PAT identity with a 401 "
            f"'{_KNOWN_PROVISIONING_ISSUE_DETAIL}'. See tests/integration/_known_issues.py "
            "for how to re-enable."
        )
    raise exc
