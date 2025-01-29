from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService
from core.security import create_access_token, create_refresh_token
from schemas.auth_schema import TokenSchema
from schemas.user_schema import UserDetail
from models.user_model import User
from api.dependencies.user_deps import get_current_user

auth_router = APIRouter()

@auth_router.post("/login",
                  summary="Login to get access token",
                  response_model=TokenSchema
                  )
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
  user = await UserService.authenticate(email=data.username, password=data.password)
  
  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="E-mail or password is incorrect",
    )
  
  return {
    "access_token": create_access_token(user.user_id),
    "refresh_token": create_refresh_token(user.user_id)
  }
  
@auth_router.post(
                  "/test-token", 
                  summary="Test access token", 
                  response_model=UserDetail
                  )
async def test_token(user: User = Depends(get_current_user)):
  return user