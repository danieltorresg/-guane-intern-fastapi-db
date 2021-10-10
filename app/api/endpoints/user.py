from typing import List, Optional, Union

from fastapi import APIRouter, HTTPException

from app.schemas.user import CreateUser, UpdateUser, User
from app.services.user import user_service

router = APIRouter()


@router.get(
    "",
    response_model=Union[List[User], None],
    status_code=200,
    responses={
        200: {"description": "Users found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all() -> Optional[List[User]]:
    users = await user_service.get_all()
    if users:
        return users
    else:
        return []


@router.post(
    "",
    response_model=Union[User, None],
    status_code=200,
    responses={
        200: {"description": "Users found"},
        401: {"description": "User unauthorized"},
    },
)
async def create(*, new_user: CreateUser) -> Optional[User]:
    user = await user_service.create(new_user=new_user)
    if user:
        return user
    return []


@router.get(
    "/upload_file",
    response_model=dict,
    status_code=200,
    responses={
        200: {"description": "User found"},
        401: {"description": "User unauthorized"},
    },
)
async def upload_file() -> Optional[dict]:
    response = await user_service.upload_file()
    if response:
        return response
    return None


@router.get(
    "/get_by_email/{email}",
    response_model=Union[User, None],
    status_code=200,
    responses={
        200: {"description": "User found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_one_by_email(*, email: str) -> Optional[User]:
    user = await user_service.get_one_by_email(email=email)
    if user:
        return user
    return None


@router.get(
    "/filter_by_name",
    response_model=Union[List[User], None],
    status_code=200,
    responses={
        200: {"description": "User found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_by_filter_name(*, name: str) -> Optional[User]:
    users = await user_service.get_filter_by_name(name=name)
    if users:
        return users
    else:
        return []


@router.get(
    "/{id}",
    response_model=Union[User, None],
    status_code=200,
    responses={
        200: {"description": "User found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_by_id(*, id: int) -> Optional[User]:
    user = await user_service.get_one_by_id(id=id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.patch(
    "/{id}",
    response_model=Union[User, None],
    status_code=200,
    responses={
        200: {"description": "User found"},
        401: {"description": "User unauthorized"},
    },
)
async def update_by_id(*, id: int, update_user: UpdateUser) -> Optional[User]:
    user = await user_service.update(id=id, updated_user=update_user)
    if user:
        return user
    return None


@router.delete(
    "/{id}",
    response_model=Union[User, None, dict],
    status_code=200,
    responses={
        200: {"description": "User found"},
        401: {"description": "User unauthorized"},
    },
)
async def delete(*, id: int) -> Optional[User]:
    delete_response = await user_service.delete(id=id)
    if delete_response:
        return delete_response
    return None
