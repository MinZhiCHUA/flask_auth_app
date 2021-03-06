from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_authorize import Authorize
import os
from dotenv import load_dotenv

# import logging


from applicationinsights.flask.ext import AppInsights
# from logging import StreamHandler

load_dotenv()

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

# def create_app():
app = Flask(__name__)

# app.config['SECRET_KEY'] = 'secret-key-goes-here'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["WTF_CSRF_SECRET_KEY"] = os.getenv("WTF_CSRF_SECRET_KEY")

# =======================================================
# mz added these trying to connect to the insight
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = '9fc0b1a2-8f7f-472e-b889-e346889e4218'
appinsights = AppInsights(app)


# # keep stdout/stderr logging using StreamHandler
# streamHandler = StreamHandler()
# app.logger.addHandler(streamHandler)


# force flushing application insights handler after each request
@app.after_request
def after_request(response):
    appinsights.flush()
    return response



# =======================================================
# Trying authorization

def my_current_user():
    """
    Return current user to check authorization against.
    """
    return g.user

app_authorization = Authorize(
    current_user=my_current_user,
    # exception=MyUnauthorizedException,
    strict=False,)
app_authorization.init_app(app)
# =======================================================


db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

    # return app