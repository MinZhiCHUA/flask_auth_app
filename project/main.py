from flask import Blueprint, render_template
from flask_login import login_required, current_user#, roles_required
# from flask_user import current_user
# from flask_user import roles_required
from project import app, app_authorization

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
    isadmin = False
    # print (current_user.roles)
    print (current_user.name)
    print (current_user.id)
    print (current_user.password)
    print (current_user.email)
    # print (current_user.role)
    if current_user.has_roles('admin'):
        print('THis is an admin!!!!!!!!!!!!!!!!')
        isadmin = True
    # if app_authorization.has_role('admin'):
    #     print('THis is an admin!!!!!!!!!!!!!!!!')
    return render_template('profile.html', name=current_user.name, isadmin = isadmin)

@main.route('/admin-page')
@login_required
# @app_authorization.has_roles('admin') # How to do this?????
# @roles_required('admin')
def admin_page():
    print('You are a admin!!!')
    return render_template('admin_page.html', name=current_user.name)