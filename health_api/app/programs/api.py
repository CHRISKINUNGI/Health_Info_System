from fastapi import APIRouter, HTTPException, status
from typing import List
from . import models, schemas, services

router = APIRouter()

@router.post("/programs/", response_model=schemas.Program, status_code=status.HTTP_201_CREATED)
def create_program(program: schemas.ProgramCreate):
    
    programs = services.get_all_programs()
    if any(p.program_name == program.program_name for p in programs):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Program with name '{program.program_name}' already exists")
    
    return services.create_new_program(program)

@router.get("/programs/", response_model=List[schemas.Program])
def list_programs(skip: int = 0, limit: int = 10):
    try:
        return services.get_all_programs(skip, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
