FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY pyproject.toml ./

RUN uv sync

COPY src ./src

EXPOSE 5000

CMD ["uv", "run", "flask", "run", "--host", "0.0.0.0", "--port", "5000"]
