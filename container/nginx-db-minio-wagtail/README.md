# Podman‑Compose Multi‑Service Example

## Overview

This example shows how to run a simple stack on Fedora 42 with Podman‑Compose (rootless):

- **nginx-proxy**: NGINX reverse proxy exposing port 80.
- **webapp**: NGINX backend serving static content on its default port 80 (internal only).
- **minio**: MinIO object storage (API on 9000, console on 9001).
- **minio-init**: One‑shot init service that creates a bucket if absent.
- **postgres**: PostgreSQL 17 database (internal only).

All services share a private network; only the proxy is exposed externally.

## Prerequisites

1. **Fedora 42** with Podman and Podman‑Compose:

   ```bash
   sudo dnf install podman podman-compose
   ```

2. Allow rootless Podman to bind port 80:

   ```bash
   sudo sysctl net.ipv4.ip_unprivileged_port_start=80
   echo "net.ipv4.ip_unprivileged_port_start=80" | sudo tee /etc/sysctl.d/rootless_ports.conf
   ```

3. Create a `.env` file:

   ```dotenv
   MINIO_ROOT_USER=minio
   MINIO_ROOT_PASSWORD=minio123
   MINIO_BUCKET=mybucket
   POSTGRES_USER=user
   POSTGRES_PASSWORD=pass
   POSTGRES_DB=appdb
   ```

## Usage

1. **Start the stack**

   ```bash
   podman-compose up -d
   ```

2. **Verify services**  

   ```bash
   podman ps
   ```

## Access

- **Webapp**:  

  ```bash
  curl http://localhost
  ```

- **MinIO API** (list buckets):

  ```bash
  curl http://localhost/minio/
  ```

- **MinIO Console UI**: open in browser:

  ```txt
  http://localhost/minio/ui/
  ```

- **PostgreSQL** (internal): connect from another service by hostname `postgres:5432`.

## Debugging

- Check logs:

  ```bash
  podman logs nginx-proxy
  podman logs minio
  podman logs minio-init
  podman logs postgres
  ```

- Test internal connectivity:

  ```bash
  podman exec -it nginx-proxy curl -I http://minio:9000/
  podman exec -it nginx-proxy curl -I http://minio:9001/
  podman exec -it nginx-proxy curl -I http://webapp:80/
  ```

## Cleanup

```bash
podman-compose down --rmi local
```
