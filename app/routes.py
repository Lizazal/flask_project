from random import choice

from app import app
from flask import render_template, request, redirect, url_for


JOKES = [
    "I told my computer I needed a break, and it said: 'No problem, I’ll go to sleep.'",
    "Why do Java developers wear glasses? Because they don't C#.",
    "There are 10 types of people: those who understand binary and those who don't.",
    "My code doesn’t work, I have no idea why. My code works, I have no idea why."
]


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


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")  # Получаем имя из формы
        email = request.form.get("email")  # Получаем email из формы
        color = request.form.get("color")
        profession = request.form.get("profession")
        hobbies = request.form.getlist("hobbies")
        level = request.form.get("level")
        superpower = request.form.get("superpower")

        errors = []
        if not name:
            errors.append("We can't process the form without your name, Mr. Anonymous! 😶‍🌫️")
        if not email:
            errors.append("Without mail our pigeon won't fly! 🕊️")
        if errors:
            return render_template("form.html", errors=errors)

        joke = choice(JOKES)
        return render_template(
            "result.html",
            name=name, email=email, color=color,
            profession=profession, hobbies=hobbies, level=level,
            superpower=superpower, joke=joke
        )
    else:
        return redirect(url_for("form"))  # Если запрос GET, возвращаем на форму
