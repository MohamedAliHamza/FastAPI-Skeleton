from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[str] = []

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    class ConfigDict:
        case_sensitive = True


settings = Settings(
    _env_file=".env", 
    PROJECT_NAME="FastAPI Skeleton"
)
