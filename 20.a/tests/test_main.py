import os
import pytest

# important: this line needs to be set BEFORE the "app" import
os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from main import app, db


@pytest.fixture
def client():
    client = app.test_client()

    cleanup()  # clean up before every test

    db.create_all()

    yield client


def cleanup():
    # clean up/delete the DB (drop all tables in the database)
    db.drop_all()


def test_home_page(client):
    response = client.get("/")
    assert b"Do you want to register or log-in" in response.data



def test_registration_page_post_get(client):
    response = client.get("/registration")

    assert b"Welcome to registration" in response.data


def test_registration_page_post(client):
    response = client.post("/registration", data={"user-email": "b@b", "password": "b", "repeat": "b"})
    assert b"Your registration was successful!" in response.data


def test_dashboard_page(client):
    client.post("/registration", data={"user-email": "b@b", "password": "b", "repeat": "b"})
    client.post("/login", data={"user-email": "b@b", "password": "b"}, follow_redirects=True)
    response = client.get("/dashboard")

    assert b"Your email is" in response.data