"""
Web forms for the application.
"""

from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class MadLibSelector(FlaskForm):
    """
    """
    madlib_choice = SelectField('Choose', choices=[('mlib1', 'Mad Lib 1'),
                                                   ('mlib2', 'Mad Lib 2')])
    submit = SubmitField('Start')


class MadLibOne(FlaskForm):
    """
    """
    adj1 = StringField('Adjective 1', validators=[DataRequired()])
    adj2 = StringField('Adjective 2', validators=[DataRequired()])
    verb1 = StringField('Verb', validators=[DataRequired()])
    adj3 = StringField('Adjective 3', validators=[DataRequired()])
    adj4 = StringField('Adjective 4', validators=[DataRequired()])
    submit = SubmitField('Create Mad Lib')


class MadLibTwo(FlaskForm):
    """
    """
    adj1 = StringField('An adjective', validators=[DataRequired()])
    name = StringField("A Man's name", validators=[DataRequired()])
    adj2 = StringField('An adjective', validators=[DataRequired()])
    place = StringField('A formal place', validators=[DataRequired()])
    place2 = StringField('A place', validators=[DataRequired()])
    number = IntegerField('Whole number', validators=[DataRequired()])
    foodstuff = StringField('A foodstuff', validators=[DataRequired()])
    object1 = StringField('An object', validators=[DataRequired()])
    submit = SubmitField('Create Mad Lib')
