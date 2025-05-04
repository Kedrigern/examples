from flask import Flask, render_template
import os
from dotenv import load_dotenv
from src.services.db import get_db_info
from src.services.storage import get_minio_info, ensure_logo

if not os.getenv("MINIO_BUCKET"):
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

REQUIRED = ["POSTGRES_USER", "POSTGRES_PASSWORD",
            "MINIO_ENDPOINT_URL", "MINIO_ROOT_USER",
            "MINIO_ROOT_PASSWORD", "MINIO_BUCKET"]

missing = [v for v in REQUIRED if not os.getenv(v)]
if missing:
    raise RuntimeError(f"Chybí proměnné prostředí: {', '.join(missing)}")


app = Flask(__name__)

@app.route("/")
def index():
    env_vars = {
        "FLASK_ENV":       os.getenv("FLASK_ENV", "-not set–"),
        "FLASK_DEBUG":     os.getenv("FLASK_DEBUG", "–not set–"),
        "POSTGRES_DB":     os.getenv("POSTGRES_DB", "–not set–"),
        "MINIO_ROOT_USER": os.getenv("MINIO_ROOT_USER", "–not set–"),
        "MINIO_BUCKET":    os.getenv("MINIO_BUCKET", "–not set–")
    }
    db_info = get_db_info()
    minio_info = get_minio_info()
    logo_url = ensure_logo(os.getenv('MINIO_BUCKET'))

    return render_template(
        "index.html",
        env_vars=env_vars,
        db_info=db_info,
        minio_info=minio_info,
        logo_url=logo_url
    )