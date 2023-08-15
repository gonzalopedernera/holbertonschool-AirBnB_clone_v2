#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask

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


@app.route("pyhton/<text>", strict_slashes=False)
def python_is_fun(text="is cool"):
    """Function for display on web python/<text> route"""
    if text:
        formated_text = text.replace("_", " ")
        return f"Python {formated_text}"
    else:
        return f"Pyhton {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
