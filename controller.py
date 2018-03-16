from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from forms import IncubatorForm

import model

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/dbase'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'family'

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/incubators', methods=('POST', 'GET'))
def incubators():
    form = IncubatorForm()
    my_incubators = model.get_incubators()
    if form.validate_on_submit():
        if model.add_incubator(form):
            flash("Incubator has successfuly been created.")
        else:
            flash("Error Occured, Incubator not created")
        return redirect(url_for('incubators'))
    return render_template('incubators.html', form=form, my_incubators=my_incubators)


@app.route('/incubators/1')
def incubator():
    # my_incubator = model.FetchIncubator(incub_id)
    # return render_template('incubate.html', my_incubator=my_incubator)
    return render_template('incubate.html')


if __name__ == '__main__':
    app.run(debug=True)
