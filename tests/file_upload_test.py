"""This tests transactions uploads"""
from flask_login import FlaskLoginClient

from app import db
from app.db.models import Transaction, User


def test_credit_balance_correct(application):
    """Show CREDIT balance correct when add DEBIT"""
    application.test_client_class = FlaskLoginClient
    user = User('user@user.user', 'user')
    db.session.add(user)
    db.session.commit()

    transaction = Transaction(200, 'DEBIT')
    db.session.add(transaction)
    db.session.commit()

    with application.test_client(user=user) as client:
        response = client.get('/dashboard')
        assert response.status_code == 200
        assert b'0$' in response.data


def test_debit_balance_correct(application):
    """Show DEBIT balance correct when add CREDIT"""
    application.test_client_class = FlaskLoginClient
    user = User('user@user.user', 'user')
    db.session.add(user)
    db.session.commit()

    transaction = Transaction(10, 'CREDIT')
    db.session.add(transaction)
    db.session.commit()

    with application.test_client(user=user) as client:
        response = client.get('/dashboard')
        assert response.status_code == 200
        assert b'0$' in response.data
