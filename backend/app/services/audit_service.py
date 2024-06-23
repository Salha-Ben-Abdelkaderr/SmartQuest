import datetime
from fastapi import HTTPException
from bson import ObjectId
from app.utils.db import db
from app.models.audit import AuditTrail

def log_action(action: str, user_id: ObjectId, details: str):
    audit_entry = AuditTrail(action=action, user_id=user_id, timestamp=str(datetime.utcnow()), details=details)
    result = db.audit_trail.insert_one(audit_entry.dict())
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Logging failed")
    return audit_entry
