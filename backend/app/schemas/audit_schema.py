from pydantic import BaseModel

class AuditCreate(BaseModel):
    action: str
    user_id: str
    details: str

class AuditOut(AuditCreate):
    id: str
    timestamp: str
