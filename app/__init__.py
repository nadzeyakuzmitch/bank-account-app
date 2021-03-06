"""A simple flask web app"""
import os

import flask_login
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

from app.auth import auth
from app.auth_pages import auth_pages
from app.bank_app_pages import bank_app_pages
from app.cli import (create_database, create_log_folder, create_uploads_folder,
                     db_folder_create, uploads_folder_create)
from app.context_processors import utility_text_processors
from app.db import db
from app.db.models import User
from app.error_handlers import error_handlers
from app.logging_config import log_con

from app.transactions_pages import transactions_pages

login_manager = flask_login.LoginManager()


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    if app.config["ENV"] == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif app.config["ENV"] == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("app.config.TestingConfig")

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    csrf = CSRFProtect(app)
    bootstrap = Bootstrap5(app)

    app.register_blueprint(auth_pages)
    app.register_blueprint(bank_app_pages)
    app.register_blueprint(auth)
    app.context_processor(utility_text_processors)

    app.register_blueprint(log_con)
    app.register_blueprint(error_handlers)
    app.register_blueprint(transactions_pages)
    app.cli.add_command(create_database)
    app.cli.add_command(create_uploads_folder)
    app.cli.add_command(create_log_folder)
    db.init_app(app)

    @app.before_request
    def create_necessary_folders():
        db_folder_create()
        uploads_folder_create()

    return app


def create_test_app():
    """Create fake app for testing with test database"""
    app = Flask(__name__)
    app.config.from_object("app.config.TestingConfig")

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    csrf = CSRFProtect(app)
    bootstrap = Bootstrap5(app)

    app.register_blueprint(auth_pages)
    app.register_blueprint(bank_app_pages)
    app.register_blueprint(auth)
    app.context_processor(utility_text_processors)

    app.register_blueprint(log_con)
    app.register_blueprint(error_handlers)
    app.register_blueprint(transactions_pages)
    app.cli.add_command(create_database)
    app.cli.add_command(create_uploads_folder)
    app.cli.add_command(create_log_folder)
    db.init_app(app)

    return app


@login_manager.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None
