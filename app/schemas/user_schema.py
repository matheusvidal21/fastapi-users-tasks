from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserAuth(BaseModel):
  email: EmailStr = Field(..., description="User email")
  username: str = Field(..., description="Username", min_length=5, max_length=20)
  password: str = Field(..., description="Password", min_length=5, max_length=20)
  
class UserDetail(BaseModel):
  user_id: UUID
  username: str
  email: str