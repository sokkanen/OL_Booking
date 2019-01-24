from application import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    notes = db.Column(db.String(144), nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False)
    requested_date = db.Column(db.DateTime, nullable=False)

    # Käyttäjä ja työntekijä tullaan toteuttamaan viiteavaimilla...

    def __init__(self, notes, confirmed, requested_date):
        self.notes = notes
        self.confirmed = confirmed
        self.requested_date = requested_date
        self.done = False
