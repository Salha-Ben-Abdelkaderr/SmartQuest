from pydantic import BaseModel, EmailStr
from typing import Optional
from bson import ObjectId
from datetime import datetime

class User(BaseModel):
    id: ObjectId
    first_name: str
    last_name: str
    email: EmailStr
    password_hash: str
    phone: str
    created_at: datetime
    updated_at: datetime
    roles: str
