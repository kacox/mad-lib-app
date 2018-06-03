"""
Init for the app_main package.

This package controls the creation of a Flask application instance, its
configurations, and any Flask extensions.

This package also houses all static files, templates, and other code pertaining
to the application.
"""
from flask import Flask

def create_app:
    app = Flask(__name__)
    return app
