from typing import List
from ..database import supabase
from app.clients import schemas

def search_clients_by_contact_number(contact_number: str, limit: int = 10, offset: int = 0) -> List[schemas.Client]:
    response = supabase.table("clients").select("*") \
        .eq("contact_number", contact_number) \
        .range(offset, offset + limit - 1) \
        .execute()

    if not response.data:
        return []

    data = response.data
    return [schemas.Client(**item) for item in data]
