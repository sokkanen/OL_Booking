from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from application import app, db
from application.account.models import Account
from application.customer.models import Customer
from application.account.forms import LoginForm
from application.customer.forms import NewCustomerForm

@app.route("/login", methods = ["GET", "POST"])
def user_login():
    if request.method == "GET":
        return render_template("account/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    account = Account.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not account:
        return render_template("account/loginform.html", form = form,
                               error = "No such username or password")

    login_user(account)
    flash('Logged in successfully.')
    return redirect(url_for("index"))

@app.route("/logout")
def user_logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for("index"))

@app.route("/register", methods = ["GET", "POST"])
def user_register():
    if request.method == "GET":
        return render_template("account/register.html", form = NewCustomerForm())

    form = NewCustomerForm(request.form)
    if not form.validate():
        return render_template("account/register.html", form = form)

    password = form.password.data
    username = form.username.data
    account = Account(username, password)
    db.session().add(account)
    db.session().commit() # Luodaan ensin Account
    account_id = Account.query.filter_by(username=form.username.data, password=form.password.data).first().id
    name = form.name.data
    email = form.email.data
    address = form.address.data
    phone = form.phone.data
    customer = Customer(name, email, address, phone, account_id)
    db.session().add(customer)
    db.session().commit() # Luodaan Customer, jossa viite äsken luotuun Accountiin.
    flash('User created')
    return redirect(url_for("user_login"))

# ASIAKASSIVU
# Puuttuu template
# Puuttuu linkkaaminen /Bookings -sivulta.
# Tähän myös asiakastietojen muokkaaminen.
@app.route("/account/<customer_id>/", methods=["GET", "POST"])
def customer_information(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    return render_template("account/customer.html", customer = customer)
