import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from api.views.dummy_api import Dummy

db = SQLAlchemy()
login_manager = LoginManager()

app = Flask(__name__)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

db.init_app(app)
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."

from api.views.manage_user import login_blueprint, logout_blueprint
app.register_blueprint(login_blueprint)
app.register_blueprint(logout_blueprint)

app.shell_context_processor({'app': app, 'db': db})
