import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from api.views.dummy_api import Dummy

db = SQLAlchemy()

def create_app(script_info=None):

    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    api = Api(app)

    api.add_resource(Dummy,
        '/api/v1/dummy',
        '/api/v1/dummy/',
        endpoint='dummy'
    )
    app.shell_context_processor({'app': app, 'db': db})

    return app
