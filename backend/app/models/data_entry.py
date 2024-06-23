from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class DataEntry(BaseModel):
    id: Optional[ObjectId]
    form_id: str
    field_id: str
    study_id: ObjectId
    entered_by: ObjectId
    data: dict
    timestamp: str
