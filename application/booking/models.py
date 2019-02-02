from application import db
from application.models import Base

class Booking(Base):

    notes = db.Column(db.String(150), nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False)
    requested_date = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)

    def __init__(self, notes, confirmed, requested_date, customer_id, service_id):
        self.notes = notes
        self.confirmed = confirmed
        self.requested_date = requested_date
        self.done = False
        self.customer_id = customer_id
        self.service_id = service_id
        self.worker_id = 0
