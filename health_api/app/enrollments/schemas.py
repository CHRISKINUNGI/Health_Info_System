# app/enrollments/schemas.py

from pydantic import BaseModel
from uuid import UUID
from typing import List
from app.clients.models import Client
from app.programs.models import Program

class EnrollmentBase(BaseModel):
    client_id: UUID
    program_id: UUID

class EnrollmentCreate(BaseModel):  # <-- Don't inherit from EnrollmentBase
    client_id: UUID
    program_ids: List[UUID]  # <-- It's a list now, for creation

class Enrollment(EnrollmentBase):
    id: int
    client: Client
    program: Program

    class Config:
        from_attributes = True
