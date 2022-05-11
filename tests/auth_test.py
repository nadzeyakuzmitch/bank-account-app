"""This test the homepage"""


def test_foud_index(client):
    """Check found index"""
    response = client.get("/index")
    assert response.status_code == 200


def test_foud_register(client):
    """Check found register"""
    response = client.get("/register")
    assert response.status_code == 200


def test_foud_login(client):
    """Check found login"""
    response = client.get("/login")
    assert response.status_code == 200


def test_not_foud_page(client):
    """Checknot not found page"""
    response = client.get("/whateveves")
    assert response.status_code == 404


def test_deny_dashboard(client):
    """Deny dashboard"""
    response = client.get("/dashboard")
    assert response.status_code == 302


def test_deny_transactions_page(client):
    """Deny transactions page"""
    response = client.get("/transactions")
    assert response.status_code == 302


def test_deny_transactions_upload(client):
    """Deny transactions upload"""
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


def test_deny_users_page(client):
    """Deny users page"""
    response = client.get("/users")
    assert response.status_code == 302
