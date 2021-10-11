from typing import Union

from fastapi import HTTPException
from starlette.responses import Response

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.dog import Dog
from app.schemas.dog import AdoptDog, CreateDog, UpdateDog
from app.services.user import user_service


class CRUDDog(CRUDBase[Dog, CreateDog, UpdateDog]):
    async def create(self, *, obj_in: CreateDog) -> Union[dict, None]:
        dog_data = obj_in.dict()
        if await self.get_by_element(name=dog_data["name"]):
            raise HTTPException(
                status_code=409, detail="Duplicate key: There is a dog with this data"
            )
        if await self.get_by_element(id=dog_data["id"]):
            raise HTTPException(
                status_code=409, detail="Duplicate key: There is a dog with this data"
            )

        if type(dog_data["in_charge_id"]) == int:
            if not await user_service.get_one_by_id(id=dog_data["in_charge_id"]):
                raise HTTPException(status_code=409, detail="This dog is not yours")
        if type(dog_data["owner_id"]) == int:
            if not await user_service.get_one_by_id(id=dog_data["owner_id"]):
                raise HTTPException(
                    status_code=409, detail="User not found: Invalid owner id"
                )
            dog_data["is_adopted"] = True
        else:
            dog_data["is_adopted"] = False
        dog = await self.model.create(**dog_data)
        return dog

    async def delete(self, *, name: str) -> Union[dict, None]:
        dog_deleted = await self.get_by_element(name=name)
        if dog_deleted:
            dog_deleted = await self.model.filter(name=name).first().delete()
            status_code = 204 if dog_deleted == 1 else 404
            return Response(status_code=status_code)
        else:
            raise HTTPException(
                status_code=404,
                detail="Dog not found: There is not a dog with this id",
            )

    async def update(
        self, *, name: str, obj_in: Union[UpdateDog, AdoptDog]
    ) -> Union[dict, None]:
        dog_in_db = await self.get_by_element(name=name)
        dog_updated = await self.model.filter(name=name).update(
            **obj_in.dict(exclude_unset=True)
        )
        dog_updated = await self.get_by_element(id=dog_in_db[0]["id"])
        return dog_updated[0]


dog = CRUDDog(Dog)
