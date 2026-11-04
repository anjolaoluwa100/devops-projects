# Week 2: Containerize a 3-Tier App

A Notes API (Python Flask) and a PostgreSQL database behind an nginx reverse proxy, run together with Docker Compose.

## Architecture

## Setup

### Prerequisites

- Ubuntu 24.04 (I used a Multipass VM on macOS)
- Git
- Docker Engine and the Docker Compose plugin (install steps below)

### Install Docker

These steps follow Docker's official guide for Ubuntu. For other systems, see the [Docker install docs](https://docs.docker.com/engine/install/).

1. Add Docker's GPG key, so apt can verify Docker's packages:

```bash
sudo apt update
sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

2. Add Docker's apt repository, then refresh the package list:

```bash
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF
sudo apt update
```

3. Install Docker Engine, the CLI, containerd, Buildx and Compose:

```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

4. Check that the Docker service is running:

```bash
sudo systemctl status docker
```

5. Let your user run Docker without `sudo`, then log out and back in so the change applies:

```bash
sudo usermod -aG docker $USER
```

6. Test the install:

```bash
docker run --rm hello-world
docker compose version
```

### Run the app

## Environment variables

## API endpoints
All requests go through nginx on port 8080 (for example `curl localhost:8080/notes`).

- `GET /health`: returns 200 when the API can reach the database, 503 when it can't.
- `GET /notes`: returns every note as a JSON list.
- `POST /notes`: saves a note sent as JSON, like `{"text": "my first note"}`, and returns it with status 201. Without `text` it returns 400.

## Design decisions

## Tests and evidence

## Problems and troubleshooting

## What I learned
