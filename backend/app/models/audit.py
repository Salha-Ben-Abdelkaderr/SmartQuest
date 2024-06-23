from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class AuditTrail(BaseModel):
    id: Optional[ObjectId]
    action: str
    user_id: ObjectId
    timestamp: str
    details: str
