from fastapi import APIRouter, HTTPException, Depends
from app.services.study_service import create_study, get_study, update_study
from app.models.study import Study
from app.schemas.study_schema import StudyCreate, StudyOut

router = APIRouter(prefix="/studies", tags=["studies"])

@router.post("/", response_model=StudyOut)
def create(study: StudyCreate):
    return create_study(study)

@router.get("/{study_id}", response_model=StudyOut)
def read(study_id: str):
    return get_study(study_id)

@router.put("/{study_id}", response_model=StudyOut)
def update(study_id: str, study: StudyCreate):
    return update_study(study_id, study.dict())
