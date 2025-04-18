# NGINX Reverse Proxy with Internal NGINX Webapp

## Overview
This example demonstrates how to run two NGINX containers on Podman‑Compose:
- **proxy**: An NGINX reverse proxy exposed to the host on port 80.
- **web**: A backend NGINX server serving static content on its default port 80, only accessible internally.

Both services are placed on a private network so that only the proxy is reachable from outside.

## Project Structure
```
.
├── docker-compose.yml
├── proxy
│   └── default.conf
└── web
    └── index.html
```

- **docker-compose.yml**: Defines `proxy` and `web` services and the shared network.
- **proxy/default.conf**: NGINX reverse proxy configuration.
- **web/index.html**: Static HTML content served by the backend.

## Prerequisites
- **Fedora 42** with Podman and Podman‑Compose installed:
  ```bash
  sudo dnf install podman podman-compose
  ```
- Allow rootless Podman users to bind to port 80:
  ```bash
  sudo sysctl net.ipv4.ip_unprivileged_port_start=80
  echo "net.ipv4.ip_unprivileged_port_start=80" | sudo tee /etc/sysctl.d/rootless_ports.conf
  ```
  This enables listening on port 80 without root privileges.

## Configuration

### proxy/default.conf
```nginx
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://web:80;
        proxy_set_header Host             $host;
        proxy_set_header X-Real-IP        $remote_addr;
        proxy_set_header X-Forwarded-For  $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### docker-compose.yml
```yaml
version: "3.9"

services:
  proxy:
    image: nginx:alpine
    container_name: nginx-proxy
    ports:
      - "80:80"
    volumes:
      - ./proxy/default.conf:/etc/nginx/conf.d/default.conf:Z
    networks:
      - internal_net

  web:
    image: nginx:alpine
    container_name: webapp
    volumes:
      - ./web/index.html:/usr/share/nginx/html/index.html:Z
    expose:
      - "80"
    networks:
      - internal_net

networks:
  internal_net:
    driver: bridge
```

## Build and Run
Start the stack in detached mode:
```bash
podman-compose up -d
```
Verify the containers are running:
```bash
podman ps
```

## Usage
- **Access the website**  
  ```bash
  curl http://localhost
  ```
  → Should return the content of `web/index.html`.

## Debugging & Troubleshooting
1. **Inspect logs**
   ```bash
   podman logs nginx-proxy
   podman logs webapp
   ```
2. **Test internal connectivity from proxy**
   ```bash
   podman exec -it nginx-proxy curl -I http://web:80
   ```
3. **Test backend directly**
   ```bash
   podman exec -it webapp curl -I http://localhost:80
   ```
4. **Check network**
   ```bash
   podman network inspect internal_net
   ```

## Cleanup
To stop and remove containers and networks:
```bash
podman-compose down --rmi local
```
