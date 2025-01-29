from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from models.user_model import User
from models.task_model import Task
from api.api_v1.router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connecting to database")
    mongo_client = AsyncIOMotorClient(
        str(settings.MONGO_DSN),
        username=settings.MONGO_USER,
        password=settings.MONGO_PASSWORD,
    )
    
    db = mongo_client[settings.DATABASE_NAME]
    
    await init_beanie(
        database=db,
        document_models=[
            User,
            Task
        ]
    )
    
    yield
    
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

app.include_router(
    router, 
    prefix=settings.API_V1_STR
)