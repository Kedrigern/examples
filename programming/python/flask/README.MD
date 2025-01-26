# Flask

Flask je microframework pro webové aplikace v Pythonu.

## Anatomie aplikace

Flask aplikace může být jeden soubor, ale v realu se většinou používá celý python modul, mnohdy i se submoduly. Minimální `__init__.py`:

```python3
import os

from flask import Flask

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    return app
```

Jedná se o [Application Factories](http://flask.pocoo.org/docs/1.0/patterns/appfactories/), `flask` automaticky hledá v modulu funkci `create_app`, která vrací app.

## Tutorial:Flaskr

Spustit jako modul:

```bash
FLASK_APP=flaskr FLASK_ENV=development python3 -m flask init-db
FLASK_APP=flaskr FLASK_ENV=development python3 -m flask run
```

Spustit přes flask cli s virtualenv:

```bash
python3 -m venv venv      # příprava virtualenv
. venv/bin/activate       # aktivace virtualenv
pip install -e .          # install requirments
export FLASK_APP=flaskr   # definice, která aplikace se má pustit
export FLASK_ENV=development
flask init-db             # inicializace DB (zde SQLite)
flask run                 # spuštění aplikace
```