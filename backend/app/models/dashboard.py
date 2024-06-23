from pydantic import BaseModel
from typing import List, Optional
from bson import ObjectId

class CollaboratorEntryCount(BaseModel):
    collaborator_id: ObjectId
    entry_count: int

class TimeBasedMetric(BaseModel):
    date: str
    entry_count: int

class DashboardMetrics(BaseModel):
    study_id: ObjectId
    total_entries: int
    total_participants: int
    entries_per_collaborator: List[CollaboratorEntryCount]
    time_based_metrics: List[TimeBasedMetric]
