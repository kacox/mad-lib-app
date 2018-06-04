"""
Default blueprint for the application.
"""
from flask import Blueprint

default = Blueprint('default', __name__)

from . import views
