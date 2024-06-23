from fastapi import HTTPException
from bson import ObjectId
from app.utils.db import db
from app.models.message import Message

def send_message(message: Message):
    message_data = message.dict()
    result = db.messages.insert_one(message_data)
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Message sending failed")
    return db.messages.find_one({"_id": result.inserted_id})

def get_messages(study_id: str):
    messages = db.messages.find({"study_id": study_id})
    return list(messages)
