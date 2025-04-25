from ..database import supabase
from . import models, schemas

def create_new_program(program: schemas.ProgramCreate) -> models.Program:
    new_program = {
        "program_name": program.program_name,
        "description": program.description
    }
    response = supabase.table("programs").insert(new_program).execute()
    print(f"Create Program - Full Response: {response.model_dump_json()}")

    # Check if response data is present
    if not response.data:
        raise Exception(f"Supabase Error: {response.error if response.error else 'Unknown error occurred'}")

    data = response.data
    if len(data) > 0:
        return models.Program(**data[0])
    raise Exception("No data returned when creating program.")

def get_all_programs(skip=0, limit=10) -> list[models.Program]:
    response = supabase.table("programs").select("*").range(skip, skip + limit - 1).execute()
    print(f"Get All Programs - Full Response: {response.model_dump_json()}")

    # Check if response data is present
    if not response.data:
        raise Exception(f"Supabase Error: {response.error if response.error else 'Unknown error occurred'}")

    return [models.Program(**item) for item in response.data]
