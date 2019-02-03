from application import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime, date, timedelta
from application.booking.models import Booking
from application.service.models import Service
from application.worker.models import Worker
from application.customer.models import Customer
from application.booking.forms import BookingForm
from application.customer.forms import NewCustomerForm
from application.booking.cal import Month_And_Year, First_And_Last
import calendar
from calendar import monthrange

current = Month_And_Year()
daynames = ['|MO|', '|TU|', '|WE|', '|TH|', '|FR|', '|SA|', '|SU|']

@app.route("/bookings", methods=["GET"])
@login_required
def booking_index():
    cbookings = Booking.query.filter_by(confirmed=1).all()
    bookings = Booking.query.filter_by(confirmed=0).all()
    return render_template("booking/list.html", bookings = bookings, cbookings = cbookings, services = Service.query.all(), workers = Worker.query.all(), customers = Customer.query.all())

@app.route("/bookings/<booking_id>/", methods=["POST"])
@login_required
def booking_set_confirmed(booking_id):
    b = Booking.query.get(booking_id)
    w_id = Worker.query.filter_by(name=request.form['assign']).first().id
    b.confirmed = 1
    b.worker_id = w_id
    db.session().commit()
    return redirect(url_for("booking_index"))

@app.route("/bookings/del/<booking_id>/", methods=["POST"])
@login_required
def booking_remove(booking_id):
    b = Booking.query.get(booking_id)
    db.session.delete(b)
    db.session().commit()
    flash("Booking successfully removed")
    
    return redirect(url_for("booking_index"))

@app.route("/calendar")
def cal_index():
    year = current.get_year()
    month = current.get_month()
    dates = First_And_Last(year, month)
    first = dates.get_first()
    last = dates.get_last()
    lst = []
    books = Booking.find_bookings_with_workers_and_duration(first, last)
    for week in list(calendar.monthcalendar(year, month)):
        newweek = []
        for day in week:
            newday = []
            newday.append(day)
            for book in books:
                if str(day) == book[0]:
                    if (book[1] == None):
                        newday.append("U/K: " + book[2])
                    else:
                        newday.append(book[1] + ": "+ book[2])
            newday.append("No reservations")
            newweek.append(newday)
        lst.append(newweek)
    if (current_user.is_authenticated):
        return render_template("booking/calendar.html", year = year, month = month , days = lst, daynames = daynames, form = BookingForm())
    else:
        cform = NewCustomerForm()
        return render_template("booking/unreg_calendar.html", year = year, month = month , days = lst, daynames = daynames, form = BookingForm(), cform = cform)

@app.route("/calendar/prev/", methods=["POST"])
def prev_month():
    current.previous_month()
    return redirect(url_for("cal_index"))

@app.route("/calendar/next/", methods=["POST"])
def next_month():
    current.next_month()
    return redirect(url_for("cal_index"))

@app.route("/calendar/now/", methods=["POST"])
def current_time():
    current.now()
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
        service_id = form.service.data.id
        if (current_user.is_authenticated):
            customer_id = Customer.query.filter_by(account_id=current_user.id).first().id
        else:
            name = request.form['name']
            email = request.form['email']
            address = request.form['address']
            phone = request.form['phone']
            c = Customer(name, email, address, phone, 0)
            db.session().add(c)
            db.session().commit()
            customer_id = Customer.query.filter_by(name=name).first().id
        b = Booking(notes, False, dateAndTime, customer_id, service_id)
        db.session().add(b)
        db.session().commit()
        flash('Booking successfully submitted.')

    return redirect(url_for("cal_index"))