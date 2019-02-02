from application import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime, date
from application.booking.models import Booking
from application.booking.forms import BookingForm
from application.booking.cal import Month_And_Year
import calendar

current = Month_And_Year()
daynames = ['|MO|', '|TU|', '|WE|', '|TH|', '|FR|', '|SA|', '|SU|']

@app.route("/bookings", methods=["GET"])
@login_required
def booking_index():
    ### Haettava käyttäjä
    return render_template("booking/list.html", bookings = Booking.query.all())

@app.route("/bookings/<booking_id>/", methods=["POST"])
@login_required
def booking_set_confirmed(booking_id):
    b = Booking.query.get(booking_id)
    b.confirmed = True
    db.session().commit()

    return redirect(url_for("booking_index"))

@app.route("/bookings/del/<booking_id>/", methods=["POST"])
@login_required
def booking_remove(booking_id):
    b = Booking.query.get(booking_id)
    db.session.delete(b)
    db.session().commit()
    
    return redirect(url_for("booking_index"))

@app.route("/calendar")
def cal_index():
    year = current.get_year()
    month = current.get_month()
    lst = []
    for day in list(calendar.monthcalendar(year, month)):
        lst.append(day)
    return render_template("booking/calendar.html", year = year, month = month , days = lst, daynames = daynames, form = BookingForm())

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
    form = BookingForm(request.form)
    if not form.validate():
        year = current.get_year()
        month = current.get_month()
        lst = []
        for day in list(calendar.monthcalendar(year, month)):
            lst.append(day)
        return render_template("booking/calendar.html", year = year, month = month , days = lst, daynames = daynames, form = form)
    else:
        dateAndTime = form.date.data
        notes = form.notes.data
        if (current_user.is_authenticated):
            customer_id = current_user.id
        else:
            customer_id = 0
        b = Booking(notes, False, dateAndTime, customer_id)
        db.session().add(b)
        db.session().commit()
        flash('Booking successfully submitted.')

    return redirect(url_for("cal_index"))