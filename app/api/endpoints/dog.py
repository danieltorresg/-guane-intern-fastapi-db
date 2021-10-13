from typing import List, Optional, Union

from fastapi import APIRouter, HTTPException, Query
from fastapi.param_functions import Depends

from app.schemas.dog import AdoptDog, CreateDog, Dog, UpdateDog
from app.services.dog import dog_service
from app.api.params.query import QueryPayloadDog

router = APIRouter()


@router.get(
    "",
    response_model=Union[List[Dog], None],
    status_code=200,
    responses={
        200: {"description": "Dogs found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(
    *,
    doggys_in: QueryPayloadDog = Depends(QueryPayloadDog.as_query),
    skip: int = Query(0),
    limit: int = Query(99999),
) -> Optional[List[Dog]]:
    dogs = await dog_service.get_all(skip=skip, limit=limit, payload=doggys_in.dict(exclude_none=True))
    if dogs:
        return dogs
    else:
        return []


@router.get(
    "/is_adopted",
    response_model=Union[List[Dog], None],
    status_code=200,
    responses={
        200: {"description": "Dogs founds"},
        401: {"description": "User unauthorized"},
    },
)
async def get_is_adopted() -> Optional[Dog]:
    dog = await dog_service.get_by_element(is_adopted=True)
    if dog:
        return dog
    raise HTTPException(status_code=404, detail="Dogs adopted not found")


@router.patch(
    "/adopt/{name}",
    response_model=Union[Dog, None],
    status_code=200,
    responses={
        200: {"description": "Dog adopted"},
        401: {"description": "User unauthorized"},
    },
)
async def adopt(*, name: str, dog_info: AdoptDog) -> Optional[Dog]:
    print(dog_info)
    dog = await dog_service.adopt(dog_info=dog_info, name=name)
    if dog:
        return dog
    raise HTTPException(status_code=404, detail="Dog adopted not found")


@router.get(
    "/{name}",
    response_model=Union[Dog, None],
    status_code=200,
    responses={
        200: {"description": "Dog found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_by_name(*, name: str) -> Optional[Dog]:
    dog = await dog_service.get_one_by_element(name=name)
    if dog:
        return dog
    raise HTTPException(status_code=404, detail="Dog not found")


@router.post(
    "/{name}",
    response_model=Union[Dog, None],
    status_code=200,
    responses={
        200: {"description": "Dog created"},
        401: {"description": "User unauthorized"},
    },
)
async def create_by_name(*, dog_in: CreateDog) -> Optional[Dog]:
    print(dog_in)
    dog = await dog_service.create_by_name(dog=dog_in)
    if dog:
        return dog
    return None


@router.patch(
    "/{name}",
    response_model=Union[Dog, None],
    status_code=200,
    responses={
        200: {"description": "Dog updated"},
        401: {"description": "User unauthorized"},
    },
)
async def update_by_name(
    *,
    dog_in: UpdateDog,
    name: str,
) -> Optional[Dog]:
    dog = await dog_service.update_by_name(updated_dog=dog_in, name=name)
    if dog:
        return dog
    return None


@router.delete(
    "/{name}",
    response_model=Union[Dog, None],
    status_code=200,
    responses={
        200: {"description": "Dog updated"},
        401: {"description": "User unauthorized"},
    },
)
async def delete_by_name(*, name: str) -> Optional[Dog]:
    deleted_response = await dog_service.delete(name=name)
    if deleted_response:
        return deleted_response
    return None
