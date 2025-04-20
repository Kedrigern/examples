import os
import psycopg


def get_conn_params() -> dict[str, str]:
    return {
        "dbname": os.getenv("POSTGRES_DB"),
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "host": os.getenv("POSTGRES_HOST", "postgres"),
        "port": os.getenv("POSTGRES_PORT", 5432),
    }


def get_db_info() -> dict[str, str]:
    """
    Connects to PostgreSQL and returns a dictionary with:
      - version: the database version
      - table_count: number of tables in the public schema
      - uptime: server uptime
    """
    info: dict = {"version": None, "table_count": None, "uptime": None}
    try:
        with psycopg.connect(**get_conn_params()) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version()")
                info["version"] = cur.fetchone()[0]

                cur.execute(
                    "SELECT count(*) FROM information_schema.tables WHERE table_schema = 'public';"
                )
                info["table_count"] = cur.fetchone()[0]

                cur.execute(
                    "SELECT date_trunc('second', now() - pg_postmaster_start_time()) AS uptime;"
                )
                info["uptime"] = str(cur.fetchone()[0])
    except Exception as e:
        error_msg = f"Error connecting to DB: {e}"
        info = {"version": error_msg, "table_count": error_msg, "uptime": error_msg}
    return info
