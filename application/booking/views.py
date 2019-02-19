from application import app, db, login_required
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user
from datetime import datetime, date, timedelta
from application.booking.models import Booking
from application.service.models import Service
from application.worker.models import Worker
from application.customer.models import Customer
from application.booking.forms import BookingForm, UnregisteredBookingForm, BookingStatisticsForm
from application.customer.forms import NewCustomerForm
from application.booking.cal import Month_And_Year, First_And_Last, Days_of_the_Month, Date_From_String
import calendar
from calendar import monthrange

current = Month_And_Year()
daynames = ['|MO|', '|TU|', '|WE|', '|TH|', '|FR|', '|SA|', '|SU|']
req_day = 0

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
    global req_day
    form = BookingForm()
    urform = UnregisteredBookingForm()
    if req_day != 0:
        form.date.data = req_day
        urform.date.data = req_day
        req_day = 0
    year = current.get_year()
    month = current.get_month()
    days = Days_of_the_Month(year, month)
    lst = days.get_days()
    if current_user.is_authenticated:
        return render_template("booking/calendar.html", year = year, month = month , days = lst, daynames = daynames, form = form)
    else:
        return render_template("booking/unreg_calendar.html", year = year, month = month , days = lst, daynames = daynames, form = urform)

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

@app.route("/calendar/setday/<day>", methods=["POST"])
def set_day(day):
    global req_day
    times = Date_From_String(current.get_year(), current.get_month(), day)
    timestr = times.get_daytime_object()
    req_day = timestr
    return redirect(url_for("cal_index"))

@app.route("/calendar", methods=["POST"])
def booking_create():
    form = BookingForm(request.form)
    if not form.validate():
        year = current.get_year()
        month = current.get_month()
        days = Days_of_the_Month(year, month)
        lst = days.get_days()
        return render_template("booking/calendar.html", year = year, month = month , days = lst, daynames = daynames, form = form)
    else:
        dateAndTime = form.date.data
        notes = form.notes.data
        service_id = form.service.data.id
        if current_user.get_role() == "CUSTOMER":
            customer_id = Customer.query.filter_by(account_id=current_user.id).first().id
            b = Booking(notes, 0, dateAndTime, service_id, customer_id)
            db.session().add(b)
            db.session().commit()
        else:
            b = Booking(notes, 0, dateAndTime, service_id)
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
        days = Days_of_the_Month(year, month)
        lst = days.get_days()
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
        b = Booking(notes, 0, dateAndTime, service_id, customer_id)
        db.session().add(b)
        db.session().commit()
        flash('Booking successfully submitted.')
    return redirect(url_for("cal_index"))

@app.route("/bookings/statistics", methods=["GET", "POST"])
@login_required(role="ADMIN")
def booking_statistics():
    vat_for_year = Booking.total_revenue_or_vat_for_year(current.get_year(), 24)
    total_for_year = Booking.total_revenue_or_vat_for_year(current.get_year(), 0)
    if request.method == "GET":
        return render_template("booking/statistics.html", total=total_for_year, vat = vat_for_year, year=current.get_year(), form=BookingStatisticsForm())
    else:
        form = BookingStatisticsForm(request.form)  
        if not form.validate():
            return render_template("booking/statistics.html", total=total_for_year, vat = vat_for_year, year=current.get_year(), form=form)
        vat_for_year_month = Booking.total_revenue_or_vat_for_year_month(form.year.data, form.month.data, 24)
        total_for_year_month = Booking.total_revenue_or_vat_for_year_month(form.year.data, form.month.data, 0)
        ayear = form.year.data
        amonth = form.month.data
        totalBook = Booking.total_bookings_for_year_month(form.year.data, form.month.data)
        return render_template("booking/statistics.html", total=total_for_year, vat = vat_for_year, year=current.get_year(), form=BookingStatisticsForm(), ar=total_for_year_month, av=vat_for_year_month, ayear=ayear, amonth=amonth, totalBook=totalBook)

