from application import app, db, login_required
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user
from datetime import datetime, date, timedelta
from application.booking.models import Booking
from application.service.models import Service
from application.worker.models import Worker
from application.customer.models import Customer
from application.booking.forms import BookingForm, UnregisteredBookingForm
from application.customer.forms import NewCustomerForm
from application.booking.cal import Month_And_Year, First_And_Last
import calendar
from calendar import monthrange

current = Month_And_Year()
daynames = ['|MO|', '|TU|', '|WE|', '|TH|', '|FR|', '|SA|', '|SU|']

@app.route("/bookings", methods=["GET"])
@login_required(role="ANY")
def booking_index():
    if current_user.get_role() == "WORKER":
        aid = current_user.get_id()
        worker_id = Worker.query.filter_by(account_id = aid).first().id
        cbookings = Booking.find_confimed_bookings_for_worker(worker_id)
        bookings = []
        return render_template("booking/list.html", bookings = bookings, cbookings = cbookings, services = Service.query.all(), workers = Worker.query.all(), customers = Customer.query.all())
    
    if current_user.get_role() == "CUSTOMER":
        aid = current_user.get_id()
        customer_id = Customer.query.filter_by(account_id = aid).first().id
        cbookings = Booking.find_confirmed_bookings_for_customer(customer_id)
        bookings = []
        return render_template("booking/list.html", bookings = bookings, cbookings = cbookings, services = Service.query.all(), workers = Worker.query.all(), customers = Customer.query.all())
    
    cbookings = Booking.query.filter_by(confirmed=1).all()
    bookings = Booking.query.filter_by(confirmed=0).all()
    return render_template("booking/list.html", bookings = bookings, cbookings = cbookings, services = Service.query.all(), workers = Worker.query.all(), customers = Customer.query.all())

@app.route("/bookings/<booking_id>/", methods=["POST"])
@login_required(role="ADMIN")
def booking_set_confirmed(booking_id):
    b = Booking.query.get(booking_id)
    w_id = Worker.query.filter_by(name=request.form['assign']).first().id
    b.confirmed = 1
    b.worker_id = w_id
    db.session().commit()
    flash("Booking assigned and confirmed.")
    return redirect(url_for("booking_index"))

@app.route("/bookings/del/<booking_id>/", methods=["POST"])
@login_required(role="ADMIN")
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
                        newday.append("Ex-worker: " + book[2])
                    else:
                        newday.append(book[1] + ": "+ book[2])
            newday.append("No reservations")
            newweek.append(newday)
        lst.append(newweek)
    if current_user.is_authenticated:
        return render_template("booking/calendar.html", year = year, month = month , days = lst, daynames = daynames, form = BookingForm())
    else:
        cform = NewCustomerForm()
        return render_template("booking/unreg_calendar.html", year = year, month = month , days = lst, daynames = daynames, form = UnregisteredBookingForm())

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
                            newday.append("Ex-worker: " + book[2])
                        else:
                            newday.append(book[1] + ": "+ book[2])
                newday.append("No reservations")
                newweek.append(newday)
            lst.append(newweek)
        return render_template("booking/calendar.html", year = year, month = month , days = lst, daynames = daynames, form = form)
    else:
        dateAndTime = form.date.data
        notes = form.notes.data
        service_id = form.service.data.id
        customer_id = Customer.query.filter_by(account_id=current_user.id).first().id
        b = Booking(notes, 0, dateAndTime, customer_id, service_id)
        db.session().add(b)
        db.session().commit()
        flash('Booking successfully submitted.')
    return redirect(url_for("cal_index"))

@app.route("/calendar/urb", methods=["POST"])
def unreg_booking_create():
    form = UnregisteredBookingForm(request.form)
    if not form.validate():
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
                            newday.append("Ex-worker: " + book[2])
                        else:
                            newday.append(book[1] + ": "+ book[2])
                newday.append("No reservations")
                newweek.append(newday)
            lst.append(newweek)
        return render_template("booking/unreg_calendar.html", year = year, month = month , days = lst, daynames = daynames, form = form)
    else:
        dateAndTime = form.date.data
        notes = form.notes.data
        service_id = form.service.data.id
        name = form.name.data
        email = form.email.data
        address = form.address.data
        phone = form.phone.data
        c = Customer(name, email, address, phone)
        db.session().add(c)
        db.session().commit()
        customer_id = Customer.query.filter(Customer.name == name).first().id
        b = Booking(notes, 0, dateAndTime, customer_id, service_id)
        db.session().add(b)
        db.session().commit()
        flash('Booking successfully submitted.')
    return redirect(url_for("cal_index"))