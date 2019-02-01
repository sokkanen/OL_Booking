from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, StringField, validators, ValidationError
from wtforms.fields.html5 import DateTimeLocalField
from datetime import datetime

def date_not_in_past(form, field):
    current = datetime.now()
    if (current > field.data):
        raise ValidationError('Please choose an upcoming date')


class BookingForm(FlaskForm):
    date = DateTimeLocalField('Date and time: ',[date_not_in_past],format='%Y-%m-%dT%H:%M')
    service = SelectField(u"Service: ", choices=[('1', 'Haravointi'), ('2', 'Imurointi'), ('2', 'Taimien istutus')])
    notes = StringField("Notes: ", [validators.Length(max=150)])

    class Meta:
        csrf = False