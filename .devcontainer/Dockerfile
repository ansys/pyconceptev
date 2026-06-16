FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

# The Python devcontainer base image ships with the Yarn apt repository.
# Its GPG key (62D54FD4003F6525) has expired/rotated which causes apt-get update
# to fail inside devcontainer feature installation scripts.
# Remove Yarn's apt source before any feature or package installation runs.
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends make curl ca-certificates \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Install Poetry directly in the image so it is always on PATH.
# Pinned to match the version used in CI (poetry==2.4.1 is latest stable).
RUN pip install --no-cache-dir "poetry==2.4.1" \
    && poetry --version

# Install the gh CLI so developers can trigger and watch GitHub Actions runs
# from inside the Codespace (e.g. gh workflow run tests-manual.yml --ref <branch>).
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
        | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
        > /etc/apt/sources.list.d/github-cli.list \
    && apt-get update && apt-get install -y --no-install-recommends gh \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
    && gh --version

# Note: Docker and Docker Compose are provided by the docker-in-docker devcontainer feature.
