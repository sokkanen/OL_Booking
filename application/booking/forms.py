from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, StringField, validators, ValidationError
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.service.models import Service
from datetime import datetime

def date_not_in_past(form, field):
    current = datetime.now()
    if (current > field.data):
        raise ValidationError('Please choose an upcoming date')

def service_query():
    return Service.query

class BookingForm(FlaskForm):
    date = DateTimeLocalField('Date and time: ',[date_not_in_past],format='%Y-%m-%dT%H:%M')
    service = QuerySelectField(query_factory=service_query, allow_blank=True, get_label='name')
    notes = StringField("Notes: ", [validators.Length(max=150)])

    class Meta:
        csrf = False