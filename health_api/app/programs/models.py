# Health_api/app/programs/models.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ProgramBase(BaseModel):
    program_name: str = Field(..., min_length=3, max_length=100, description="Name of the health program")
    description: Optional[str] = Field(None, max_length=500, description="Optional description of the program")

class ProgramCreate(ProgramBase):
    pass

class ProgramUpdate(ProgramBase):
    program_name: Optional[str] = Field(None, min_length=3, max_length=100, description="Optional new name of the health program")
    description: Optional[str] = Field(None, max_length=500, description="Optional new description of the program")

class Program(ProgramBase):
    id: str = Field(..., description="Unique identifier of the program")
    created_at: datetime = Field(..., description="Timestamp when the program was created")

    class Config:
        from_attributes = True