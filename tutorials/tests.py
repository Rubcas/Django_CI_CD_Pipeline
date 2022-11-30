from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial

# This Unit test is to make sure when the reverse the view named home, we gt the expected path for the homepage on the website.

def test_homepage_access():
    url = reverse('home')
    assert url == "/"

# This integration test will check whether we can succesfully interact with the database via Django models/ORM.

#The decorator below gives access to the connected database. 
'''@pytest.mark.django_db
def test_create_turorial():
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url = 'https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    assert tutorial.title == "Pytest"

'''
#Writing more integration test for the test_create_tutorial function. Implementing a fixture to do this
@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

#Checks that the object created by the fixture exist, by searching for an object with the same title.
def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

#updates the title of the new_tutorial object, saves the update, and asserts that a tutorial with the updated name exists in the database.
def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()


# This fixture is implemented to show that we can use multiple fixtures in the test function.
@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

# Checks that passing the both fixtures are not equal.
def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk


#Integration Test to check the user login by using Django built in user model and authentication system
