# app/enrollments/models.py

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class EnrollmentBase(BaseModel):
    client_id: str  # UUID for client
    program_id: str  # UUID for program

class EnrollmentCreate(EnrollmentBase):
    pass

class Enrollment(EnrollmentBase):
    id: int  # ID of the enrollment in the table
    created_at: datetime

    class Config:
        from_attributes = True