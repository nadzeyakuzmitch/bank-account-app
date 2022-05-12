import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'
    SESSION_COOKIE_SECURE = True
    BOOTSTRAP_BOOTSWATCH_THEME = 'Simplex'
    DB_DIR = "database/db2.sqlite"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(DB_DIR)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = './uploads'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    DB_DIR = "database/dbtest.sqlite"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(DB_DIR)
    SESSION_COOKIE_SECURE = False
    DEBUG = True
