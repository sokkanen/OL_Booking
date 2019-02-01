from application import db
from application.models import Base

class Account(Base):

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    linked_worker = db.relationship('Worker', backref='account', uselist=False, lazy=True)
    linked_customer = db.relationship('Customer', backref='account', uselist=False, lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True