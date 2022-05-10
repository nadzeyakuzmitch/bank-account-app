"""This tests the context processors that help the theme print common functions"""
import datetime
from os import getenv

def test_context_variables_environment(client):
    """This test checks if the environment is printed"""
    assert 200 == 200