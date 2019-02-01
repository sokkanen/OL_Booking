from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    name = StringField("Name: ", [InputRequired()])
    password = PasswordField("Password: ", [InputRequired()])

    class Meta:
        csrf = False