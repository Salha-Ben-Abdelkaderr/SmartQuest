from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class Message(BaseModel):
    id: Optional[ObjectId]
    sender_id: ObjectId
    receiver_id: ObjectId
    study_id: ObjectId
    message: str
    timestamp: str
