from typing import Union

from fastapi import HTTPException
from starlette.responses import Response

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.user import User
from app.schemas.user import CreateUser, UpdateUser


class CRUDUser(CRUDBase[User, CreateUser, UpdateUser]):
    async def create(self, *, obj_in: CreateUser) -> Union[dict, None]:
        user_data = obj_in.dict()
        if await self.get_by_element(email=user_data["email"]):
            raise HTTPException(
                status_code=409, detail="Duplicate key: There is a user with tis data"
            )
        if await self.get_by_element(id=user_data["id"]):
            raise HTTPException(
                status_code=409, detail="Duplicate key: There is a user with tis data"
            )
        user = await self.model.create(**user_data)
        return user

    async def delete(self, *, id: str) -> Union[dict, None]:
        user_to_delete = await self.get_by_element(id=id)
        if user_to_delete:
            user_delete = await self.model.filter(id=id).first().delete()
            status_code = 204 if user_delete == 1 else 404
            return Response(status_code=status_code, content="User deleted")
        else:
            raise HTTPException(
                status_code=404,
                detail="User not found: There is not a user with this id",
            )

    async def update(self, *, id: int, obj_in: UpdateUser) -> Union[dict, None]:
        print(obj_in.dict(exclude_unset=True))
        user_in_db = await self.get_by_element(id=id)
        if user_in_db:
            user_updated = await self.model.filter(id=id).update(
                **obj_in.dict(exclude_unset=True)
            )
            user_updated = await self.get_by_element(id=id)
            return user_updated[0]
        else:
            raise HTTPException(
                status_code=404,
                detail="User not found: There is not a user with this id",
            )

    async def get_filter_by_name(self, *, name: str):
        users = await self.model.filter(name__icontains=name)
        return users


user = CRUDUser(User)
