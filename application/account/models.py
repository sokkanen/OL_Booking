from application import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    linked_worker = db.relationship('Worker', backref='account', uselist=False, lazy=True)
    linked_customer = db.relationship('Customer', backref='account', uselist=False, lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.customer_id = customer_id
        self.worker_id = worker_id

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True