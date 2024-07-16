from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ApiForm(FlaskForm):
    endpoint = StringField('API Endpoint', 
                            validators=[DataRequired()])
    submit = SubmitField('Test')

class ScanForm(FlaskForm):
    ip = StringField('IP Adress or Range',
                       validators=[DataRequired()])
    submit = SubmitField('Scan')