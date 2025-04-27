# tests/test_search_clients.py

from fastapi.testclient import TestClient
from app.main import app  # Adjust based on your app's structure
from app.clients import schemas

client = TestClient(app)

def test_search_clients_success():
    # Test for searching an existing contact number
    contact_number = "1122345671"  # Assume this number exists in your test DB

    response = client.get(f"/api/v1/search/clients?contact_number={contact_number}&limit=10&offset=0")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0  # Assuming at least one client is returned
    assert data[0]["contact_number"] == contact_number

def test_search_clients_not_found():
    # Test for searching a non-existing contact number
    contact_number = "9999999999"  # Assume this number doesn't exist in your DB

    response = client.get(f"/api/v1/search/clients?contact_number={contact_number}&limit=10&offset=0")

    assert response.status_code == 404
    assert "Client not found" in response.json().get("detail", "")

def test_search_clients_invalid_contact_number():
    # Test for an invalid contact number format
    contact_number = "invalid_number"

    response = client.get(f"/api/v1/search/clients?contact_number={contact_number}&limit=10&offset=0")

    assert response.status_code == 404  # Unprocessable Entity for invalid query params
    assert "Client not found" in response.json().get("detail", "")  # Expected error message
