"""
Contains routes and corresponding view functions for the default blueprint.
"""
from .default_blueprint import default
from flask import render_template

@default.route('/')
def index():
    return render_template('index.html', title="Home")
