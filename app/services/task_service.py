from models.user_model import User
from models.task_model import Task
from typing import List
from schemas.task_schema import TaskCreate

class TaskService:
  @staticmethod
  async def list_tasks(user: User) -> List[Task]:
    return await Task.find(Task.owner.id == user.id).to_list()
    
  @staticmethod
  async def create_task(data: TaskCreate, user: User) -> Task:
    task = Task(**data.dict(), owner=user)
    return await task.insert()
  