"""
Web forms for the application.
"""

from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class MadLibSelector(FlaskForm):
    """
    """
    madlib_choice = SelectField('Choose', choices=[('mlib1', 'Mad Lib 1'),
                                                   ('mlib2', 'Mad Lib 2')])
    submit = SubmitField('Start')


class MadLibOne(FlaskForm):
    """
    """
    pass


class MadLibTwo(FlaskForm):
    """
    """
    pass
