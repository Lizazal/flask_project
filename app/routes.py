from app import app


@app.route('/')
def hello_flask():
    return "Hello, Flask!"


@app.route('/hello')
def hello():
    return "Hello, world!"


@app.route('/info')
def info():
    return "This is an informational page."


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
