from flask_login import UserMixin
# from flask_user import UserMixin # This has the function _has_role
from flask_authorize import RestrictionsMixin, AllowancesMixin
from flask_authorize import PermissionsMixin

from . import db



def add_func (a,b):
    return a + b

# class UserRole (db.Model):

#     'user_role', db.Model.metadata,
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
#     db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))

UserRole = db.Table(
    'user_role', db.Model.metadata,
    # id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    roles = db.relationship('Role', secondary=UserRole, backref=db.backref("user", lazy="dynamic"))

    # Or we can use this method from flask_user import UserMixin # This has the function _has_role
    def has_roles(self, *args):
        return set(args).issubset({role.name for role in self.roles})


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



class Role(db.Model, AllowancesMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

# ========================================================