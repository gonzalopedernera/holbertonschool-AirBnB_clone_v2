#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Function for display on web start"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function for display on web hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Function for display on web c/<text> route"""
    formated_text = text.replace("_", " ")
    return f"C {formated_text}"


@app.route("/python/", strict_slashes=False, defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_is_fun(text):
    """Function for display on web python/<text> route"""
    formated_text = text.replace("_", " ")
    return f"Python {formated_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Function to display on web app number/<n> only if n is an int"""
    if type(n) == int:
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Function to display template on web app number_template/<n>"""
    if type(n) == int:
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Function to display template on web app /number_odd_or_even/<n>"""
    if type(n) == int:
        return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
