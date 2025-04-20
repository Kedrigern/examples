import os
import psycopg
from flask import Flask, render_template

app = Flask(__name__)

def get_pg_info() -> dict[str,str|None]:
    conn_params = {
        "dbname": os.getenv("POSTGRES_DB"),
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "host": os.getenv("POSTGRES_HOST", "postgres"),
        "port": os.getenv("POSTGRES_PORT", 5432),
    }
    info: dict[str,str|None] = {
        "version": None,
        "table_count": None,
        "uptime": None,
    }

    try:
        with psycopg.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version()")
                info["version"] = cur.fetchone()[0]

                cur.execute(
                    """
                    SELECT count(*)
                    FROM information_schema.tables
                    WHERE table_schema = 'public';
                    """
                )
                info["table_count"] = cur.fetchone()[0]

                cur.execute(
                    """
                    SELECT date_trunc('second', now() - pg_postmaster_start_time())
                    AS uptime;
                    """
                )
                info["uptime"] = str(cur.fetchone()[0])
    except Exception as e:
        error_msg = f"Error connecting to DB: {e}"
        info = {"version": error_msg, "table_count": error_msg, "uptime": error_msg}

    return info

@app.route("/")
def index():
    env_vars = {
        "FLASK_ENV":       os.getenv("FLASK_ENV", "-not set–"),
        "FLASK_DEBUG":     os.getenv("FLASK_DEBUG", "–not set–"),
        "POSTGRES_DB":     os.getenv("POSTGRES_DB", "–not set–"),
        "MINIO_ROOT_USER": os.getenv("MINIO_ROOT_USER", "–not set–"),
        "MINIO_BUCKET":    os.getenv("MINIO_BUCKET", "–not set–")
    }
    return render_template("index.html", env_vars=env_vars, db_info=get_pg_info())
