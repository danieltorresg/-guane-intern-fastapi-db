from typing import Any, Dict, List, Optional, TypeVar, Union

from fastapi.exceptions import HTTPException
from passlib.hash import bcrypt

from app.core.config import Settings, get_settings
from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.crud.user import user
from app.schemas.user import CreateUser, UpdateUser, User

QueryType = TypeVar("QueryType", bound=CRUDBase)


settings: Settings = get_settings()


class UserService:
    def __init__(self, user_query: QueryType):
        self.__user_query = user_query

    async def get_all(
        self,
        payload: Optional[Dict[str, Any]],
        skip: int = 0,
        limit: int = 99999,
        route: Optional[str] = "",
    ) -> Optional[List[User]]:
        users = await self.__user_query.get_all(payload=payload, skip=skip, limit=limit)
        return users

    async def create(self, new_user: CreateUser) -> Optional[User]:
        new_user.password = bcrypt.hash(new_user.password)
        user = await self.__user_query.create(obj_in=new_user)
        return user

    async def get_one_by_id(self, *, id: int) -> Union[dict, None]:
        user = await self.__user_query.get_by_element(id=id)
        if user:
            return user[0]
        return None

    async def get_one_by_email(self, *, email: str) -> Union[dict, None]:
        user = await self.__user_query.get_by_element(email=email)
        if user:
            return user[0]
        raise HTTPException(
            status_code=404,
            detail="User not found: There is not a user with this email",
        )

    async def update(self, *, id: int, updated_user: UpdateUser) -> Union[dict, None]:
        if updated_user.password:
            updated_user.password = bcrypt.hash(updated_user.password)
        print(updated_user)
        user_updated = await self.__user_query.update(id=id, obj_in=updated_user)
        return user_updated

    async def deactivate(self, *, id: int) -> Union[dict, None]:
        deactivate = UpdateUser(is_active=False)
        user_updated = await self.__user_query.update(id=id, obj_in=deactivate)
        return user_updated

    async def delete(self, *, id: int) -> Union[dict, None]:
        delete_response = await self.__user_query.delete(id=id)
        return delete_response

    async def get_filter_by_name(self, *, name: str) -> Union[dict, None]:
        user = await self.__user_query.get_filter_by_name(name=name)
        if user:
            return user
        return None


user_service = UserService(user_query=user)
