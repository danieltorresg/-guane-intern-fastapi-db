from fastapi import APIRouter

from app.api.endpoints import dog, login, user

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(dog.router, prefix="/dogs", tags=["dog"])
api_router.include_router(user.router, prefix="/users", tags=["user"])
