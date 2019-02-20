from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, fields, validators
from wtforms.validators import EqualTo, InputRequired, ValidationError
from wtforms.fields import PasswordField
from application.account.models import Account

def validate_username(form, field):
    if Account.query.filter(Account.username == field.data).count():
        raise ValidationError('Please choose another username')

class WorkerForm(FlaskForm):
    name = StringField("Name: ", [InputRequired(), validators.Length(min=3, max=50)])
    username = StringField("Username: ", [InputRequired(), validators.Length(min=3, max=50), validate_username])
    password = PasswordField('Password: ', [InputRequired(), validators.Length(min=5, max=100), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Repeat password: ')
    role = RadioField('Choose worker role: ', choices=[('True', 'Admin'), ('False', 'Worker')], default='False')

    class Meta:
        csrf = False