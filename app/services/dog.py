from typing import Any, List, Dict, Optional, TypeVar, Union

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.crud.dog import dog
from app.schemas.dog import AdoptDog, CreateDog, Dog, UpdateDog

QueryType = TypeVar("QueryType", bound=CRUDBase)


class DogService:
    def __init__(self, dog_query: QueryType):
        self.__dog_query = dog_query

    async def get_all(
        self,
        payload: Optional[Dict[str, Any]],
        skip: int = 0,
        limit: int = 99999,
        route: Optional[str] = "",
    ) -> Optional[List[Dog]]:
        dogs = await self.__dog_query.get_all(payload=payload, skip=skip, limit=limit)
        return dogs







    async def create_by_name(self, *, dog: CreateDog) -> Union[dict, None]:
        print(dog)
        new_dog_id = await self.__dog_query.create(obj_in=dog)
        return new_dog_id

    async def get_one_by_element(self, **content) -> Union[dict, None]:
        print("++++++++++++++++++++++++++++++++++")
        print(content)
        doggy = await self.__dog_query.get_by_element(**content)
        if doggy:
            return doggy[0]
        return None

    async def get_by_element(self, **content) -> Union[dict, None]:
        doggy = await self.__dog_query.get_by_element(**content)
        if doggy:
            return doggy
        return None

    async def update_by_name(
        self, *, updated_dog: UpdateDog, name: str
    ) -> Union[dict, None]:
        dog_updated = await self.__dog_query.update(name=name, obj_in=updated_dog)
        return dog_updated

    async def adopt(self, *, dog_info: AdoptDog, name: str):
        dog_updated = await self.__dog_query.update(name=name, obj_in=dog_info)
        return dog_updated

    async def delete(self, *, name: str) -> Union[dict, None]:
        deleted_response = await self.__dog_query.delete(name=name)
        return deleted_response


dog_service = DogService(dog_query=dog)
