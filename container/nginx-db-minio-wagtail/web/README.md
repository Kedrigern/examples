# Wagtailo web app

## Setup

```bash
uv sync
```

## Run at host

## Build an container

```bash
podman build -t wagtail_app .
podman run -p "8000:8000" localhost/wagtail_app:latest
```
