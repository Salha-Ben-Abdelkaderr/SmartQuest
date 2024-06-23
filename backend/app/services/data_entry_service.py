from fastapi import HTTPException
from bson import ObjectId
from app.utils.db import db
from app.models.data_entry import DataEntry

def enter_data(data_entry: DataEntry):
    data_entry_data = data_entry.dict()
    result = db.data_entries.insert_one(data_entry_data)
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Data entry failed")
    return db.data_entries.find_one({"_id": result.inserted_id})

def update_data(entry_id: str, data_entry_data: dict):
    result = db.data_entries.update_one({"_id": ObjectId(entry_id)}, {"$set": data_entry_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Data entry not found")
    return db.data_entries.find_one({"_id": ObjectId(entry_id)})
