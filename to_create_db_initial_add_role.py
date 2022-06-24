from project import db, app, models
from werkzeug.security import generate_password_hash, check_password_hash
from project.models import User, Role

# app = create_app()
app.app_context().push()
# app.app_context()

db.drop_all()
db.create_all()
# db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.


# ========================================================
# Put some initial users 
role_user = Role(name="user")
role_admin = Role(name="admin")

new_user1 = User(email='abcabc@gmail.com', name='ABC ABC', password=generate_password_hash('abcabc', method='sha256'))
new_user1.roles.append(role_user)
new_user2 = User(email='testing@gmail.com', name='Testing all the time', password=generate_password_hash('testing', method='sha256'))
new_user2.roles.append(role_user)
new_user3 = User(email='mickey@gmail.com', name='Mickey MOUSE', password=generate_password_hash('mickey', method='sha256'))
new_user3.roles.append(role_user)
new_user4 = User(email='harry@gmail.com', name='Harry Potter', password=generate_password_hash('harry', method='sha256'))
new_user4.roles.append(role_user)

new_admin = User(email='admin@gmail.com', name='Admin: Min Zhi', password=generate_password_hash('admin', method='sha256'))
new_admin.roles.append(role_admin)
new_admin.roles.append(role_user)

#     # add the new user to the database
db.session.add(new_user1)
db.session.add(new_user2)
db.session.add(new_user3)
db.session.add(new_user4)
db.session.add(new_admin)

db.session.commit()