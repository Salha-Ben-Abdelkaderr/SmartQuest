from pydantic import BaseModel
from typing import List

class StudyBase(BaseModel):
    name: str
    description: str

class StudyCreate(StudyBase):
    pass

class Study(StudyBase):
    id: str
    collaborators: List[str] = []

    class Config:
        orm_mode = True
