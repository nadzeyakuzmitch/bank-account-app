"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name
import pytest

from app import create_test_app, User
from app.db import db


@pytest.fixture()
def application():
    """This makes the appplication itself"""
    application = create_test_app()
    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        db.drop_all()
    return application


@pytest.fixture()
def add_user(application):
    """ Adding a user to the application's database """
    with application.app_context():
        user = User('test@test.test', 'test')
        db.session.add(user)
        db.session.commit()


@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()
