from application import app, db
from flask import render_template, request, redirect, url_for
from datetime import datetime, date
from application.worker.models import Worker
from application.service.models import Service
from application.worker.forms import WorkerForm
from application.service.forms import ServiceForm, Service_Worker_Form

@app.route("/worker", methods=["GET"])
def worker_index():
    return render_template("worker/list.html", workers = Worker.query.all(), services = Service.query.all(), wform = WorkerForm(), sform = ServiceForm(), swform = Service_Worker_Form())

@app.route("/worker/<worker_id>/", methods=["POST"])
def worker_modify(worker_id):
    w = Worker.query.get(worker_id)
    # TARVITSEE SÄÄTÄÄ JA RAKENTAA
    #b.confirmed = True
    #db.session().commit()
    return redirect(url_for("booking_index"))

@app.route("/worker", methods=["POST"])
def worker_create():
    form = WorkerForm(request.form)
    if not form.validate():
        return render_template("worker/list.html", workers = Worker.query.all(), services = Service.query.all(), wform = form, sform = ServiceForm(), swform = Service_Worker_Form())
    name = form.name.data
    password = form.password.data
    isAdmin = form.role.data
    if isAdmin == "True":
        isAdmin = True
    else:
        isAdmin = False
    worker = Worker(name, name, password, isAdmin)
    db.session().add(worker)
    db.session().commit()
    return redirect(url_for("worker_index"))

@app.route("/worker/assign", methods=["POST"])
def worker_assign():
    # TARVITSEE LIITOSTAULUN
    print("hi!")
    return redirect(url_for("worker_index"))

@app.route("/worker/add_service", methods=["POST"])
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