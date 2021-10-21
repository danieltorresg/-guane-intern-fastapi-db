import asyncio
import os
import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer
from app.core.config import Settings, get_settings
from app.main import create_application
def get_settings_override():
    return Settings(
        TESTING=1, DEBUGGER=True, DATABASE_TEST_URL="sqlite://:memory"
    )
@pytest.fixture(scope="function", autouse=True)
def test_app():
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    initializer(
        ["app.infra.postgres.models"],
        db_url="sqlite://:memory",
    )
    with TestClient(app) as test_client:
        yield test_client
    finalizer()
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
