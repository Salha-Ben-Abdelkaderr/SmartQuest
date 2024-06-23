from fastapi import APIRouter, HTTPException, Depends
from app.services.form_service import create_form, update_form
from app.models.study import Form
from app.schemas.study_schema import FormCreate, FormOut

router = APIRouter(prefix="/forms", tags=["forms"])

@router.post("/{study_id}", response_model=FormOut)
def create(study_id: str, form: FormCreate):
    return create_form(study_id, form)

@router.put("/{study_id}/{form_id}", response_model=FormOut)
def update(study_id: str, form_id: str, form: FormCreate):
    return update_form(study_id, form_id, form.dict())
