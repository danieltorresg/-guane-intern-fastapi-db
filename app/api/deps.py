from fastapi import HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError

from app.core.config import Settings, get_settings
from app.infra.postgres.models.user import User
from app.schemas.token import TokenPayload
from app.services.user import user_service

settings: Settings = get_settings()

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/login/token")


async def get_current_user(
    token: str = Security(reusable_oauth2),
) -> User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = await user_service.get_one_by_id(id=token_data.id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(
    current_user=Security(get_current_user),
):
    if not current_user["is_active"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user",
        )
    return current_user
