import logging

from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import Settings, get_settings
from app.debuger import initialize_fastapi_server_debugger_if_needed
from app.services.db import init_db

log = logging.getLogger("uvicorn.info")


settings: Settings = get_settings()


def create_application() -> FastAPI:
    initialize_fastapi_server_debugger_if_needed()
    application = FastAPI(
        title=settings.WEB_APP_TITLE,
        description=settings.WEB_APP_DESCRIPTION,
        version=settings.WEB_APP_VERSION,
    )
    application.include_router(api_router, prefix="/api")
    return application


app = create_application()


@app.get("/")
def index():
    return {"detail": "index guane app"}


@app.on_event("startup")
async def startup_event():
    init_db(app)
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
