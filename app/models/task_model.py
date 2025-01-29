from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field
from .user_model import User

class Task(Document):
  task_id: UUID = Field(default_factory=uuid4, unique=True)
  status: bool = False
  title: Indexed(str)
  description: Indexed(str)
  created_at: datetime = Field(default_factory=datetime.now)
  updated_at: datetime = Field(default_factory=datetime.now)
  owner: Link[User]
  
  def __repr__(self):
    return f"Task: {self.title}"
  
  def __str__(self):
    return f"{self.title}"
  
  def __hash__(self):
    return hash(self.title)
  
  def __eq__(self, other):
    if not isinstance(other, Task):
      return False
    return self.task_id == other.task_id
  
  @before_event([Replace, Insert])
  def sync_update_at(self):
    self.updated_at = datetime.now()