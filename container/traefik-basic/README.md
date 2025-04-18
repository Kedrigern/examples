# Podman + Traefik + Custom Nginx Example

## Overview
This example demonstrates how to run a simple static website served by a custom Nginx image behind Traefik v3.3.6 as a reverse proxy, all orchestrated using Podman‑Compose (Rootless Podman). The project includes:

- A **custom Nginx** image (based on `nginx:alpine`) that contains your HTML content and configuration.
- **Traefik v3.3.6** configured for HTTP routing and dashboard access.
- A **docker-compose.yml** file compatible with Podman‑Compose.

## Project Structure


```
.
├── docker-compose.yml
├── web
│   ├── Dockerfile
│   ├── content
│   │   └── index.html
│   └── default.conf
└── traefik-config
    ├── traefik.yml
    └── traefik_dynamic.yml
```

- **docker-compose.yml**: Defines two services: `web` (built from the custom Nginx Dockerfile) and `traefik`.
- **web/**: Contains the Dockerfile and static website content.
- **traefik-config/**: Holds the static (`traefik.yml`) and dynamic (`traefik_dynamic.yml`) configuration files for Traefik.

## Prerequisites

- Fedora 42 with Podman and Podman‑Compose installed:
  ```bash
  sudo dnf install podman podman-compose
  ```
- Allow rootless users to bind to port 80:
  ```bash
  sudo sysctl net.ipv4.ip_unprivileged_port_start=80
  echo "net.ipv4.ip_unprivileged_port_start=80" | sudo tee /etc/sysctl.d/rootless_ports.conf
  ```

## Build and Run

1. **Start the stack**  
   From the project root:
   
   ```bash
   podman-compose up -d
   ```
   Podman‑Compose will build the `web` image and start both Traefik and Nginx services.

2. **Verify running containers**  


   ```bash
   podman ps
   ```

## Usage

- **Access the website**  
  Open your browser or use `curl`:
  ```bash
  curl http://localhost
  ```
  You should see:
  ```
  Hello from Podman Nginx via custom image!
  ```

- **Access the Traefik dashboard**  
  Open:
  ```
  http://localhost/dashboard/
  ```
  This shows the Traefik UI with routers, services, and entrypoints.

## Customization

- To serve your own content, replace `web/content/index.html`.
- Adjust Nginx settings via `web/default.conf`.
- Extend Traefik routing rules in `traefik-config/traefik_dynamic.yml`.
- For HTTPS, enable the ACME provider in `traefik-config/traefik.yml` and mount a volume for `acme.json`.

## Cleanup

To stop and remove containers and networks:


```bash
podman-compose down --rmi local
```

## Troubleshooting

- **Port binding errors**: Ensure `net.ipv4.ip_unprivileged_port_start=80` is set.
- **Permission (SELinux)**: Confirm `:Z` flag is used in volume mounts within Compose.
- **Logs**: Check logs for both services:
  ```bash
  podman logs traefik
  podman logs web
  ```
