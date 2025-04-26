from fastapi import HTTPException
from postgrest.exceptions import APIError
from app.database import supabase
from app.enrollments import schemas

def create_enrollment(enrollment: schemas.EnrollmentCreate):
    client_id = str(enrollment.client_id)
    program_ids = [str(program_id) for program_id in enrollment.program_ids]  # List of program_ids
    
    # Create the enrollment data for each program
    enrollments_data = [
        {"client_id": client_id, "program_id": program_id}
        for program_id in program_ids
    ]

    try:
        # Insert the data into the enrollments table
        response = supabase.table("enrollments").insert(enrollments_data).execute()

        if not response.data:
            raise Exception("Failed to create enrollment")
        
        created_enrollments = response.data

        # Check for client existence
        client_response = supabase.table("clients").select("*").eq("id", client_id).single().execute()
        if not client_response.data:
            raise HTTPException(status_code=400, detail="Invalid client ID: Client does not exist.")
        
        # Fetch all the programs at once
        program_response = supabase.table("programs").select("*").in_("id", program_ids).execute()
        if not program_response.data:
            raise HTTPException(status_code=400, detail="Invalid program ID: One or more programs do not exist.")

        # Combine program and client information for the created enrollments
        for created_enrollment in created_enrollments:
            created_enrollment["client"] = client_response.data
            created_enrollment["program"] = next(
                (program for program in program_response.data if program["id"] == created_enrollment["program_id"]),
                None
            )
            if created_enrollment["program"] is None:
                raise HTTPException(status_code=400, detail="Program not found for enrollment.")

        return created_enrollments

    except APIError as e:
        # Handle PostgREST specific error (e.g., foreign key constraint violation)
        if "Key (client_id)" in str(e):
            raise HTTPException(status_code=400, detail="Invalid client ID: Client does not exist.")
        raise HTTPException(status_code=500, detail="An unexpected error occurred during enrollment creation.")
    except Exception as e:
        # Handle other errors
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
