from project import db, app, models

# app = create_app()
app.app_context().push()
# app.app_context()

db.create_all()
# db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.


# ========================================================
# 