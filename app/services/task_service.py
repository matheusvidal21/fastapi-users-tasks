from models.user_model import User
from models.task_model import Task
from typing import List
from schemas.task_schema import TaskCreate, TaskUpdate
from uuid import UUID

class TaskService:
  @staticmethod
  async def list_tasks(user: User) -> List[Task]:
    return await Task.find(Task.owner.id == user.id).to_list()
    
  @staticmethod
  async def create_task(data: TaskCreate, user: User) -> Task:
    task = Task(**data.dict(), owner=user)
    return await task.insert()
  
  @staticmethod
  async def get_task(task_id: UUID, user: User) -> Task:
    return await Task.find_one(Task.owner.id == user.id, Task.task_id == task_id)
  
  @staticmethod
  async def update_task(task_id: UUID, data: TaskUpdate, user: User) -> Task:
    task = await TaskService.get_task(task_id, user)
    if task:
      update_data = data.dict(exclude_unset=True)
      await task.update({'$set': update_data})
      return await task.save()
    return None
  
  @staticmethod
  async def delete_task(task_id: UUID, user: User) -> None:
    task = await TaskService.get_task(task_id, user)
    if task:
      await task.delete()
    return None