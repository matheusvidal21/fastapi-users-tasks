from fastapi import APIRouter, Depends, status, Response
from schemas.task_schema import TaskDetail, TaskCreate, TaskUpdate
from models.user_model import User
from models.task_model import Task
from api.dependencies.user_deps import get_current_user
from typing import List
from services.task_service import TaskService
from uuid import UUID

task_router = APIRouter()

@task_router.get('/',
                summary='Get all tasks for the current user',
                response_model=List[TaskDetail]
                )
async def list(user: User = Depends(get_current_user)):
  return await TaskService.list_tasks(user)

@task_router.get('/{task_id}',
                 summary='Get a task by ID',
                 response_model=TaskDetail
                )
async def get(task_id: UUID, user: User = Depends(get_current_user)):
  return await TaskService.get_task(task_id, user)

@task_router.post('/',
                summary='Create a new task',
                response_model=Task
                )
async def create(data: TaskCreate, user: User = Depends(get_current_user)):
  return await TaskService.create_task(data, user)

@task_router.put('/{task_id}',
                summary='Update a task by ID',
                response_model=Task
                )
async def update(task_id: UUID, data: TaskUpdate, user: User = Depends(get_current_user)):
  return await TaskService.update_task(task_id, data, user)

@task_router.delete('/{task_id}',
                    summary='Delete a task by ID',
                    response_model=Task
                    )
async def delete(task_id: UUID, user: User = Depends(get_current_user)):
  await TaskService.delete_task(task_id, user)
  return Response(status_code=status.HTTP_204_NO_CONTENT)