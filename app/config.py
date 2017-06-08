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
    SQLALCHEMY_DATABASE_URI = "postgres://" + DB_USER + ":" + DB_PASS + "@localhost/" + DB_NAME
    REDIS_HOST = REDIS_DEV_HOST
    REDIS_PORT = REDIS_DEV_PORT
    REDIS_DB = REDIS_DEV_DB
    REDIS_PASSWORD = REDIS_DEV_PASSWORD

# Production configurations
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = THE_SECRET_KEY
    SQLALCHEMY_DATABASE_URI = HEROKU_DB_URL
    REDIS_HOST = REDIS_PROD_URL
    # REDIS_PORT = REDIS_PROD_PORT
    # REDIS_DB = REDIS_PROD_DB
    # REDIS_PASSWORD = REDIS_PROD_PASSWORD

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
