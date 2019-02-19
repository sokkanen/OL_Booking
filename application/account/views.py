from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from application import app, db, bcrypt, login_required
from application.account.models import Account
from application.customer.models import Customer
from application.booking.models import Booking
from application.account.forms import LoginForm
from application.customer.forms import NewCustomerForm

@app.route("/login", methods = ["GET", "POST"])
def user_login():
    if request.method == "GET":
        return render_template("account/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    account = Account.query.filter_by(username=form.username.data).first()
    if not account:
        return render_template("account/loginform.html", form = form,
                               error = "No such username or password")
    candidate = form.password.data
    candidate.encode('utf-8')
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
    account = Account(username, pwhash, 'CUSTOMER')
    db.session().add(account)
    db.session().commit()
    account_id = Account.query.filter_by(username=form.username.data, password=pwhash).first().id
    name = form.name.data
    email = form.email.data
    address = form.address.data
    phone = form.phone.data
    customer = Customer(name, email, address, phone)
    customer.account_id = account_id
    db.session().add(customer)
    db.session().commit()
    flash('User created')
    return redirect(url_for("user_login"))

@app.route("/accounts/<customer_id>/", methods=["GET", "POST"])
@login_required(role="CUSTOMER")
def customer_information(customer_id):
    if request.method == "POST" and current_user.get_role() == "WORKER":
        return redirect(url_for("user_login"))
    customer = Customer.query.filter_by(id=customer_id).first()
    if current_user.get_role() == "CUSTOMER":
        if customer.account.id != current_user.get_id():
            return redirect(url_for("user_login"))
    form = NewCustomerForm()
    if customer.account_id is not None:
        account = Account.query.filter_by(id=customer.account_id).first()
    if request.method == "GET":
        if customer.account_id is not None:
            form.username.data = account.username
        else:
            form.username.data = "not registered"
        form.name.data = customer.name
        form.email.data = customer.email
        form.address.data = customer.address
        form.phone.data = customer.phone
        form.password.data = "12345"
        form.confirm_password.data = "12345"
        return render_template("account/modinfo.html", form = form, customer = customer)
    if not form.validate():
        return render_template("account/modinfo.html", form = form, customer = customer)
    if form.password.data != "12345" and customer.account_id != 0:
        account.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    if customer.account_id != None:
        account.username = form.username.data
    customer.name = form.name.data
    customer.email = form.email.data
    customer.address = form.address.data
    customer.phone = form.phone.data
    db.session().commit()
    flash("Customer information successfully updated.")
    return render_template("account/modinfo.html", form = form, customer = Customer.query.filter_by(id=customer_id).first(), account = Account.query.filter_by(id=customer.account_id).first())

@app.route("/accounts")
@login_required(role="CUSTOMER")
def customer_listing():
    if current_user.get_role() == "CUSTOMER":
        customers = Customer.query.filter_by(account_id=current_user.get_id()).first()
        return render_template("account/accounts.html", customers = customers)
    else:
        customers = Customer.query.order_by(Customer.name).all()
        return render_template("account/accounts.html", customers = customers)

@app.route("/accounts/del/<customer_id>/", methods=["POST"])
@login_required(role="ADMIN")
def customer_remove(customer_id):
    c = Customer.query.filter(Customer.id == customer_id).first()
    del_b = Booking.__table__.delete().where(Booking.customer_id == customer_id) # Poistetaan varaukset
    del_c = Customer.__table__.delete().where(Customer.id == customer_id) # Poistetaan asiakas
    db.session.execute(del_b)
    db.session.execute(del_c)
    if c.account_id != None:
        del_a = Account.__table__.delete().where(Account.id == c.account_id) # Poistetaan tili
        db.session.execute(del_a)
    db.session().commit()
    flash("Customer successfully removed")
    
    return redirect(url_for("customer_listing"))
    