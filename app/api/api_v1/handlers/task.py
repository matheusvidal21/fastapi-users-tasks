from fastapi import APIRouter, Depends
from schemas.task_schema import TaskDetail
from models.user_model import User
from api.dependencies.user_deps import get_current_user
from typing import List

task_router = APIRouter()

@task_router.get("/",
                summary='Get all tasks for the current user',
                response_model=List[TaskDetail])
async def teste(user: User = Depends(get_current_user)):
  pass