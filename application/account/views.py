from flask import render_template, request, redirect, url_for

from application import app
from application.account.models import Account
from application.account.forms import LoginForm

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


    print("Käyttäjä " + account.username + " tunnistettiin")
    return redirect(url_for("index"))    
