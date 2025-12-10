import os
from typing import List, Optional
from pydantic_settings import BaseSettings 
from pydantic import PostgresDsn, validator
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__),'..','..','.env'))
class Settings (BaseSettings):
    #Основные настройки проекта 
    PROJECT_NAME: str="Task Manager"
    VERSION: str = '/api/v1'
    DEBUG : bool = False

    # PostgreSQL настройки (которые наследуются из .env)
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = 'localhost'
    POSTGRES_PORT= '5432'
    POSTGRES_DB: str

    #пОЛНЫЙ urL ДЛЯ ПОДКЛЮЧЕНИЯ 
    DATABASE_URL: Optional[PostgresDsn] = None
    @validator("DATABASE_URL", pre=True)
    def assemble_db_connection(cls, v:Optional[str], values):
        if isinstance(v, str):
            return v
        return PostgresDsn.build()
    

    