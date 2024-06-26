from pydantic import BaseModel

class DataEntryCreate(BaseModel):
    form_id: str
    field_id: str
    study_id: str
    entered_by: str
    data: dict
    timestamp: str

class DataEntryOut(DataEntryCreate):
    id: str
