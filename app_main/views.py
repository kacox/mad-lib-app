"""
Contains routes and corresponding view functions for the default blueprint.
"""
from .default_blueprint import default

@default.route('/')
def index():
    return 'Hello World'
