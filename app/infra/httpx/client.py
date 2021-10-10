import logging
from typing import Any, Dict, Optional

from httpx._auth import Auth
from httpx._client import AsyncClient
from pydantic import AnyHttpUrl

log = logging.getLogger(__name__)


class HTTPClient:
    async def get(
        self,
        *,
        url_service: AnyHttpUrl,
        timeout: float = 45,
        auth: Optional[Auth] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        cookies: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:

        try:
            async with AsyncClient() as client:
                response = await client.get(
                    url_service,
                    params=params,
                    headers=headers,
                    cookies=cookies,
                    timeout=timeout,
                    auth=auth,
                )
                return response
        except Exception as e:
            log.error(e)
            return None

    async def post(
        self,
        *,
        url_service: AnyHttpUrl,
        timeout: float = 45,
        auth: Optional[Auth] = None,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        cookies: Optional[Dict[str, Any]] = None,
        xml: Optional[bool] = False
    ) -> Optional[Dict[str, Any]]:

        try:
            async with AsyncClient() as client:
                response = await client.post(
                    url_service,
                    params=params,
                    json=body,
                    data=data,
                    headers=headers,
                    cookies=cookies,
                    timeout=timeout,
                    auth=auth,
                )
                return response
        except Exception as e:
            log.error(e)
            return None

    async def put(
        self,
        *,
        url_service: AnyHttpUrl,
        timeout: float = 45,
        auth: Optional[Auth] = None,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        cookies: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:

        try:
            async with AsyncClient() as client:
                response = await client.put(
                    url_service,
                    params=params,
                    json=body,
                    data=data,
                    headers=headers,
                    cookies=cookies,
                    timeout=timeout,
                    auth=auth,
                )
                return response
        except Exception as e:
            log.error(e)
            return None

    async def delete(
        self,
        *,
        url_service: AnyHttpUrl,
        timeout: float = 45,
        auth: Optional[Auth] = None,
        headers: Optional[Dict[str, Any]] = None,
        cookies: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:

        try:
            async with AsyncClient() as client:
                response = await client.delete(
                    url_service,
                    headers=headers,
                    cookies=cookies,
                    timeout=timeout,
                    auth=auth,
                )
                return response
        except Exception as e:
            log.error(e)
            return None

    async def patch(
        self,
        *,
        url_service: AnyHttpUrl,
        timeout: float = 45,
        auth: Optional[Auth] = None,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        cookies: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:

        try:
            async with AsyncClient() as client:
                response = await client.patch(
                    url_service,
                    params=params,
                    json=body,
                    data=data,
                    headers=headers,
                    cookies=cookies,
                    timeout=timeout,
                    auth=auth,
                )
                return response
        except Exception as e:
            log.error(e)
            return None

client: HTTPClient = HTTPClient()