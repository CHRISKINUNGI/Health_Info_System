# Health_api/app/clients/services.py

from typing import List
from . import models, schemas
from ..database import supabase
from datetime import datetime

def check_existing_client_by_name(first_name: str, last_name: str) -> models.Client | None:
    response = supabase.table("clients").select("*").ilike("first_name", first_name).ilike("last_name", last_name).execute()
    data = response.data
    if data and len(data) > 0:
        return models.Client(**data[0])
    return None

def create_new_client(client: schemas.ClientCreate) -> models.Client:
    existing_client = check_existing_client_by_name(client.first_name, client.last_name)
    if existing_client:
        raise Exception(f"Client with name '{client.first_name} {client.last_name}' already exists.")

    new_client = client.dict()
    for key, value in new_client.items():
        if isinstance(value, datetime):
            new_client[key] = value.isoformat()

    response = supabase.table("clients").insert(new_client).execute()
    print(f"Create Client - Full Response: {response.model_dump_json()}")

    if not response.data:
        raise Exception(f"Supabase Error: {response.error if response.error else 'Unknown error occurred'}")

    data = response.data
    if len(data) > 0:
        return models.Client(**data[0])
    raise Exception("No data returned when creating client.")
def get_all_clients(skip: int = 0, limit: int = 100) -> List[schemas.Client]:
    response = supabase.table("clients").select("*").range(skip, skip + limit - 1).execute()

    print(f"Get All Clients - Skip: {skip}, Limit: {limit} - Full Response: {response.model_dump_json()}")

    response_dict = response.model_dump()
    data = response_dict.get("data", [])
    
    clients = []
    for item in data:
        # Ensure datetime fields are parsed correctly
        item["created_at"] = datetime.fromisoformat(item["created_at"].replace("Z", "+00:00"))
        item["date_of_birth"] = datetime.fromisoformat(item["date_of_birth"].replace("Z", "+00:00"))
        clients.append(schemas.Client(**item))
        
    return clients

def get_client_profile(client_id: int):
    """
    Fetch the client profile by its ID from the database.
    """
    client = models.Client.query.filter_by(id=client_id).first()
    if client:
        return client
    return None

def search_client_by_phone(phone_number: str) -> List[models.Client]:
    response = supabase.table("clients").select("*").eq("contact_number", phone_number).execute()
    print(f"Search Client by Phone - Number: {phone_number} - Full Response: {response.model_dump_json()}")

    response_dict = response.model_dump()
    data = response_dict.get("data", [])

    if data:
        return [models.Client(**item) for item in data]
    
    raise Exception("User not found.")
