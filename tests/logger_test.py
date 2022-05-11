"""This checks logger files"""
# pylint: disable=redefined-outer-name

import os

from click.testing import CliRunner

runner = CliRunner()


def test_create_errors_log_file(client):
    """Testing if errors log was created."""
    response = client.get("/")
    assert response.status_code == 200
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../app/logs/appErrors.log')
    assert os.path.exists(logdir) is True


def test_create_info_log_file(client):
    """Testing if info log was created."""
    response = client.get("/")
    assert response.status_code == 200
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../app/logs/appInfo.log')
    assert os.path.exists(logdir) is True


def test_create_requests_log_file(client):
    """Testing if requests log was created."""
    response = client.get("/")
    assert response.status_code == 200
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../app/logs/appRequests.log')
    assert os.path.exists(logdir) is True


def test_create_debug_log_file(client):
    """Testing if debug log was created."""
    response = client.get("/")
    assert response.status_code == 200
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../app/logs/rootLogger.log')
    assert os.path.exists(logdir) is True


def test_create_transactions_log_file(client):
    """Testing if transactions log was created."""
    response = client.get("/")
    assert response.status_code == 200
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../app/logs/transactionUploads.log')
    assert os.path.exists(logdir) is True
