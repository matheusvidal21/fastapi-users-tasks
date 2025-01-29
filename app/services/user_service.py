from models.user_model import User
from schemas.user_schema import UserAuth
from core.security import get_hash_password, verify_password
from typing import Optional
from uuid import UUID

class UserService:
  
  @staticmethod
  async def create_user(user: UserAuth):
    try:
      user = User(
        username = user.username,
        email = user.email,
        hash_password = get_hash_password(user.password)
      )
      await user.save()
      return user
    except DuplicateKeyError:
      raise
      
  @staticmethod
  async def get_user_by_id(id: UUID) -> Optional[User]:
    return await User.find_one(User.user_id == id)
      
  @staticmethod
  async def get_user_by_email(email: str) -> Optional[User]:
    return await User.find_one(User.email == email)
      
  @staticmethod
  async def authenticate(email: str, password: str) -> Optional[User]:
    user = await UserService.get_user_by_email(email)
    if not user:
      return None
    if not verify_password(password, user.hash_password):
      return None
    return user        