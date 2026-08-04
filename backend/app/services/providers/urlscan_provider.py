"""
URLScan Provider

Submits a URL to URLScan.io and retrieves scan results.
"""

import asyncio

from app.core.config import settings
from app.core.exceptions import InvalidAPIKeyError
from app.core.http_client import HTTPClient
from app.services.providers.base import BaseProvider


class URLScanProvider(BaseProvider):

    SUBMIT_URL = "https://urlscan.io/api/v1/scan/"
    RESULT_URL = "https://urlscan.io/api/v1/result"

    def __init__(self):
        self.client = HTTPClient()

        self.headers = {
            "API-Key": settings.URLSCAN_API_KEY,
            "Content-Type": "application/json",
        }

    async def analyze(self, url: str):

        if not settings.URLSCAN_API_KEY:
            raise InvalidAPIKeyError(
                "URLSCAN_API_KEY not found."
            )

        submit = await self.client.post(
            self.SUBMIT_URL,
            headers=self.headers,
            json={
                "url": url
            },
        )

        uuid = submit["uuid"]

        result = None

        for i in range(30):

            result = await self.client.get(
                f"{self.RESULT_URL}/{uuid}/",
                headers=self.headers,
            )

            if result:
                print("URLScan completed.")
                break

            print(f"Waiting for URLScan... ({i + 1}/30)")

            await asyncio.sleep(2)

        if result is None:
            return {
                "provider": "URLScan",
                "success": False,
                "reason": "Timed out waiting for URLScan."
            }

        page = result.get("page", {})
        task = result.get("task", {})
        verdicts = result.get("verdicts", {})
        lists = result.get("lists", {})
        stats = result.get("stats", {})

        return {

            "provider": "URLScan",

            "success": True,

            "uuid": uuid,

            "url": task.get("url"),

            "final_url": page.get("url"),

            "title": page.get("title"),

            "ip": page.get("ip"),

            "country": page.get("country"),

            "server": page.get("server"),

            "asn": page.get("asn"),

            "screenshot": task.get("screenshotURL"),

            "redirects": stats.get("redirects", 0),

            "malicious": verdicts.get("overall", {}).get(
                "malicious", False
            ),

            "brands": lists.get("brands", []),
        }