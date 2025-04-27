# app/auth/schemas.py

from pydantic import BaseModel, EmailStr

class DoctorSignUp(BaseModel):
    email: EmailStr
    password: str

class DoctorLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class DoctorProfile(BaseModel):
    id: str
    email: EmailStr
