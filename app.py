import sqlite3
import os
from flask import Flask, render_template as rt, request, g, flash, \
    abort, redirect, url_for, make_response, render_template
from db import DataBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from user_login import UserLogin

import werkzeug.exceptions

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


login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    db = get_db()
    database: DataBase = DataBase(db)
    return UserLogin().from_db(user_id, database)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/')
def index():
    db = get_db()
    database: DataBase = DataBase(db)
    return render_template('index.html', title='Start page')


@app.route('/login', methods=['POST', "GET"])
def login():
    db = get_db()
    database: DataBase = DataBase(db)
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')

        user = database.get_user_by_name(name)
        if user and check_password_hash(user['password'], password):
            return redirect(url_for('profile'))
        else:
            flash('Неверный пароль!')
    return render_template("login.html")


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    db = get_db()
    database: DataBase = DataBase(db)
    if request.method == "POST":
        if len(request.form['username'] + request.form['password']) > 8 and \
                request.form['password'] == request.form['password2']:
            password_hash = generate_password_hash(request.form['password'])
            res = database.add_user(request.form['username'], password_hash)
            if res:
                flash("Вы успешно зарегистрированы", "success")
                return redirect(url_for('login'))
            else:
                flash("Ошибка при добавлении в БД", "error")
        else:
            flash("Неверно заполнены поля", "error")
    return render_template('registration.html', title='Registration page')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')


@app.errorhandler(404)
def page_not_found(error: werkzeug.exceptions.NotFound):
    return render_template('page404.html', title='Page not found', warning='404'), 404


if __name__ == '__main__':
    app.run()
