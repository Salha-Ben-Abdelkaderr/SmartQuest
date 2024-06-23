from fastapi import APIRouter, HTTPException, Depends
from app.services.audit_service import log_action
from app.models.audit import AuditTrail
from app.schemas.audit_schema import AuditCreate, AuditOut

router = APIRouter(prefix="/audit", tags=["audit"])

@router.post("/", response_model=AuditOut)
def log(audit: AuditCreate):
    return log_action(audit.action, audit.user_id, audit.details)
