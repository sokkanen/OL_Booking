from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, fields, validators
from wtforms.validators import EqualTo, InputRequired
from wtforms.fields import PasswordField

class WorkerForm(FlaskForm):
    name = StringField("Name: ", [InputRequired(), validators.Length(min=1, max=100)])
    password = PasswordField('Password: ', [InputRequired(), validators.Length(min=5, max=100), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Repeat password: ')
    role = RadioField('Choose worker role: ', choices=[('True', 'Admin'), ('False', 'Worker')], default='False')

    class Meta:
        csrf = False