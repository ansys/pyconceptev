#!/bin/bash
# Post-create setup for the pyconceptev devcontainer.
# Poetry is pre-installed in the Dockerfile image layer.
set -e

echo "========================================"
echo "pyconceptev DevContainer Setup"
echo "========================================"

echo "Checking toolchain..."
python3 --version
poetry --version
docker --version

echo ""
echo "Configuring Poetry..."
# Store the virtualenv inside the project directory so VS Code discovers it automatically
poetry config virtualenvs.in-project true

if [ -z "${CONCEPTEV_PASSWORD}" ]; then
    echo "WARNING: CONCEPTEV_PASSWORD is not set."
    echo "Integration and e2e tests will fail without it."
    echo "Set it in your Codespace secrets at: https://github.com/settings/codespaces"
else
    echo "CONCEPTEV_PASSWORD is configured."
fi

if [ -z "${LICENSE_SERVER}" ]; then
    echo "WARNING: LICENSE_SERVER is not set."
    echo "E2E tests (optiSLang) will not run without it."
else
    echo "LICENSE_SERVER is configured (ANSYSLMD_LICENSE_FILE will be 1055@${LICENSE_SERVER})."
fi

echo ""
echo "Installing project dependencies (dev + test groups)..."
poetry install --with dev,tests

echo ""
echo "Installing pre-commit hooks..."
poetry run pre-commit install

cat << 'EOF'

DevContainer is ready!

Run tests:
  poetry run pytest tests/unit              # unit tests, no secrets needed
  poetry run pytest tests/integration       # live API, needs CONCEPTEV_PASSWORD
  bash .devcontainer/run-e2e.sh             # optiSLang e2e, needs all secrets

EOF
