FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

# The Python devcontainer base image ships with the Yarn apt repository.
# Its GPG key (62D54FD4003F6525) has expired/rotated and causes `apt-get update`
# to fail inside devcontainer feature installation scripts.
# We only need Python + Docker for this project, so remove Yarn's apt source.
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    /etc/apt/keyrings/yarnkey.gpg \
    /usr/share/keyrings/yarnkey.gpg 2>/dev/null; \
    apt-get clean
