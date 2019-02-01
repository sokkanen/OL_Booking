from flask import render_template, request, redirect, url_for

from application import app
from application.customer.models import Customer
from application.customer.forms import CustomerLoginForm

@app.route("/customer/login", methods = ["GET", "POST"])
def customer_login():
    if request.method == "GET":
        return render_template("customer/loginform.html", form = CustomerLoginForm())

    form = CustomerLoginForm(request.form)
    # mahdolliset validoinnit

    customer = Customer.query.filter_by(name=form.name.data, password=form.password.data).first()
    if not customer:
        return render_template("customer/loginform.html", form = form,
                               error = "No such username or password")


    print("Käyttäjä " + customer.name + " tunnistettiin")
    return redirect(url_for("index"))    
