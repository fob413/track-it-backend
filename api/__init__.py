import os

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from api.views.dummy_api import Dummy

db = SQLAlchemy()
login_manager = LoginManager()

executors = {
    'default': {'type': 'threadpool', 'max_workers': 20},
    'processpool': ProcessPoolExecutor(max_workers=5)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 1
}

scheduler = BackgroundScheduler()

app = Flask(__name__)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)
app.config['REDIS_URL'] = os.getenv('REDIS_URL')

db.init_app(app)
CORS(app)

from api.views.manage_user import login_blueprint
app.register_blueprint(login_blueprint)

from api.views.manage_pfi import pfi_blueprint, sse_blueprint
app.register_blueprint(pfi_blueprint)
app.register_blueprint(sse_blueprint)

from api.views.manage_shipments import statement_blueprint
app.register_blueprint(statement_blueprint)

app.shell_context_processor({'app': app, 'db': db})
