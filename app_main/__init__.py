"""
Init for the app_main package.

This package controls the creation of a Flask application instance, sets its
configurations, blueprint, and any Flask extensions.

This package also houses all static files, templates, and other code pertaining
to the application.
"""
from flask import Flask

def create_app():
    # create app instance
    app = Flask(__name__)

    # change to environment variable later
    app.config['SECRET_KEY'] = 'a_tough_to_guess_string'

    # white space control
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    # attach routes
    from .default_blueprint import default
    app.register_blueprint(default)

    return app
