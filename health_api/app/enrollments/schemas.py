# app/enrollments/schemas.py

from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional
from app.clients.models import Client
from app.programs.models import Program

class EnrollmentBase(BaseModel):
    client_id: UUID  # Use UUID for client
    program_id: UUID  # Use UUID for program

class EnrollmentCreate(EnrollmentBase):
    client_id: UUID  # Use UUID for client
    program_ids: List[UUID]  # Allow multiple program IDs for enrollment

class Enrollment(EnrollmentBase):
    id: int  # ID of the enrollment in the table
    client: Client  # Include client info
    program: Program  # Include program info

    class Config:
        from_attributes = True