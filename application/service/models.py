from application import db
from application.models import BaseWithName

class Service(BaseWithName):
    
    duration_hrs = db.Column(db.Integer)
    duration_mins = db.Column(db.Integer)
    cost_per_hour = db.Column(db.Integer)
    bookings = db.relationship('Booking', backref='service', lazy=True)

    def __init__(self, name, duration_hrs, duration_mins, cost_per_hour):
        self.name = name
        self.duration_hrs = duration_hrs
        self.duration_mins = duration_mins
        self.cost_per_hour = cost_per_hour