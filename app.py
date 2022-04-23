import os
import sqlite3

import werkzeug.exceptions
from flask import Flask, render_template, g, url_for, session, request, redirect, flash

from db import *
from dotenv import dotenv_values

CONFIG = dotenv_values(".env")
DATABASE = CONFIG['DATABASE']
DEBUG = CONFIG['DEBUG']
SECRET_KEY = CONFIG['SECRET_KEY']

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(
    dict(
        DATABASE=os.path.join(
            app.root_path, 'db.db'
        )
    )
)


def connect_db():
    connect = sqlite3.connect(app.config['DATABASE'])
    connect.row_factory = sqlite3.Row
    return connect


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/')
def index():
    db = get_db()
    database: DataBase = DataBase(db)
    return render_template('index.html', title='Start page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    db = get_db()
    database: DataBase = DataBase(db)
    return render_template('login.html', title='Login page')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    db = get_db()
    database: DataBase = DataBase(db)
    return render_template('registration.html', title='Registration page')


@app.route('/profile/<path:username>')
def profile(username: str):
    return render_template('profile.html', username=username)


@app.errorhandler(404)
def page_not_found(error: werkzeug.exceptions.NotFound):
    return render_template('page404.html', title='Page not found', warning='404'), 404


if __name__ == '__main__':
    app.run()
