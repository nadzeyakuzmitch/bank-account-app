
"""This test login and registration"""

from flask_login import FlaskLoginClient

from app import db
from app.db.models import User


def test_login_success(application):
    """Test success login"""
    application.test_client_class = FlaskLoginClient
    user = User('user@user.user', 'user')
    db.session.add(user)
    db.session.commit()

    with application.test_client(user=user) as client:
        response = client.get('/dashboard')
        assert response.status_code == 200
        assert b'user@user.user' in response.data


def test_login_not_success(application):
    """Test not success login"""
    application.test_client_class = FlaskLoginClient

    with application.test_client() as client:
        response = client.get('/dashboard')
        assert response.status_code == 302
