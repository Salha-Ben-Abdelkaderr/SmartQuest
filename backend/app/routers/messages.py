from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.services.message_service import send_message, get_messages
from app.schemas.message_schema import MessageCreate, MessageOut

router = APIRouter(prefix="/messages", tags=["messages"])

@router.post("/", response_model=MessageOut)
def send(message: MessageCreate):
    return send_message(message)

@router.get("/{study_id}", response_model=List[MessageOut])
def read(study_id: str):
    return get_messages(study_id)
