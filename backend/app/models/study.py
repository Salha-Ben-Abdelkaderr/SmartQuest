from pydantic import BaseModel
from typing import List, Optional
from bson import ObjectId

class Field(BaseModel):
    field_id: str
    field_type: str
    field_name: str
    lower_limit: Optional[float]
    upper_limit: Optional[float]

class Form(BaseModel):
    form_id: str
    form_name: str
    fields: List[Field]

class Collaborator(BaseModel):
    collaborator_id: ObjectId
    role: str  # "co-owner" or "investigator"

class Study(BaseModel):
    id: Optional[ObjectId]
    study_id: str
    title: str
    description: str
    owner_id: ObjectId
    forms: List[Form]
    is_active: bool
    collaborators: List[Collaborator]
    audit_trail: List[dict]
