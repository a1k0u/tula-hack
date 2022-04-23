import werkzeug.exceptions
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Start page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Login page')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template('registration.html', title='Registration page')


@app.route('/<path:username>')
def profile(username: str):
    return render_template('profile.html', username=username)


@app.errorhandler(404)
def page_not_found(error: werkzeug.exceptions.NotFound):
    return render_template('page404.html', title='Page not found', warning='404'), 404


if __name__ == '__main__':
    app.run()
