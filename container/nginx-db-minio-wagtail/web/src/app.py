from flask import Flask, render_template
import os
from src.services.db import get_db_info
from src.services.storage import get_minio_info, ensure_logo

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