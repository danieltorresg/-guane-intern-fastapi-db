from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.networks import EmailStr


class BaseUser(BaseModel):
    id: int
    name: str
    last_name: str
    email: EmailStr
    password: str
    is_active: bool = True


class CreateUser(BaseUser):
    pass


class UpdateUser(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    is_active: Optional[bool]


class UserInDB(BaseUser):
    created_date: datetime


class User(UserInDB):
    pass
