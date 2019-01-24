from application import app, db
from flask import render_template, request, redirect, url_for
from datetime import datetime, date
from application.booking.models import Booking
import calendar

# Kalenteritoiminnallisuus omaan luokkaansa.

class Month_And_Year:
    def __init__(self):
        self.year = datetime.now().year
        self.month = datetime.now().month

    def previous_month(self):
        if self.month == 1:
            self.year -=1
            self.month = 12
        else:
            self.month -=1

    def next_month(self):
        if self.month == 12:
            self.year +=1
            self.month = 1
        else:
            self.month +=1

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

current = Month_And_Year()

@app.route("/bookings", methods=["GET"])
def booking_index():
    return render_template("booking/list.html", bookings = Booking.query.all())

@app.route("/bookings/<booking_id>/", methods=["POST"])
def booking_set_confirmed(booking_id):
    b = Booking.query.get(booking_id)
    b.confirmed = True
    db.session().commit()

    return redirect(url_for("booking_index"))

@app.route("/bookings/del/<booking_id>/", methods=["POST"])
def booking_remove(booking_id):
    b = Booking.query.get(booking_id)
    db.session.delete(b)
    db.session().commit()
    
    return redirect(url_for("booking_index"))

@app.route("/calendar")
def cal_index():
    year = current.get_year()
    month = current.get_month()
    daynames = ['|MO|', '|TU|', '|WE|', '|TH|', '|FR|', '|SA|', '|SU|']
    lst = []
    for day in list(calendar.monthcalendar(year, month)):
        lst.append(day)
    return render_template("booking/calendar.html", year = year, month = month , days = lst, daynames = daynames)

@app.route("/calendar/prev/", methods=["POST"])
def prev_month():
    current.previous_month()
    return redirect(url_for("cal_index"))

@app.route("/calendar/next/", methods=["POST"])
def next_month():
    current.next_month()
    return redirect(url_for("cal_index"))

@app.route("/calendar", methods=["POST"])
def booking_create():
    req_time = datetime.strptime(request.form.get("time"), '%Y-%m-%dT%H:%M')
    notes = request.form.get("notes")
    b = Booking(notes, False, req_time)
    db.session().add(b)
    db.session().commit()

    return redirect(url_for("cal_index"))