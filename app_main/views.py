"""
Contains routes and corresponding view functions for the default blueprint.
"""
from .default_blueprint import default
from flask import render_template, url_for, redirect
from . import forms

@default.route('/', methods=['GET', 'POST'])
def index():
    form = forms.MadLibSelector()
    if form.validate_on_submit():
        # Successful POST request; assign user choice to variable
        choice = form.madlib_choice.data

        # redirect to choice's corresponding route
        for option in form.madlib_choice.choices:
            if option[0] == choice:
                return redirect(url_for('default.' + str(choice)))
    # form not submitted
    return render_template('main.html', title="Home", selectform=form)


@default.route('/mlib1', methods=['GET', 'POST'])
def mlib1():
    return render_template('base.html', title="Mad Lib 1", heading='Mad Lib 1')


@default.route('/mlib2', methods=['GET', 'POST'])
def mlib2():
    return render_template('base.html', title="Mad Lib 2", heading='Mad Lib 2')
