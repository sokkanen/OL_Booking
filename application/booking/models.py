from application import db
from application.models import Base
from sqlalchemy.sql import text
from datetime import datetime, date, timedelta

class Booking(Base):

    notes = db.Column(db.String(150), nullable=False)
    confirmed = db.Column(db.Integer, nullable=False)
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

    @staticmethod
    def find_bookings_with_workers_and_duration(first, last):
        stmt = text("SELECT Booking.requested_date, Worker.name, Service.duration_hrs, Service.duration_mins" 
                    " FROM Booking LEFT JOIN Worker ON Worker.id = Booking.worker_id"
                    " LEFT JOIN Service ON Booking.service_id = Service.id"
                    " WHERE Booking.confirmed = 1"
                    " GROUP BY Booking.requested_date")
        res = db.engine.execute(stmt)

        lst = []
        for x in res:
            y = datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S.%f')
            if (y > first and y < last):
                y_string = y.strftime("%Y-%m-%d %H:%M")
                endtime = y + timedelta(hours=x[2]) + timedelta(minutes=x[3])
                e_string = endtime.strftime("%Y-%m-%d %H:%M")
                line = []
                line.append(y_string[8:10])
                line.append(x[1])
                line.append(y_string + " - " + e_string)
                lst.append(line)
        return lst
