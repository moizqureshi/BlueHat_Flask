''' =========================================================================================== '''
# BlueHat Flask Web App

# Local Imports
from app import app
from app import models
from app.models import *
from app import db
from env import *
import os


''' =========================================================================================== '''
# run the app
if __name__ == '__main__':
    app.run()
