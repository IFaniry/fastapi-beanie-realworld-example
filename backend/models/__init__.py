from pydantic import BaseSettings

from .user import User
from .article import Article


class Settings(BaseSettings):
    """Server config settings"""

    # MongoDB
    MONGO_CONNECTION: str
    MONGO_DB = "demo_app_db"

# All models to instantiate on load
__beanie_models__ = [User, Article]
