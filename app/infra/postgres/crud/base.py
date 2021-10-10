from typing import Generic, List, TypeVar, Union

from pydantic import BaseModel
from tortoise import models

ModelType = TypeVar("ModelType", bound=models.Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: ModelType):
        self.model = model

    async def get_all(
        self,
        *,
        content: dict = None,
        skip: int = 0,
        limit: int = 50,
    ) -> List:
        if content:
            model = (
                await self.model.filter(**content)
                .offset(skip)
                .limit(limit)
                .all()
                .values()
            )
        else:
            model = await self.model.all().offset(skip).limit(limit).values()
        return model

    async def create(self, *, obj_in: CreateSchemaType) -> Union[dict, None]:
        obj_in_data = obj_in.dict()
        model = self.model(**obj_in_data)
        await model.save()
        return model

    async def get_by_element(self, **content) -> Union[dict, None]:
        model = await self.model.all().filter(**content).values()
        if model:
            return model
        return None

    async def update(self, *, id: int, obj_in: UpdateSchemaType) -> Union[dict, None]:
        model = await self.get_by_element(id=id)
        if model:
            model_updated = await self.model.filter(id=id).update(
                **obj_in.dict(exclude_unset=True)
            )
            model_updated = await self.get_by_element(id=id)
            return model_updated[0]
        else:
            return None

    async def delete(self, *, id: int) -> None:
        await self.model.filter(id=id).first().delete()
        return None


crud: CRUDBase = CRUDBase(CRUDBase)
