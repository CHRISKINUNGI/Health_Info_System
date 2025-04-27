from app.database import get_supabase_client
from fastapi import HTTPException
from jose import jwt, JWTError
from .schemas import DoctorSignUp, DoctorLogin
import os
import re

JWT_SECRET = os.getenv("JWT_SECRET")  # Set this in your .env too!

supabase = get_supabase_client()

def is_valid_email(email: str) -> bool:
    """Simple email validation using regex."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

def signup_doctor(payload: DoctorSignUp):
    # Validate email format
    if not is_valid_email(payload.email):
        raise HTTPException(status_code=400, detail="Invalid email format.")
    
    try:
        # Attempt to sign up the doctor
        response = supabase.auth.sign_up({
            "email": payload.email.strip(),
            "password": payload.password
        })
        
        # Log the entire response object for debugging
        print(f"Supabase response: {response}")

        # Check if the user is created
        if response.user is None:
            raise HTTPException(status_code=400, detail="Signup failed. Please check your details.")
        
        return {"message": "Signup successful. Please verify your email."}
    
    except Exception as e:
        # Catch any unexpected error and raise an HTTPException
        raise HTTPException(status_code=400, detail=f"Signup failed: {str(e)}")

def login_doctor(payload: DoctorLogin):
    # Validate email format
    if not is_valid_email(payload.email):
        raise HTTPException(status_code=400, detail="Invalid email format.")
    
    try:
        # Attempt to log in the doctor
        response = supabase.auth.sign_in_with_password({
            "email": payload.email,
            "password": payload.password
        })

        # Log the entire response object for debugging
        print(f"Login Supabase response: {response}")
        
        # Check if the session exists
        if not response.session:
            raise HTTPException(status_code=401, detail="Login failed. Check email and password.")
        
        # Ensure that we extract the access token from the response
        access_token = response.session.access_token if response.session else None
        
        if not access_token:
            raise HTTPException(status_code=401, detail="Access token not found.")
        
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    except Exception as e:
        # Catch any unexpected error and raise an HTTPException
        raise HTTPException(status_code=400, detail=f"Login failed: {str(e)}")

def decode_doctor_token(token: str):
    try:
        # Decode the JWT token
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except JWTError as e:
        # Handle invalid or expired token
        raise HTTPException(status_code=401, detail="Invalid or expired token.")
    except Exception as e:
        # Catch any other decoding issues
        raise HTTPException(status_code=401, detail=f"Error decoding token: {str(e)}")
