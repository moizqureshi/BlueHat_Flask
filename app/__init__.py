# local imports
from config import app_config
from env import *

# third-party imports
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_login import LoginManager
from flask_compress import Compress
from flask_cdn import CDN

# Socket Init Setting
async_mode = "eventlet"

# db variable initialization
db = SQLAlchemy()

# flask-login initialization
login_manager = LoginManager()

# cdn initialization
cdn = CDN()

# compress initialization
compress = Compress()

# App Config
app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)
app.config.from_object(app_config[FLASK_CONFIG])
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = False
app.config['CDN_DOMAIN'] = 'd30bzjua38r0w8.cloudfront.net'
app.config['CDN_HTTPS'] = True
app.config['CDN_DEBUG'] = True

# DB Config
db.init_app(app)

# Migration Config
migration = Migrate(app, db)

# Session Config
app.secret_key = THE_SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# CDN Config
cdn.init_app(app)

# flask-compress config
compress.init_app(app)

# flask-login config
login_manager.init_app(app)


# Late import so modules can import their dependencies properly
from app import models, views
