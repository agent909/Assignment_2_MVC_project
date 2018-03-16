from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class IncubatorForm(FlaskForm):
    name = StringField('Incubator Name:', validators=[DataRequired()])
    rows = IntegerField('Rows:', validators=[DataRequired()])
    columns = IntegerField('Columns:', validators=[DataRequired()])
    submit = SubmitField('Submit')


class TrayReport(FlaskForm):
    balot = IntegerField('Balot', validators=[DataRequired()])
    freska = IntegerField('Freska:', validators=[DataRequired()])
    penoy = IntegerField('Penoy:', validators=[DataRequired()])
    echo = IntegerField('Echo:', validators=[DataRequired()])
    matra = IntegerField('Matra:', validators=[DataRequired()])
    cracked = IntegerField('Cracked:', validators=[DataRequired()])
