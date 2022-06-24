from flask_login import UserMixin
from . import db

def add_func (a,b):
    return a + b

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# ========================================================
# class Channel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False) 
#     url = db.Column(db.String(200), nullable=False)
#     description = db.Column(db.String(200), nullable=True)
#     language = db.Column(db.String(200), nullable=True)
#     subjects = db.Column(db.String(200), nullable=True)
#     image_url = db.Column(db.String(200), nullable=True)

# ========================================================

# ========================================================
# Create the Role Table

# Class Role()


# ========================================================