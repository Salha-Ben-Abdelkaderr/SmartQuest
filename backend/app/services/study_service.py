from fastapi import HTTPException
from bson import ObjectId
from app.utils.db import db
from app.models.study import Study

def create_study(study: Study):
    study_data = study.dict()
    result = db.studies.insert_one(study_data)
    created_study = db.studies.find_one({"_id": result.inserted_id})
    return

def get_study(study_id: str):
    study = db.studies.find_one({"study_id": study_id})
    if not study:
        raise HTTPException(status_code=404, detail="Study not found")
    return study

def update_study(study_id: str, study_data: dict):
    result = db.studies.update_one({"study_id": study_id}, {"$set": study_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Study not found")
    return db.studies.find_one({"study_id": study_id})
