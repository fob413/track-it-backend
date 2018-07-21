import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from api.views.dummy_api import Dummy

db = SQLAlchemy()
login_manager = LoginManager()

app = Flask(__name__)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

db.init_app(app)
CORS(app)

from api.views.manage_user import login_blueprint
app.register_blueprint(login_blueprint)

from api.views.manage_pfi import pfi_blueprint
app.register_blueprint(pfi_blueprint)

from api.views.manage_shipments import statement_blueprint
app.register_blueprint(statement_blueprint)

app.shell_context_processor({'app': app, 'db': db})
