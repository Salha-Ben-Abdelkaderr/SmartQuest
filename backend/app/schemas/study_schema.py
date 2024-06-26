from pydantic import BaseModel
from typing import List, Optional

class FieldCreate(BaseModel):
    field_id: str
    field_type: str
    field_name: str
    lower_limit: Optional[float]
    upper_limit: Optional[float]

class FormCreate(BaseModel):
    form_id: str
    form_name: str
    fields: List[FieldCreate]

class CollaboratorCreate(BaseModel):
    collaborator_id: str
    role: str  # "co-owner" or "investigator"

class StudyCreate(BaseModel):
    study_id: str
    title: str
    description: str
    owner_id: str
    forms: List[FormCreate]
    is_active: bool
    collaborators: List[CollaboratorCreate]
    audit_trail: List[dict]

class StudyOut(StudyCreate):
    id: str
