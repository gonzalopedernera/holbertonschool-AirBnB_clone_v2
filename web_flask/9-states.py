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
@app.route('/states_list', strict_slashes=False)
def states(id=None):
    """Function to display on web app /states route"""
    states_list = storage.all(State).values()
    return render_template('7-states_list.html', states=states_list, id=id)


@app.route('/states/<id>', strict_slashes=False)
def state_found(id):
    states_list = storage.all(State).values()
    for state in states_list:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
