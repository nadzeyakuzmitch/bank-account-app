"""This test pages on various conditions"""

from flask_login import FlaskLoginClient
from app import db
from app.db.models import User


def test_foud_index(client):
    """Allow index page"""
    response = client.get("/index")
    assert response.status_code == 200


def test_foud_register(client):
    """Allow register page"""
    response = client.get("/register")
    assert response.status_code == 200


def test_foud_login(client):
    """Allow login page"""
    response = client.get("/login")
    assert response.status_code == 200


def test_not_foud_page(client):
    """Check not found page"""
    response = client.get("/whateveves")
    assert response.status_code == 404


def test_deny_dashboard(client):
    """Deny dashboard page"""
    response = client.get("/dashboard")
    assert response.status_code == 302


def test_deny_transactions_page(client):
    """Deny transactions page"""
    response = client.get("/transactions")
    assert response.status_code == 302


def test_deny_transactions_upload(client):
    """Deny transactions upload page"""
    response = client.get("/transactions/upload")
    assert response.status_code == 302


def test_deny_profile_page(client):
    """Deny profile page"""
    response = client.get("/profile")
    assert response.status_code == 302


def test_deny_account_page(client):
    """Deny account page"""
    response = client.get("/account")
    assert response.status_code == 302


def test_logged_in_found_dashboard(application):
    """Allow dashboard page for logged in user"""
    application.test_client_class = FlaskLoginClient
    user = User('user@user.user', 'user')
    db.session.add(user)
    db.session.commit()
    with application.test_client(user=user) as client:
        response = client.get('/dashboard')
        assert response.status_code == 200


def test_logged_in_found_transactions(application):
    """Allow transactions page for logged in user"""
    application.test_client_class = FlaskLoginClient
    user = User('user@user.user', 'user')
    db.session.add(user)
    db.session.commit()
    with application.test_client(user=user) as client:
        response = client.get('/transactions')
        assert response.status_code == 200


def test_logged_in_found_transactions_upload(application):
    """Allow transactions upload page for logged in user"""
    application.test_client_class = FlaskLoginClient
    user = User('user@user.user', 'user')
    db.session.add(user)
    db.session.commit()
    with application.test_client(user=user) as client:
        response = client.get('/transactions/upload')
        assert response.status_code == 200


def test_logged_in_found_profile(application):
    """Allow profile page for logged in user"""
    application.test_client_class = FlaskLoginClient
    user = User('user@user.user', 'user')
    db.session.add(user)
    db.session.commit()
    with application.test_client(user=user) as client:
        response = client.get('/profile')
        assert response.status_code == 200


def test_logged_in_found_account(application):
    """Allow account page for logged in user"""
    application.test_client_class = FlaskLoginClient
    user = User('user@user.user', 'user')
    db.session.add(user)
    db.session.commit()
    with application.test_client(user=user) as client:
        response = client.get('/account')
        assert response.status_code == 200
