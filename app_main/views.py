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
    form = forms.MadLibOne()
    if form.validate_on_submit():
        # Successful POST request; take data
        adj1 = form.adj1.data
        adj2 = form.adj2.data
        verb1 = form.verb1.data
        adj3 = form.adj3.data
        adj4 = form.adj4.data
        entry_list = [adj1, adj2, verb1, adj3, adj4]

        # Show filled out mad lib
        return render_template('madlib1-completed.html', entry_list=entry_list)

    # Form not submitted    
    return render_template('madlib1.html', title="Mad Lib 1",
                            heading='Mad Lib 1', form=form)


@default.route('/mlib2', methods=['GET', 'POST'])
def mlib2():
    return render_template('base.html', title="Mad Lib 2", heading='Mad Lib 2')
