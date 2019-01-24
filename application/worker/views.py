from application import app, db
from flask import render_template, request, redirect, url_for
from datetime import datetime, date
from application.worker.models import Worker

# Kalenteritoiminnallisuus omaan luokkaansa?cat 

@app.route("/worker", methods=["GET"])
def worker_index():
    return render_template("worker/list.html", workers = Worker.query.all())

@app.route("/worker/<worker_id>/", methods=["POST"])
def worker_modify(worker_id):
    w = Worker.query.get(worker_id)
    #b.confirmed = True
    #db.session().commit()
    return redirect(url_for("booking_index"))

@app.route("/worker", methods=["POST"])
def worker_create():
    name = request.form.get("name")
    username = request.form.get("username")
    password = request.form.get("password") # NO HASH IN USE!!!
    isAdmin = request.form.get("admin")
    if isAdmin == "True":
        isAdmin = True
    else:
        isAdmin = False
    worker = Worker(name, username, password, isAdmin)
    db.session().add(worker)
    db.session().commit()

    return redirect(url_for("worker_index"))