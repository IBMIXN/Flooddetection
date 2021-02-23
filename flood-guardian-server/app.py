from routes.location import location_app
from routes.assistant import assistant_app
# from routes.forecasts.jakarta import jakarta_app
from routes.forecast import forecast_app
from flask import Flask
import os

# load ENV variables
from dotenv import load_dotenv
load_dotenv(verbose=True)

app = Flask(__name__)

app.register_blueprint(assistant_app, url_prefix='/api/assistant')
app.register_blueprint(location_app, url_prefix='/api/location')
app.register_blueprint(forecast_app, url_prefix='/api/forecast')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
