from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    phone: str

class UserOut(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    roles: str
    created_at: datetime
    updated_at: datetime
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str