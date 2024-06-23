from fastapi import APIRouter, HTTPException, Depends
from app.services.data_entry_service import enter_data, update_data
from app.models.data_entry import DataEntry
from app.schemas.data_entry_schema import DataEntryCreate, DataEntryOut

router = APIRouter(prefix="/data_entries", tags=["data_entries"])

@router.post("/", response_model=DataEntryOut)
def create(data_entry: DataEntryCreate):
    return enter_data(data_entry)

@router.put("/{entry_id}", response_model=DataEntryOut)
def update(entry_id: str, data_entry: DataEntryCreate):
    return update_data(entry_id, data_entry.dict())
