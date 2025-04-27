# tests/test_clients.py

from fastapi.testclient import TestClient
from app.main import app  # adjust if your FastAPI app is elsewhere

client = TestClient(app)


def test_register_client_success():
    client_data = {
       
    "first_name": "eri",
    "last_name": "Ky",
    "date_of_birth": "1990-05-15T00:00:00",
    "gender": "male",
    "contact_number": "1122345671"
    }

    response = client.post("/api/v1/clients/", json=client_data)
    if response.status_code == 409:
        assert "already exists" in response.json()["detail"].lower()
    else:
        assert response.status_code == 201
        data = response.json()
        assert data["first_name"] == client_data["first_name"]
        assert data["last_name"] == client_data["last_name"]
        assert data["contact_number"] == client_data["contact_number"]
    


def test_register_client_duplicate_contact():
    client_data = {
       
    "first_name": "eri",
    "last_name": "Ky",
    "date_of_birth": "1990-05-15T00:00:00",
    "gender": "male",
    "contact_number": "1122345671"
    }

    response = client.post("/api/v1/clients/", json=client_data)

    assert response.status_code == 409
    assert "already exists" in response.json()["detail"].lower()


def test_list_all_clients():
    response = client.get("/api/v1/clients/?skip=0&limit=10")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_client_profile_not_found():
    fake_client_id = "00000000-0000-0000-0000-000000000000"

    response = client.get(f"/clients/{fake_client_id}")

    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_search_client_by_phone_not_found():
    fake_phone_number = "9999999999"

    response = client.get(f"/clients/search_by_phone/{fake_phone_number}")

    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
