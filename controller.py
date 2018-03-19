from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from forms import IncubatorForm, TrayReport

import model

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/dbase'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'family'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

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


@app.route('/incubators/<int:incubator_id>')
def incubate(incubator_id):
    tray_report = TrayReport()
    my_incubator = model.fetch_incubator(incubator_id)
    total_eggs = model.get_incubator_eggs(incubator_id)

    return render_template('incubate.html', my_incubator=my_incubator, total_eggs=total_eggs[0],
                           trays=total_eggs[1], tray_report=tray_report)


if __name__ == '__main__':
    app.run(debug=True)


