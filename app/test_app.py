from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200  # This will pass

def test_read_item():
    response = client.get("/items/1?q=test")
    assert response.status_code == 200  # This will pass

def test_intentional_fail():
    # This test will fail as it checks for a non-existing route
    response = client.get("/non-existing-route")
    assert response.status_code == 200  # This will fail since the status code will be 404
