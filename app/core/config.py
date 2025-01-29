from ctypes import cast
from typing import List
from decouple import config
from pydantic import AnyHttpUrl, MongoDsn
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = str(config("JWT_SECRET_KEY", default="secret"))
    JWT_REFRESH_SECRET_KEY: str = str(config("JWT_REFRESH_SECRET_KEY", default="secret"))
    JWT_ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "TODOFast"
    
    # Database
    MONGO_USER: str = 'root'
    MONGO_PASSWORD: str = 'root'
    MONGO_DSN: MongoDsn = MongoDsn(str(config("MONGO_CONNECTION_STRING")))
    DATABASE_NAME: str = "todoapp"
    
    class Config:
        case_sensitive = True

settings = Settings()