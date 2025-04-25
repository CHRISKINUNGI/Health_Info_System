# Health_api/app/clients/models.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ClientBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    date_of_birth: datetime
    gender: str
    contact_number: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    gender: Optional[str] = None
    contact_number: Optional[str] = None

class Client(ClientBase):
    id: str = Field(...)
    created_at: datetime

    class Config:
        from_attributes = True