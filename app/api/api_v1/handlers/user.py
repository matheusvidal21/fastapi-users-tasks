from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserAuth, UserDetail
from services.user_service import UserService
import pymongo

user_router = APIRouter()

@user_router.post('/register', summary='Register a new user', response_model=UserDetail)
async def adiciona_usuario(data: UserAuth):
  try:
    return await UserService.create_user(data)
  except Exception as ex:
    if isinstance(ex, pymongo.errors.DuplicateKeyError):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")