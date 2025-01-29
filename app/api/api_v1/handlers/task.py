from fastapi import APIRouter

task_router = APIRouter()

@task_router.get("/")
async def teste():
  pass