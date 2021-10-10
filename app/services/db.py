import logging

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.core.config import Settings, get_settings

settings: Settings = get_settings()

log = logging.getLogger("uvicorn.info")  # new


def init_db(app: FastAPI) -> None:
    db_url = settings.DATABASE_URL
    log.info(f"connected to the database {db_url}")
    register_tortoise(
        app,
        db_url=db_url,
        modules={"models": ["app.infra.postgres.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
