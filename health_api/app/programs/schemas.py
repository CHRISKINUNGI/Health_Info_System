# Health_api/app/programs/schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProgramBase(BaseModel):
    program_name: str
    description: Optional[str] = None

class ProgramCreate(ProgramBase):
    pass

class ProgramUpdate(ProgramBase):
    pass

class Program(ProgramBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True