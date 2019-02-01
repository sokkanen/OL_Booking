from application import db
from application.models import BaseWithName

class Customer(BaseWithName):

    email = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(144), nullable=False)
    phone = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    bookings = db.relationship('Booking', backref='customer', lazy=True)

    def __init__(self, name, email, address, phone, account_id):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.account_id = account_id