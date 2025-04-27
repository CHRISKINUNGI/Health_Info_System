from fastapi import APIRouter, Depends, Header, HTTPException
from app.auth.schemas import DoctorSignUp, DoctorLogin, TokenResponse, DoctorProfile
from app.auth.services import signup_doctor, login_doctor, decode_doctor_token

router = APIRouter()

@router.post("/signup", summary="Doctor Signup", status_code=201)
def doctor_signup(payload: DoctorSignUp):
    return signup_doctor(payload)

@router.post("/login", response_model=TokenResponse, summary="Doctor Login")
def doctor_login(payload: DoctorLogin):
    return login_doctor(payload)

def get_current_doctor(authorization: str = Header(...)) -> dict:
    """Helper function to extract and decode the token from the 'Authorization' header."""
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header.")
    
    token = authorization.split(" ")[1]
    try:
        doctor = decode_doctor_token(token)
        if "sub" not in doctor or "email" not in doctor:
            raise HTTPException(status_code=401, detail="Invalid token payload.")
        return doctor
    except HTTPException as e:
        raise e  # Reraise the error if decoding fails
    except Exception:
        raise HTTPException(status_code=401, detail="Token decoding error.")

@router.get("/profile", response_model=DoctorProfile, summary="Get Current Doctor Profile")
def doctor_profile(doctor: dict = Depends(get_current_doctor)):
    """Endpoint to retrieve the doctor's profile."""
    return {
        "id": doctor["sub"],
        "email": doctor["email"]
    }
