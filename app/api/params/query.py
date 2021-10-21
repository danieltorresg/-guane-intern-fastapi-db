from datetime import datetime
from typing import Optional

from fastapi import Query
from pydantic.networks import EmailStr

from app import schemas


class QueryPayloadDog(schemas.dog.PayloadDog):
    @classmethod
    async def as_query(
        cls,
        name: Optional[str] = Query(None),
        owner_id: Optional[int] = Query(None),
        in_charge_id: Optional[int] = Query(None),
        is_adopted: Optional[bool] = Query(None),
    ):
        return cls(
            name=name,
            owner_id=owner_id,
            in_charge_id=in_charge_id,
            is_adopted=is_adopted,
        )


class QueryPayloadUser(schemas.user.PayloadUser):
    @classmethod
    async def as_query(
        cls,
        name: Optional[str] = Query(None),
        last_name: Optional[str] = Query(None),
        email: Optional[EmailStr] = Query(None),
        is_active: Optional[bool] = Query(None),
        created_date: Optional[datetime] = Query(None),
    ):
        return cls(
            name=name,
            last_name=last_name,
            email=email,
            is_active=is_active,
            created_date=created_date,
        )
