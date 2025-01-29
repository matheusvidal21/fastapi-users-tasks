from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class TaskCreate(BaseModel):
  title: str = Field(..., title="Title", min_length=3, max_length=50)
  description: str = Field(..., title="Description", min_length=3, max_length=150)
  status: Optional[bool] = Field(False, title="Status")

class TaskUpdate(BaseModel):
  title: Optional[str] = Field(None, title="Title", min_length=3, max_length=50)
  description: Optional[str] = Field(None, title="Description", min_length=3, max_length=150)
  status: Optional[bool] = Field(None, title="Status")

class TaskDetail(BaseModel):
  task_id: UUID
  title: str
  description: str
  status: bool
  created_at: datetime
  updated_at: datetime