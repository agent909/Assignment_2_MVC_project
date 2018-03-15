from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from forms import IncubatorForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/dbase'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SECRET_KEY']='family'

db = SQLAlchemy(app)

import model

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/incubators', methods=('POST','GET'))
def incubators():
    form = IncubatorForm()
    my_incubators=model.GetIncubators()
    if form.validate_on_submit():
        if model.AddIncubator(form):
            flash("Incubator has successfuly been created.")
        return redirect(url_for('incubators'))
    return render_template('incubators.html', form=form, my_incubators=my_incubators)


if __name__=='__main__':
    app.run(debug=True)
