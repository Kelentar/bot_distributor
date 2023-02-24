from typing import Optional, Dict, Any

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    TOKEN: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str = '5432'
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DEVAPI_ROOT: str
    ADMIN_ROOT: str
    TASK_ROOT: str
    ASSISTANT_ROOT: str
    CHAT_ROOT: str
    SUPERUSER_CHAT: str
    ASSIST_TOKEN: str
    SQLALCHEMY_DATABASE_URL: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URL", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )
    class Config:
        env_file = 'dev.env'


settings = Settings()
