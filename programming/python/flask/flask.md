
# Flask

## Quickstart

Naklonujeme si a spustíme velmi pěkný aplikační skeleton:

```bash
git clone https://github.com/realpython/flask-skeleton.git
cd flask-skeleton
pip3 install -r requirements.txt
python3 manage.py test
python3 manage.py create_db
python3 manage.py runserver
```
Ten má strukturu:

```
├── LICENSE
├── manage.py
├── project
│   ├── client
│   │   ├── static
│   │   │   ├── main.css
│   │   │   └── main.js
│   │   └── templates
│   │       ├── _base.html
│   │       ├── errors
│   │       │   ├── 401.html
│   │       │   ├── 403.html
│   │       │   ├── 404.html
│   │       │   └── 500.html
│   │       ├── footer.html
│   │       ├── header.html
│   │       ├── main
│   │       │   ├── about.html
│   │       │   └── home.html
│   │       └── user
│   │           ├── login.html
│   │           ├── members.html
│   │           └── register.html
│   ├── __init__.py
│   ├── server
│   │   ├── config.py
│   │   ├── dev.sqlite
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── user
│   │       ├── forms.py
│   │       ├── __init__.py
│   │       └── views.py
│   └── tests
│       ├── base.py
│       ├── helpers.py
│       ├── __init__.py
│       ├── test__config.py
│       ├── test_main.py
│       └── test_user.py
├── README.md
└── requirements.txt
```

## Jinja

LOOP - rekurze

```jinja
{% set outer_loop = loop %}
{% for key in category recursive %}
	{{ key }}
	{{ loop( key.children ) }}
{% endfor %}
```

## Libtree

Obecná práce nad stromy za využití PostgreSQL. [libtree][] 

## Odkazy

- app [skeleton][]


[libtree]: https://github.com/conceptsandtraining/libtree
[skeleton]: https://github.com/realpython/flask-skeleton
[zodb]: ZODB.org
