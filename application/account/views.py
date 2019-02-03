from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from application import app, db, bcrypt
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

    account = Account.query.filter_by(username=form.username.data).first()
    if not account:
        return render_template("account/loginform.html", form = form,
                               error = "No such username or password")
    candidate = form.password.data
    pw_matches = bcrypt.check_password_hash(account.password, candidate)
    
    if pw_matches != True:
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

    pwhash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    username = form.username.data
    account = Account(username, pwhash, 'Customer')
    db.session().add(account)
    db.session().commit()
    account_id = Account.query.filter_by(username=form.username.data, password=pwhash).first().id
    name = form.name.data
    email = form.email.data
    address = form.address.data
    phone = form.phone.data
    customer = Customer(name, email, address, phone, account_id)
    db.session().add(customer)
    db.session().commit()
    flash('User created')
    return redirect(url_for("user_login"))

@app.route("/accounts/<customer_id>/", methods=["GET", "POST"])
def customer_information(customer_id):
    form = NewCustomerForm()
    customer = Customer.query.filter_by(id=customer_id).first()
    account = Account.query.filter_by(id=customer.account_id).first()
    if request.method == "GET":
        form.username.data = account.username
        form.name.data = customer.name
        form.email.data = customer.email
        form.address.data = customer.address
        form.phone.data = customer.phone
        form.password.data = "12345"
        form.confirm_password.data = "12345"
        return render_template("account/modinfo.html", form = form, customer = customer)
    if not form.validate():
        return render_template("account/modinfo.html", form = form, customer = customer)
    if form.password.data != "12345":
        account.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    account.username = form.username.data
    customer.name = form.name.data
    customer.email = form.email.data
    customer.address = form.address.data
    customer.phone = form.phone.data
    db.session().commit()
    flash("Customer information successfully updated.")
    return render_template("account/modinfo.html", form = form, customer = Customer.query.filter_by(id=customer_id).first(), account = Account.query.filter_by(id=customer.account_id).first())

@app.route("/accounts")
def customer_listing():
    customers = Customer.query.order_by(Customer.name).all()
    return render_template("account/accounts.html", customers = customers)