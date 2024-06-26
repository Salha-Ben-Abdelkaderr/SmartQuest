from fastapi import HTTPException
from bson import ObjectId
from app.utils.db import db
from app.utils.security import get_password_hash
from app.models.user import User

def create_user(user_data: dict):
    user_data["password"] = get_password_hash(user_data["password"])
    result = db.users.insert_one(user_data)
    created_user = db.users.find_one({"_id": result.inserted_id})
    return created_user

def get_user_by_email(email: str):
    user = db.users.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
