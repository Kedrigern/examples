import functools, os, sys
import flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import current_app

from cislovky.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/', methods=('GET',))
def home():
    instance_path = current_app.instance_path
    cfg = current_app.config
    dirs = os.listdir( current_app.instance_path )
    pyversion = sys.version
    flaskversion = flask.__version__
    return render_template('home/home.html', in_path=instance_path, cfg=cfg, dirs=dirs, pyversion=pyversion, flaskversion=flaskversion)


@bp.route('/all', methods=('GET',))
def all():
    db = get_db()
    cislovky = db.execute(
        "SELECT id, rome, cs, en"
        " FROM cislovky"
        " ORDER BY id ASC"
    ).fetchall()
    return render_template('home/all.html', cislovky=cislovky)


@bp.route('/en', methods=('GET',))
def en():
    db = get_db()
    cislovky = db.execute(
        "SELECT id, en"
        " FROM cislovky"
        " ORDER BY id ASC"
    ).fetchall()
    return render_template('home/en.html', cislovky=cislovky)


@bp.route('/cs', methods=('GET',))
def cs():
    db = get_db()
    cislovky = db.execute(
        "SELECT id, cs"
        " FROM cislovky"
        " ORDER BY id ASC"
    ).fetchall()
    return render_template('home/cs.html', cislovky=cislovky)

