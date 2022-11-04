from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from .models import __beanie_models__, Settings


settings = Settings(_env_file=".env")
app = FastAPI()

@app.on_event("startup")
async def app_init():
    """Initialize application services"""
    client = AsyncIOMotorClient(settings.MONGO_CONNECTION)
    await init_beanie(
        database=client[settings.MONGO_DB], document_models=__beanie_models__
    )
