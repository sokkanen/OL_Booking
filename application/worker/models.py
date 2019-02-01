from application import db
from application.models import BaseWithName

class Worker(BaseWithName):
    
    isAdmin = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __init__(self, name, isAdmin, account_id):
        self.name = name
        self.isAdmin = isAdmin
        self.account_id = account_id