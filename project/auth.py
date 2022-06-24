from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

from flask_sqlalchemy import SQLAlchemy
# from flask_security import SQLAlchemyUserDatastore

from .models import User, Role, UserRole
from . import db

auth = Blueprint('auth', __name__)

# Setup Flask-Security
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    # role_user = Role.query.all(name="user")
    # print(role_user)
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    # new_user = user_datastore.create_user(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    # new_user.role = "user"
    # user.active = True
    role=1 # 1: user, 2:admin
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), roles=[Role.query.get(int(role))],)
    # new_user_role = UserRole(user_id= new_user.id, role_id = 1)
    # new_user.roles.append(role_user)
    # new_user.roles = ["user"]
    # new_user.

    # add the new user to the database
    db.session.add(new_user)
    # db.session.add(new_user_role)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))