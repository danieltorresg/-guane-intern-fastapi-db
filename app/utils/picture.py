from requests import get

from app.core.config import Settings, get_settings

settings: Settings = get_settings()


def generate_picture():
    response = get(settings.IMAGE_API)

    return response.json()["message"]
