# third-party imports
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO, send


# local imports
from config import app_config
from env import *

# db variable initialization
db = SQLAlchemy()

# App Config
app = Flask(__name__)
app.config.from_object(app_config[FLASK_CONFIG])
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = False

# DB Config
db.init_app(app)

# Migration Config
migration = Migrate(app, db)

# Session Config
app.secret_key = THE_SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


# Late import so modules can import their dependencies properly
from app import models, views
