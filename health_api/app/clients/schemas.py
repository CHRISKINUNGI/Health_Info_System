# Health_api/app/clients/schemas.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ClientBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50, description="Client's first name")
    last_name: str = Field(..., min_length=2, max_length=50, description="Client's last name")
    date_of_birth: datetime = Field(..., description="Client's date of birth (YYYY-MM-DD)")
    gender: str = Field(..., description="Client's gender (e.g., Male, Female, Other)")
    contact_number: Optional[str] = Field(None, description="Client's contact phone number")

    class Config:
        json_encoders = {datetime: lambda dt: dt.isoformat()}

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    first_name: Optional[str] = Field(None, min_length=2, max_length=50, description="Optional new first name")
    last_name: Optional[str] = Field(None, min_length=2, max_length=50, description="Optional new last name")
    date_of_birth: Optional[datetime] = Field(None, description="Optional new date of birth")
    gender: Optional[str] = Field(None, description="Optional new gender")
    contact_number: Optional[str] = Field(None, description="Optional new contact number")

    class Config:
        json_encoders = {datetime: lambda dt: dt.isoformat()}

class Client(ClientBase):
    id: str = Field(..., description="Unique identifier of the client")
    created_at: datetime = Field(..., description="Timestamp when the client was registered")

    class Config:
        from_attributes = True
        json_encoders = {datetime: lambda dt: dt.isoformat()}