# Flask web app

## Setup

```bash
uv sync
```

## Run at host

```bash
export FLASK_APP=src.app
export FLASK_ENV=development
export FLASK_DEBUG=1
uv run flask run --reload
```

## Build an container

```bash
podman build -t flask_app .
podman run -p "5000:5000" localhost/flask_app:latest
```
