FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends curl \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml ./

RUN uv sync

COPY static ./static
COPY src ./src

EXPOSE 5000

CMD ["uv", "run", "flask", "run", "--host", "0.0.0.0", "--port", "5000"]
