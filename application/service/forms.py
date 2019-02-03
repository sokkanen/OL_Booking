from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from wtforms.validators import InputRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.worker.models import Worker

class ServiceForm(FlaskForm):
    name = StringField('Service: ', [InputRequired(), validators.Length(max=100)])
    duration_hrs = IntegerField('Duration (hours): ', [InputRequired(), validators.NumberRange(min=0, max=12)])
    duration_mins = IntegerField('Duration (minutes): ', [InputRequired(), validators.NumberRange(min=0, max=59)])
    cost_per_hour = IntegerField('Cost per Hour: ', [InputRequired(), validators.NumberRange(min=0, max=999)])

    class Meta:
        csrf = False


def worker_query():
    return Worker.query

class Service_Worker_Form(FlaskForm):
    workers_list = QuerySelectField(query_factory=worker_query, get_label='name')

    class Meta:
        csrf = False