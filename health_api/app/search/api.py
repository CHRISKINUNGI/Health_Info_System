from fastapi import APIRouter, Query, HTTPException, status
from typing import List
from app.clients import schemas  # Reuse the Client schema
from . import services

router = APIRouter()

@router.get("/search/clients", response_model=List[schemas.Client])
def search_clients(
    contact_number: str = Query(..., description="Contact number to search"),
    limit: int = Query(10),
    offset: int = Query(0),
):
    try:
        clients = services.search_clients_by_contact_number(contact_number, limit, offset)

        if not clients:
            raise HTTPException(status_code=404, detail="Client not found.")

        return clients

    except HTTPException as http_exc:
        raise http_exc

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
