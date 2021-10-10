import logging
from functools import lru_cache

from pydantic import  BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    WEB_APP_TITLE: str
    WEB_APP_DESCRIPTION: str
    WEB_APP_VERSION: str
    SECRET_KEY: str
    ALGORITHM: str
    DATABASE_URL: str = "postgres://postgres:postgres@doggys_db_postgres_container:5432/doggys"
    IMAGE_API: str
    INITIAL_EMAIL: str = "init@mail.com"
    INITIAL_PASSWORD: str = "SecurePassword"
    DATABASE_TEST_URL: str = "sqlite://:memory"
    DEBUGGER: str = "False"
    


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
