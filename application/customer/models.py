from application import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    name = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(144), nullable=False)
    phone = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __init__(self, name, email, address, phone, account_id):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.account_id = account_id