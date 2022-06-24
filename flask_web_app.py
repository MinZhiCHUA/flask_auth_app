from applicationinsights.flask.ext import AppInsights
from flask import Flask

# create Flask app
app = Flask(__name__)
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = '9fc0b1a2-8f7f-472e-b889-e346889e4218'
appinsights = AppInsights(app)

# force flushing application insights handler after each request
@app.after_request
def after_request(response):
    appinsights.flush()
    return response