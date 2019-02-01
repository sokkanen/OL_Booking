from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField("Name: ", [InputRequired()])
    password = PasswordField("Password: ", [InputRequired()])

    class Meta:
        csrf = False