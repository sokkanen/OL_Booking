from application import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    duration_hrs = db.Column(db.Integer)
    duration_mins = db.Column(db.Integer)
    cost_per_hour = db.Column(db.Integer)

    def __init__(self, name, duration_hrs, duration_mins, cost_per_hour):
        self.name = name
        self.duration_hrs = duration_hrs
        self.duration_mins = duration_mins
        self.cost_per_hour = cost_per_hour