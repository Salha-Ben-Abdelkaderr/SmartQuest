from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import List

app = FastAPI()

# MongoDB connection
client = AsyncIOMotorClient('mongodb://localhost:27017')
db = client.mydatabase
collection = db.mycollection

class Item(BaseModel):
    name: str
    description: str
    price: float

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    result = await collection.insert_one(item.dict())
    if result.inserted_id:
        return item
    raise HTTPException(status_code=400, detail="Failed to insert item")

@app.get("/items/", response_model=List[Item])
async def read_items():
    items = await collection.find().to_list(100)
    return items

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    item = await collection.find_one({"_id": item_id})
    if item is not None:
        return item
    raise HTTPException(status_code=404, detail="Item not found")