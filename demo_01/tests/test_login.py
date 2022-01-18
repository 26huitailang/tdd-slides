from fastapi import FastAPI
from fastapi.testclient import TestClient

from ..app import app

client = TestClient(app)


def test_login():
    response = client.post("/login", json={"username": "root", "password": "password"})
    assert response.status_code == 200
    assert response.json() == {"success": False}
    print(response.json())
