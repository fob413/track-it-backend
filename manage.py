from api import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api.models import (Users, Shipments, Pfi)


migrate = Migrate(app, db)
manager = Manager(app)


manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    """
    Create the db tables
    """
    db.create_all()

@manager.command
def drop_db():
    """
    Drop db tables
    """
    db.drop_all()

if __name__ == '__main__':
    manager.run()
