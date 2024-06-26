from pydantic import BaseModel

class MessageCreate(BaseModel):
    sender_id: str
    recipient_id: str
    study_id: str
    message: str
    timestamp: str

class MessageOut(MessageCreate):
    id: str
