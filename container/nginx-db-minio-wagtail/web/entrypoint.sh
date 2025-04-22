#!/usr/bin/env sh
set -e

DB_HOST="${POSTGRES_HOST:-postgres}"
DB_PORT="${POSTGRES_PORT:-5432}"

echo "⏳ Waiting for DB ${DB_HOST}:${DB_PORT}..."
while ! nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 1
done
echo "✅ DB is ready to connect."

echo "🔄 Run the migration ..."
uv run src/manage.py migrate --no-input

# Exec our main process (CMD)
echo "🚀 Run the server..."
exec "$@"
