from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.networks import EmailStr


class BaseDog(BaseModel):
    id: int
    owner_email: Optional[EmailStr]


class CreateDog(BaseModel):
    id: int
    name: str
    picture: str
    in_charge_id: Optional[int]
    owner_id: Optional[int]


class UpdateDog(BaseModel):
    name: Optional[str]
    picture: Optional[str]


class AdoptDog(BaseModel):
    owner_id: int
    is_adopted: bool
    in_charge_id: Optional[int]


class DogInDB(CreateDog):
    created_date: datetime
    is_adopted: bool

class PayloadDog(BaseModel):
    name: Optional[str]
    owner_id: Optional[int]
    in_charge_id: Optional[int]
    is_adopted: Optional[bool]


class Dog(DogInDB):
    pass
