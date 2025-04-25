from typing import List
from fastapi import APIRouter, HTTPException
from app.enrollments import schemas, services

router = APIRouter()

@router.post("/enrollments/", response_model=List[schemas.Enrollment])
def create_enrollment(enrollment: schemas.EnrollmentCreate):
    try:
        created_enrollment = services.create_enrollment(enrollment)
        return created_enrollment
    except Exception as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred: " + str(e))
