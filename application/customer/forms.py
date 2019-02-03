from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, EqualTo
from wtforms.widgets import PasswordInput


class NewCustomerForm(FlaskForm):
    username = StringField("Username: ", [InputRequired()])
    password = StringField('Password:', [InputRequired(), validators.Length(min=5, max=100), EqualTo('confirm_password', message='Passwords must match')], widget=PasswordInput(hide_value=False))
    confirm_password = StringField('Repeat Password:', widget=PasswordInput(hide_value=False))
    name = StringField("Name: ", [InputRequired(), validators.Length(min=1, max=50)])
    email = EmailField('Email: ', [InputRequired(), validators.DataRequired(), validators.Email()])
    address = StringField("Address : ", [InputRequired(), validators.Length(min=5, max=100)])
    phone = StringField("Phone : ", [InputRequired(), validators.Length(min=5, max=20)])

    class Meta:
        csrf = False