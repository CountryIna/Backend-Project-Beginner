from http.client import responses

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_notes():
    response = client.get("/notes")

    assert response.status_code == 200

def test_create_note():
    response = client.post("/notes",
                            json={"title": "Testing FastAPI",
                                  "content": "Belajar pytest"})

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Testing FastAPI"
    assert data["content"] == "Belajar pytest"

def test_get_not_found():
    response = client.get("/notes/999999")

    assert response.status_code == 404