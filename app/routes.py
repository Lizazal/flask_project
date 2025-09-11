from app import app
from flask import render_template


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return "Hello, world!"


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/calc/<a>/<b>')
def calc(a, b):
    try:
        return f"The sum of {a} and {b} is {int(a) + int(b)}."
    except ValueError:
        return "I can't calculate this one."


@app.route('/reverse/<text>')
def reverse(text):
    return f"{text[::-1]}"


@app.route('/reverse/')
def no_reverse():
    return "There's nothing to reverse"


@app.route('/user/<string:name>/<int:age>')
def user(name, age):
    return f"Hello, {name}. You are {age} years old."
