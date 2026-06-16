#!/bin/bash
# Run e2e tests inside the optiSLang Docker container, mirroring the CI job exactly.
#
# Prerequisites:
#   - CONCEPTEV_PASSWORD Codespace secret is set
#   - LICENSE_SERVER Codespace secret is set
#   - Your GitHub account has read access to ghcr.io/ansys/optislang
#
# Usage:
#   bash .devcontainer/run-e2e.sh              # run all e2e tests
#   bash .devcontainer/run-e2e.sh -k test_name  # filter by test name
set -e

OPTISLANG_IMAGE="ghcr.io/ansys/optislang:25.2.0-jammy"

# Validate required secrets
if [ -z "${CONCEPTEV_PASSWORD}" ]; then
    echo "ERROR: CONCEPTEV_PASSWORD is not set. Add it to your Codespace secrets at:" >&2
    echo "  https://github.com/settings/codespaces" >&2
    exit 1
fi

if [ -z "${LICENSE_SERVER}" ]; then
    echo "ERROR: LICENSE_SERVER is not set. Add it to your Codespace secrets at:" >&2
    echo "  https://github.com/settings/codespaces" >&2
    exit 1
fi

# Authenticate to GHCR using the Codespace-provided token and the authenticated user
echo "${GITHUB_TOKEN}" | docker login ghcr.io -u "${GITHUB_ACTOR}" --password-stdin

echo "Pulling ${OPTISLANG_IMAGE} ..."
docker pull "${OPTISLANG_IMAGE}"

echo "Running e2e tests ..."
docker run --rm \
    -v "$(pwd):/workspace" \
    -w /workspace \
    -e CONCEPTEV_PASSWORD="${CONCEPTEV_PASSWORD}" \
    -e ANSYSLMD_LICENSE_FILE="1055@${LICENSE_SERVER}" \
    -e PYOPTISLANG_DISABLE_OPTISLANG_OUTPUT=true \
    -e PYCONCEPTEV_SETTINGS="tests/e2e/config.toml" \
    -e POETRY_VIRTUALENVS_CREATE=false \
    "${OPTISLANG_IMAGE}" \
    bash -c "pip install poetry --quiet && poetry install --with tests --no-interaction && poetry run pytest tests/e2e $*"
