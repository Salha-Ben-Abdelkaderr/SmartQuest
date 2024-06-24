from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: ObjectId
    first_name: str
    last_name: str
    email: EmailStr
    password_hash: str
    phone: str
    created_at: datetime
    updated_at: datetime
    roles: list[str]

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    phone: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
