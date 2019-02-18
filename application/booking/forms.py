from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, StringField, IntegerField, validators, ValidationError
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import EmailField
from application.service.models import Service
from wtforms.validators import InputRequired
from datetime import datetime

def date_not_in_past(form, field):
    current = datetime.now()
    if (current > field.data):
        raise ValidationError('Please choose an upcoming date')

def service_query():
    return Service.query

class BookingForm(FlaskForm):
    date = DateTimeLocalField('Date and time: ',[InputRequired(), date_not_in_past],format='%Y-%m-%dT%H:%M')
    service = QuerySelectField(query_factory=service_query, get_label='name')
    notes = StringField("Notes: ", [validators.Length(max=150)])

    class Meta:
        csrf = False

class UnregisteredBookingForm(FlaskForm):
    date = DateTimeLocalField('Date and time: ',[InputRequired(), date_not_in_past],format='%Y-%m-%dT%H:%M')
    service = QuerySelectField(query_factory=service_query, get_label='name')
    notes = StringField("Notes: ", [validators.Length(max=150)])
    name = StringField("Name: ", [InputRequired(), validators.Length(min=1, max=50)])
    email = EmailField('Email: ', [InputRequired(), validators.DataRequired(), validators.Email()])
    address = StringField("Address : ", [InputRequired(), validators.Length(min=5, max=100)])
    phone = StringField("Phone : ", [InputRequired(), validators.Length(min=5, max=20)])

    class Meta:
        csrf = False

class BookingStatisticsForm(FlaskForm):
    year = IntegerField("Year", [InputRequired(), validators.NumberRange(min=2018, max=2100)])
    month = IntegerField("Month", [InputRequired(), validators.NumberRange(min=1, max=12)])
    
    class Meta:
        csrf = False