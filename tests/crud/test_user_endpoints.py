import asyncio
from typing import List
from app.services.user import user
from app.schemas.user import CreateUser
from app.infra.postgres.models import User


user_default: CreateUser = CreateUser(
    id = 1,
    name = "Daniel",
    last_name = "Torres",
    email = "mail1@mail.com",
    password = "hola"
)


def test_create_user(event_loop: asyncio.AbstractEventLoop):
    created_user = create_user(event_loop, user_default)
    assert isinstance(created_user, User)
    assert created_user.__dict__.items() >= user_default.__dict__.items()


def test_get_users(event_loop: asyncio.AbstractEventLoop):
    create_some_users(event_loop)
    users: List[dict] = event_loop.run_until_complete(user.get_all())
    assert isinstance(users, list)
    del users[0]["created_date"]
    assert users[0].items() <= user_default.__dict__.items()



def create_user(event_loop: asyncio.AbstractEventLoop, user_to_create: CreateUser):
    created_user = event_loop.run_until_complete(user.create(obj_in=user_to_create))
    return created_user

def create_some_users(event_loop: asyncio.AbstractEventLoop):
    for i in range(1,5):
        user_default: CreateUser = CreateUser(
            id = i,
            name = "Daniel",
            last_name = "Torres",
            email = f"mail{i}@mail.com",
            password = "hola"
        )
        create_user(event_loop, user_default)

