import pytest
from fastapi.testclient import TestClient
from app.main import app  # assuming your FastAPI app is in a file called main.py
from app.auth.schemas import DoctorSignUp, DoctorLogin
from app.auth.services import is_valid_email

client = TestClient(app)

def test_doctor_signup():
    
    test_user = {
        "email": "chris@gmail.com",
        "password": "testpassword"
    }
    # Test the signup endpoint
    response = client.post("/api/v1/auth/signup", json=test_user)
    
    # Print the actual response for debugging
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())
    
    assert response.status_code == 201 # Ensure status code is 201 for successful signup
    assert response.json().get("message") == "Signup successful. Please verify your email."

def test_doctor_signup_invalid_email():
    invalid_payload = {
        "email": "invalid-email",
        "password": "password123"
    }
    
    response = client.post("/api/v1/auth/signup", json=invalid_payload)
    
    assert response.status_code == 422  # Expect 422 if FastAPI validation fails
    assert response.json()["detail"][0]["msg"] == "value is not a valid email address: An email address must have an @-sign."


