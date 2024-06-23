from pydantic import BaseModel, EmailStr
from typing import Optional
from bson import ObjectId

class User(BaseModel):
    id: Optional[ObjectId]
    name: str
    first_name: str
    email: EmailStr
    phone: str
    password: str
    user_id: str
    role: str  # "owner" or "collaborator"
