from application import db

class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, username, password, isAdmin):
        self.name = name
        self.username = username
        self.password = password
        self.isAdmin = isAdmin
  
    #def get_id(self):
    #    return self.id

    #def is_active(self):
    #    return True

    #def is_anonymous(self):
    #    return False

    #def is_authenticated(self):
    #    return True

    #def is_admin(self):
    #    return self.isAdmin