from application import app, db, bcrypt
from flask import render_template, request, redirect, url_for, flash
from datetime import datetime, date
from flask_login import login_required
from application.worker.models import Worker
from application.service.models import Service
from application.account.models import Account
from application.booking.models import Booking
from application.worker.forms import WorkerForm
from application.service.forms import ServiceForm, Service_Worker_Form

@app.route("/worker", methods=["GET"])
@login_required
def worker_index():
    return render_template("worker/list.html", workers = Worker.query.all(), services = Service.query.all(), accounts = Account.query.all(), wform = WorkerForm(), sform = ServiceForm(), swform = Service_Worker_Form())

@app.route("/worker/<worker_id>/", methods=["POST"])
@login_required
def worker_modify(worker_id):
    w = Worker.query.get(worker_id)
    a = Account.query.get(w.account_id)
    if a.role == 'Admin':
        a.role = 'Worker'
    else:
        a.role = 'Admin'
    db.session().add(a)
    db.session().commit()
    flash("Role changed")
    return redirect(url_for("worker_index"))

@app.route("/worker/del/<worker_id>/", methods=["POST"])
@login_required
def worker_delete(worker_id):
    w = Worker.query.get(worker_id)
    w_id = worker_id
    db.session.delete(w)
    db.session().commit()
    flash("Worker successfully removed.")
    return redirect(url_for("worker_index"))

@app.route("/worker", methods=["POST"])
@login_required
def worker_create():
    form = WorkerForm(request.form)
    if not form.validate():
        return render_template("worker/list.html", workers = Worker.query.all(), services = Service.query.all(), wform = form, sform = ServiceForm(), swform = Service_Worker_Form())
    
    pwhash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    username = form.username.data
    isAdmin = form.role.data
    role = ''
    if isAdmin == "True":
        role = 'Admin'
    else:
        role = 'Worker'
    account = Account(username, pwhash, role)
    db.session().add(account)
    db.session().commit()
    account_id = Account.query.filter_by(username=form.username.data).first().id
    name = form.name.data
    worker = Worker(name, account_id)
    db.session().add(worker)
    db.session().commit()
    return redirect(url_for("worker_index"))

@app.route("/worker/assign/<service_id>/", methods=["POST"])
@login_required
def worker_assign(service_id):
    form = Service_Worker_Form(request.form)
    w = form.workers_list.data
    s = Service.query.get(service_id)
    w.services.append(s)
    db.session.commit()
    return redirect(url_for("worker_index"))

@app.route("/worker/add_service", methods=["POST"])
@login_required
def service_create():
    form = ServiceForm(request.form)
    if not form.validate():
        return render_template("worker/list.html", workers = Worker.query.all(), services = Service.query.all(), wform = WorkerForm(), sform = form, swform = Service_Worker_Form())
    name = form.name.data
    duration_hrs = form.duration_hrs.data
    duration_mins = form.duration_mins.data
    cost = form.cost_per_hour.data
    service = Service(name, duration_hrs, duration_mins, cost)
    db.session().add(service)
    db.session().commit()
    return redirect(url_for("worker_index"))