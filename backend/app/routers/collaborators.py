from fastapi import APIRouter, HTTPException, Depends
from app.services.collaborator_service import add_collaborator, remove_collaborator
from app.models.study import Collaborator
from app.schemas.study_schema import CollaboratorCreate, CollaboratorOut

router = APIRouter(prefix="/collaborators", tags=["collaborators"])

@router.post("/{study_id}", response_model=CollaboratorOut)
def add(study_id: str, collaborator: CollaboratorCreate):
    return add_collaborator(study_id, collaborator)

@router.delete("/{study_id}/{collaborator_id}", response_model=CollaboratorOut)
def remove(study_id: str, collaborator_id: str):
    return remove_collaborator(study_id, collaborator_id)
