from application import db
from application.models import Base
from sqlalchemy.sql import text
from datetime import datetime, date, timedelta
import calendar

class Booking(Base):

    notes = db.Column(db.String(150), nullable=False)
    confirmed = db.Column(db.Integer, nullable=False)
    requested_date = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)

    def __init__(self, notes, confirmed, requested_date, service_id, customer_id=None):
        self.notes = notes
        self.confirmed = confirmed
        self.requested_date = requested_date
        self.done = False
        self.customer_id = customer_id
        self.service_id = service_id

    @staticmethod
    def find_bookings_with_workers_and_duration(first, last):
        stmt = text("SELECT Booking.requested_date, Worker.name, Service.duration_hrs, Service.duration_mins" 
                    " FROM Booking LEFT JOIN Worker ON Worker.id = Booking.worker_id"
                    " LEFT JOIN Service ON Booking.service_id = Service.id"
                    " WHERE Booking.confirmed = 1"
                    " GROUP BY Booking.requested_date, Worker.name, Service.duration_hrs, Service.duration_mins")
        res = db.engine.execute(stmt)

        lst = []
        for x in res:
            time_to_string = str(x[0])
            splitted = time_to_string.split('.')
            time_to_string = splitted[0]
            y = datetime.strptime(time_to_string, "%Y-%m-%d %H:%M:%S")
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

    @staticmethod
    def find_confimed_bookings_for_worker(worker_id):
        stmt = text("SELECT * FROM Booking WHERE confirmed = 1 "
                    "AND worker_id = :x")
        res = db.engine.execute(stmt, x=worker_id)
        cbookings = []
        for result in res:
            cbookings.append(result)
        return cbookings

    @staticmethod
    def find_confirmed_bookings_for_customer(customer_id):
        stmt = text("SELECT * FROM Booking WHERE confirmed = 1"
        " AND customer_id = :x")
        res = db.engine.execute(stmt, x=customer_id)
        cbookings = []
        for result in res:
            cbookings.append(result)
        return cbookings

    @staticmethod
    def total_revenue_or_vat_for_year_month(year, month, vat):
        start = 0
        end = 0
        # kuukausinumerolla 13 ilmaistaan, että halutaan vuosituotto
        if month == 13:
            start = date(year, 1, 1)
            end = date(year, 12, 31)
        else:
            lastDay = calendar.monthrange(year, month)[1]
            start = date(year, month, 1)
            end = date(year, month, lastDay)
        stmt = text("SELECT SUM(cost_per_hour * duration_hrs) + SUM(cost_per_hour * duration_mins / 60) "
        "FROM Service JOIN Booking ON Service.id = booking.service_id"
        " WHERE Booking.requested_date > :x and Booking.requested_date < :y")
        res = db.engine.execute(stmt, x=start, y=end)
        pal = 0
        if vat == 0:
            for result in res:
                pal = result[0]
                if pal == None:
                    return 0
            return pal
        for result in res:
                pal = result[0]
                if pal == None:
                    return 0
        return pal / 100 * vat

    @staticmethod
    def total_bookings_for_year_month(year, month):
        lastDay = calendar.monthrange(year, month)[1]
        start = date(year, month, 1)
        end = date(year, month, lastDay)
        stmt = text("SELECT COUNT(id) FROM Booking WHERE Booking.requested_date > :x and Booking.requested_date < :y")
        res = db.engine.execute(stmt, x=start, y=end)
        for result in res:
            if result[0] == None:
                return 0
            return result[0]
