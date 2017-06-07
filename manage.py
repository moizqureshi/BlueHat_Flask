import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.config import app_config
from app import app, db
from env import *

app.config.from_object(app_config[FLASK_CONFIG])
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
