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

# Note: Docker and Docker Compose are provided by the docker-in-docker devcontainer feature.
