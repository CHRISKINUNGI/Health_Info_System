# test_programs.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test creating a program
def test_create_program():
    program_data = {
        
    "program_name": "prog",
    "description": "Provides test support for mental well-being."
}
    

    # Testing POST request to create a program
    response = client.post("/api/v1/programs/", json=program_data)
    
    if response.status_code == 409:
        assert "already exists" in response.json()["detail"].lower()
    else:
        assert response.status_code == 201
        data = response.json()
        assert data["program_name"] == program_data["program_name"]
        assert data["description"] == program_data["description"]
    
    
# Test listing programs
def test_list_programs():
    response = client.get("/api/v1/programs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Make sure there are programs listed

