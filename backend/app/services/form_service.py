from fastapi import HTTPException
from bson import ObjectId
from app.utils.database import db
from app.models.study import Form

def create_form(study_id: str, form: Form):
    form_data = form.dict()
    result = db.studies.update_one({"study_id": study_id}, {"$push": {"forms": form_data}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Study not found")
    return db.studies.find_one({"study_id": study_id})

def update_form(study_id: str, form_id: str, form_data: dict):
    result = db.studies.update_one(
        {"study_id": study_id, "forms.form_id": form_id},
        {"$set": {"forms.$": form_data}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Form not found")
    return db.studies.find_one({"study_id": study_id})
