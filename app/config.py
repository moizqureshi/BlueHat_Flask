import os
from env import *

# Common configuration
class Config(object):
    """
    # Put any configurations here that are common across all environments
    """


# Development configurations
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = THE_SECRET_KEY
    #DB_HOST = os.getenv('IP', 'localhost')
    SQLALCHEMY_DATABASE_URI = "postgresql://ye_huang:@localhost:5432/bluehat"

# Production configurations
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = THE_SECRET_KEY
    #DB_HOST = os.getenv('IP', '0.0.0.0')
    SQLALCHEMY_DATABASE_URI = "postgresql://ye_huang:@localhost:5432/bluehat"

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
