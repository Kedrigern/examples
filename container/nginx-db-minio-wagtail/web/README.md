# Minopy: Wagtail Deployment with Podman

This repository demonstrates how to deploy a Wagtail 6.4.1 (Django 5.2) site using Podman 5.4. The stack is composed of multiple rootless containers, all hidden behind an NGINX reverse proxy, and includes:

nginx (reverse proxy): Exposed on port 80 to route requests to the appropriate service

web (Wagtail app): Your Django/Wagtail project running under Uvicorn (uv 0.5.5) in a Python 3.12 environment

postgres:17: PostgreSQL database for content storage

minio:latest: MinIO object storage for media files (API on 9000, console UI on 9001)

minio-init: One‑time service to create the MinIO bucket if it doesn’t exist

All containers share a private Podman network; only the nginx proxy is published on the host.

## Prerequisites

Make sure you can bind to port 80 as a rootless user:

```bash
sudo sysctl net.ipv4.ip_unprivileged_port_start=80  # apply immediately until next reboot
echo "net.ipv4.ip_unprivileged_port_start=80" | sudo tee /etc/sysctl.d/rootles
```

> Note: The first command applies the change immediately (but resets on reboot), while the second writes a configuration file to make the setting permanent across reboots.

## Configuration

1. Environment variables: Create a `.env` file in the repository root with the following values:

    ```yml
    MINIO_ROOT_USER=minio
    MINIO_ROOT_PASSWORD=minio123
    MINIO_BUCKET=mybucket
    POSTGRES_USER=user
    POSTGRES_PASSWORD=pass
    POSTGRES_DB=appdb
    ```

2. NGINX proxy:

   - Development: `proxy/dev.conf`
   - Production: `proxy/prod.conf`

3. Compose files:

   - Base (default):       `docker-compose.yml`
   - Development override: `docker-compose.dev.yml`
   - Production override:  `docker-compose.prod.yml`

4. Wagtail settings (in `web/src/minopy/settings`):

   - `base.py`: shared settings, including MinIO storage backend
   - `dev.py`: debug mode, console email backend
   - `production.py`: production settings (DEBUG=False)

## Development Setup

1. Start all services:

   ```bash
   podman-compose -f docker-compose.yml -f docker-compose.dev.yml build web
   podman-compose -f docker-compose.yml -f docker-compose.dev.yml up -d
   ```

2. Create a superuser (if needed):

   `podman-compose exec web uv run src/manage.py createsuperuser`

The Wagtail admin should now be available at `http://localhost/admin/`.

## Production Setup

1. Ensure .env is configured with production-grade secrets and hosts.
2. Start services using the production compose file:

    ```bash
    podman-compose -f docker-compose.yml -f docker-compose.prod.yml build web
    podman-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
    ```

## Persistent Volumes & Backups

In this stack, critical data is stored in Podman volumes for durability across container restarts and host reboots. You should regularly back up these volumes to prevent data loss.

### Volumes Used

- PostgreSQL data: stored in the postgres_data volume
- MinIO data: stored in the minio_data volume

### Backup Strategies

1. PostgreSQL: use pg_dump to export the database to a SQL file:

    ```bash
    podman run --rm --network container:postgres \  # connect to the postgres container
        -v $(pwd):/backup \                         # mount host dir for dump
        postgres:17 pg_dump -h localhost -U $POSTGRES_USER $POSTGRES_DB > backup_$(date +%F).sql
    ```

2. MinIO Backup

   - Use the MinIO Client (mc) to mirror the bucket to local filesystem:

      ```bash
      mc alias set local http://localhost:9000 $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD
      mc mirror local/$MINIO_BUCKET /backups/minio/$(date +%F)
      ```

   - Alternatively, copy the raw volume data:

    ```bash
    podman run --rm -v minio_data:/data -v $(pwd)/backups:/backup alpine \  # raw copy
        sh -c "tar czf /backup/minio_data_$(date +%F).tgz -C /data ."
    ```

## Debugging & Logs

- Inspect logs of containers
- Test internal connectivity via the proxy:

    ```bash
    podman exec -it nginx curl -I http://minio:9000/
    podman exec -it nginx curl -I http://web:8000/
    ```

## Cleanup

To tear down the environment and remove locally built images:

   ```bash
   podman-compose down --rmi local
   ```