#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(e):
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Function to display on web app /states route"""
    states_list = storage.all(State)
    return render_template('9-states.html', states=states_list, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
