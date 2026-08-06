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
               

            print("\n========== HTTP GET ERROR ==========")
            print("URL:", e.request.url)
            print("Status:", e.response.status_code)
            print("Response:", e.response.text)

            raise ProviderError(
                f"HTTP Error: {e.response.status_code}"
            ) from e

        except httpx.RequestError as e:

            print("\n========== REQUEST ERROR ==========")
            print(e)
            print("===================================\n")

            raise ExternalServiceUnavailableError(
                f"Unable to connect to {url}"
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

            print("\n========== HTTP POST ERROR ==========")
            print("URL:", e.request.url)
            print("Status:", e.response.status_code)
            print("Headers:", dict(e.request.headers))
            print("Request JSON:", json)
            print("Response:", e.response.text)
            print("=====================================\n")

            raise ProviderError(
                f"HTTP Error: {e.response.status_code}"
            ) from e

        except httpx.RequestError as e:

            print("\n========== REQUEST ERROR ==========")
            print(e)
            print("===================================\n")

            raise ExternalServiceUnavailableError(
                f"Unable to connect to {url}"
            ) from e

    async def close(self):

        await self.client.aclose()