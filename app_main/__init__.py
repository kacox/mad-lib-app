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

    # attach routes and custom error pages
    from .default_blueprint import default
    app.register_blueprint(default)

    return app
