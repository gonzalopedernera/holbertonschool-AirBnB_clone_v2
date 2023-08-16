#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def remove_session():
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Function to display on web app /states_list route"""
    return render_template(
        '7-states_list.html', states=storage.all(State).values()
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
