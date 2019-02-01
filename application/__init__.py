from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///olbooking.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application.booking import views
from application.booking import models
from application.worker import views
from application.worker import models
from application.service import models
from application.account import models
from application.account import views
from application.customer import models
  
db.create_all()