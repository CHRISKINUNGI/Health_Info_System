from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query, status
import supabase
from uuid import UUID
from . import schemas, services, models

router = APIRouter()

@router.post("/clients/", response_model=schemas.Client, status_code=status.HTTP_201_CREATED)
def register_client(client: schemas.ClientCreate):
    try:
        return services.create_new_client(client)
    except Exception as e:
        error_detail = str(e)
        if "duplicate key value violates unique constraint" in error_detail.lower():
            if "contact_number" in error_detail.lower():
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"Client with contact number '{client.contact_number}' already exists."
                )
        elif "already exists" in error_detail.lower():  # Handling duplicate name from service
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=error_detail
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=error_detail
            )
            
@router.get("/clients/", response_model=List[schemas.Client])
def list_all_clients(skip: int = Query(0, description="Number of clients to skip"), limit: int = Query(100, description="Maximum number of clients to retrieve")):
    """
    Retrieves a list of all registered clients with optional pagination.
    """
    try:
        return services.get_all_clients(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
 
@router.get("/clients/{client_id}", response_model=schemas.Client)
def get_client_profile(client_id: str):
    """
    Retrieve a client profile using the client ID.
    """
    try:
        client = services.get_client_profile(client_id)
        
        if client is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Client with ID '{client_id}' not found."
            )
        
        return client

    except HTTPException as http_ex:
        # Re-raise the HTTPException so FastAPI can handle it properly
        raise http_ex

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )

@router.get("/clients/search_by_phone/{phone_number}", response_model=List[schemas.Client])
def search_client_by_phone(phone_number: int):
    """
    Retrieves client details based on phone number.
    """
    try:
        clients = services.search_client_by_phone(phone_number)
        if not clients:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Client with phone number '{phone_number}' not found."
            )
        return clients
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
