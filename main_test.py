# test_app.py
import pytest
from main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello I like to make AI Apps" in response.data


def test_name_route(client):
    response = client.get("/name/John")
    assert response.status_code == 200
    assert {"value": "John"} == response.get_json()
