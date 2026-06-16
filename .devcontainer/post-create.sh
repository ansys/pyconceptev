#!/bin/bash
# Post-create setup for the pyconceptev devcontainer.
# Poetry is pre-installed via the devcontainer feature; this script installs
# project dependencies and sets up the local venv and pre-commit hooks.
set -e

# Store the virtualenv inside the project directory so VS Code discovers it automatically
poetry config virtualenvs.in-project true

# Install project + dev + test dependencies (doc group is optional and heavy, skip by default)
poetry install --with dev,tests

# Wire up pre-commit hooks for code style checks on commit
poetry run pre-commit install

echo ""
echo "pyconceptev dev environment ready."
echo ""
echo "Secrets required (set in Codespace settings before creating the Codespace):"
echo "  CONCEPTEV_PASSWORD  - ConceptEV test account password"
echo "  LICENSE_SERVER      - Ansys license server hostname (for e2e tests)"
echo ""
echo "Run tests:"
echo "  poetry run pytest tests/unit                     # unit tests, no secrets needed"
echo "  poetry run pytest tests/integration              # live API, needs CONCEPTEV_PASSWORD"
echo "  bash .devcontainer/run-e2e.sh                    # optiSLang e2e, needs all secrets"
