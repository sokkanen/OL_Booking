from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///olbooking.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Kirjautuminen.

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "user_login"
login_manager.login_message = "Please login. If you keep seeing this message, you don't have the rights to use or view this resource."

# Roolit

from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
          
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True

            if current_user.get_role() == "ADMIN":
                unauthorized = False

            if role == "CUSTOMER" and current_user.get_role() == "WORKER":
                unauthorized = False

            if current_user.get_role() == role:
                unauthorized = False

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


# Ohjelman sisäiset kohteet

from application import views

from application.booking import views
from application.booking import models

from application.worker import views
from application.worker import models

from application.service import models
from application.customer import models

from application.account import models
from application.account import views

# Kirjautuminen 2
from application.account.models import Account

@login_manager.user_loader
def load_account(account_id):
    return Account.query.get(account_id)

# Luo taulut
try:
    db.create_all()
#    pwhash = bcrypt.generate_password_hash('testi').decode('utf-8')
#    username = 'testi'
#    role = 'ADMIN'
#    account = Account(username, pwhash, role)
#    db.session().add(account)
#    db.session().commit()
except:
    pass