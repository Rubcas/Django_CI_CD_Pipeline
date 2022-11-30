from django.test import TestCase
from django.urls import reverse
import pytest


# django_user_mode is a built in fixture.
@pytest.fixture
def test_user(db, django_user_model):
    django_user_model.objects.create_user( #creates a new user
        username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple

#Test to confirm if logging into the app works using the test_user function.
def test_login_user(client, test_user):
    test_username, test_password = test_user  # this unpacks the tuple
    login_result = client.login(username=test_username, password=test_password) #login() helps with testing to see if we can log into the app.
    assert login_result == True

