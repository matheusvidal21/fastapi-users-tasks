from fastapi import APIRouter, Depends
from schemas.task_schema import TaskDetail, TaskCreate
from models.user_model import User
from models.task_model import Task
from api.dependencies.user_deps import get_current_user
from typing import List
from services.task_service import TaskService

task_router = APIRouter()

@task_router.get("/",
                summary='Get all tasks for the current user',
                response_model=List[TaskDetail])
async def list_tasks(user: User = Depends(get_current_user)):
  return await TaskService.list_tasks(user)

@task_router.post("/",
                summary='Create a new task',
                response_model=Task
                )
async def create_task(data: TaskCreate, user: User = Depends(get_current_user)):
  return await TaskService.create_task(data, user)