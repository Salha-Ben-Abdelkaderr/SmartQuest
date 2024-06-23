from fastapi import HTTPException
from bson import ObjectId
from app.utils.db import db
from app.models.study import Collaborator

def add_collaborator(study_id: str, collaborator: Collaborator):
    collaborator_data = collaborator.dict()
    result = db.studies.update_one({"study_id": study_id}, {"$push": {"collaborators": collaborator_data}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Study not found")
    return db.studies.find_one({"study_id": study_id})

def remove_collaborator(study_id: str, collaborator_id: str):
    result = db.studies.update_one({"study_id": study_id}, {"$pull": {"collaborators": {"collaborator_id": ObjectId(collaborator_id)}}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Study not found")
    return db.studies.find_one({"study_id": study_id})
