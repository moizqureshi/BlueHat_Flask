''' =========================================================================================== '''
# BlueHat Flask Web App

# Local Imports
from app import app, socketio
from app import models
from app.models import *
from app import db
from env import *
import os

# Third-party Imports
from flask_socketio import SocketIO

''' =========================================================================================== '''
# run the app
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000)
