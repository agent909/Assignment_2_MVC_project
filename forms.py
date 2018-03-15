# from flask.ext.wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired



class IncubatorForm(FlaskForm):
    name = StringField('Incubator Name:', validators=[DataRequired()])
    rows = IntegerField('rows:', validators=[DataRequired()])
    column = IntegerField('columns:', validators=[DataRequired()])
    submit = SubmitField('Submit')
