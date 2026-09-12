"""
Shared HTTP Client

Every external API request in Trinetra AI goes through this client.
"""

from typing import Any, Dict, Optional

import httpx

from app.core.exceptions import (
    ExternalServiceUnavailableError,
    ProviderError,
)
from app.core.logger import app_logger


class HTTPClient:

    def __init__(self, timeout: float = 30.0):

        self.client = httpx.AsyncClient(
            timeout=httpx.Timeout(timeout),
            follow_redirects=True,
        )

    async def get(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:

        try:

            response = await self.client.get(
                url,
                headers=headers,
                params=params,
            )

            response.raise_for_status()

            return response.json()

        except httpx.HTTPStatusError as e:

            # URLScan returns 404 while scan is processing
            if e.response.status_code == 404:

                if "not finished" in e.response.text.lower():
                    return None
               

            app_logger.error(
                "HTTP GET provider request failed with status {}",
                e.response.status_code,
            )

            raise ProviderError(
                f"HTTP Error: {e.response.status_code}"
            ) from e

        except httpx.RequestError as e:
            app_logger.error(
                "HTTP GET provider request failed: {}",
                type(e).__name__,
            )
            raise ExternalServiceUnavailableError(
                "Unable to connect to provider"
            ) from e

    async def post(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
    ) -> Dict[str, Any]:

        try:

            response = await self.client.post(
                url,
                headers=headers,
                json=json,
                data=data,
            )

            response.raise_for_status()

            return response.json()

        except httpx.HTTPStatusError as e:

            app_logger.error(
                "HTTP POST provider request failed with status {}",
                e.response.status_code,
            )
            raise ProviderError(
                f"HTTP Error: {e.response.status_code}"
            ) from e

        except httpx.RequestError as e:
            app_logger.error(
                "HTTP POST provider request failed: {}",
                type(e).__name__,
            )

            raise ExternalServiceUnavailableError(
                "Unable to connect to provider"
            ) from e

    async def close(self):

        await self.client.aclose()