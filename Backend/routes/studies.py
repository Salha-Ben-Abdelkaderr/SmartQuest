from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId

from Backend.routes.auth import get_current_user
from ..models.study import Study, StudyCreate
from ..models.user import User
from ..db import get_database

router = APIRouter()

# Create a new study
@router.post("/studies/", response_model=Study)
async def create_study(study: StudyCreate, current_user: User = Depends(get_current_user), db = Depends(get_database)):
    if not current_user.is_owner:
        raise HTTPException(status_code=403, detail="Only owners can create studies")
    
    study_dict = study.dict()
    study_dict["owner_id"] = current_user.id
    result = await db.studies.insert_one(study_dict)
    study.id = str(result.inserted_id)
    return study

# Get all studies
@router.get("/studies/", response_model=List[Study])
async def read_studies(current_user: User = Depends(get_current_user), db = Depends(get_database)):
    if current_user.is_owner:
        studies = await db.studies.find({"owner_id": current_user.id}).to_list(length=100)
    else:
        studies = await db.studies.find({}).to_list(length=100)
    return studies

# Get a study by ID
@router.get("/studies/{study_id}", response_model=Study)
async def read_study(study_id: str, current_user: User = Depends(get_current_user), db = Depends(get_database)):
    study = await db.studies.find_one({"_id": ObjectId(study_id)})
    if study:
        return Study(**study)
    raise HTTPException(status_code=404, detail="Study not found")

# Update a study
@router.put("/studies/{study_id}", response_model=Study)
async def update_study(study_id: str, study: StudyCreate, current_user: User = Depends(get_current_user), db = Depends(get_database)):
    existing_study = await db.studies.find_one({"_id": ObjectId(study_id)})
    if not existing_study:
        raise HTTPException(status_code=404, detail="Study not found")
    if existing_study["owner_id"] != current_user.id:
        raise HTTPException(status_code=403, detail="Only owners can update studies")
    
    study_dict = study.dict()
    await db.studies.update_one({"_id": ObjectId(study_id)}, {"$set": study_dict})
    updated_study = await db.studies.find_one({"_id": ObjectId(study_id)})
    if updated_study:
        return Study(**updated_study)
    raise HTTPException(status_code=404, detail="Study not found")

# Delete a study
@router.delete("/studies/{study_id}", response_model=dict)
async def delete_study(study_id: str, current_user: User = Depends(get_current_user), db = Depends(get_database)):
    existing_study = await db.studies.find_one({"_id": ObjectId(study_id)})
    if not existing_study:
        raise HTTPException(status_code=404, detail="Study not found")
    if existing_study["owner_id"] != current_user.id:
        raise HTTPException(status_code=403, detail="Only owners can delete studies")
    
    deleted_study = await db.studies.find_one_and_delete({"_id": ObjectId(study_id)})
    if deleted_study:
        return {"message": "Study deleted successfully"}
    raise HTTPException(status_code=404, detail="Study not found")
