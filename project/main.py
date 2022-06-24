from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from project import app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    app.logger.debug('This is a debug log message')
    app.logger.info('This is an information log message')
    app.logger.warn('This is a warning log message')
    app.logger.error('This is an error message')
    app.logger.critical('This is a critical message')
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)