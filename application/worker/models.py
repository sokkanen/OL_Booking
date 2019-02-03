from application import db
from application.models import BaseWithName

worker_service = db.Table('worker_service', 
    db.Column('worker_id', db.Integer, db.ForeignKey('worker.id'), primary_key=True),
    db.Column('service_id', db.Integer, db.ForeignKey('service.id'), primary_key=True)
)

class Worker(BaseWithName):
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    services = db.relationship('Service', secondary=worker_service, lazy='subquery',
        backref=db.backref('worker', lazy=True))

    def __init__(self, name, account_id):
        self.name = name
        self.account_id = account_id