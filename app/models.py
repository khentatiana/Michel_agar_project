from flask_login import UserMixin
import db

class User(UserMixin, db.Model):
    #...
    pass
