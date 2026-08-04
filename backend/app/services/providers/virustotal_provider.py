"""
VirusTotal Provider

Handles URL reputation analysis using the VirusTotal v3 API.
"""

import asyncio
import base64

from app.core.config import settings
from app.core.exceptions import (
    InvalidAPIKeyError,
)
from app.core.http_client import HTTPClient
from app.services.providers.base import BaseProvider


class VirusTotalProvider(BaseProvider):

    BASE_URL = "https://www.virustotal.com/api/v3"

    def __init__(self):

        self.client = HTTPClient()

        self.headers = {
            "x-apikey": settings.VIRUSTOTAL_API_KEY
        }

    async def analyze(self, url: str):

        if not settings.VIRUSTOTAL_API_KEY:

            raise InvalidAPIKeyError(
                "VirusTotal API Key not found."
            )

        # -------------------------
        # STEP 1
        # Submit URL
        # -------------------------

        submit = await self.client.post(

            f"{self.BASE_URL}/urls",

            headers=self.headers,

            data={
                "url": url
            }

        )

        analysis_id = submit["data"]["id"]

        # Give VirusTotal a little time
        await asyncio.sleep(3)

        # -------------------------
        # STEP 2
        # Retrieve Report
        # -------------------------

        encoded_url = base64.urlsafe_b64encode(
            url.encode()
        ).decode().strip("=")

        report = await self.client.get(

            f"{self.BASE_URL}/urls/{encoded_url}",

            headers=self.headers

        )

        stats = report["data"]["attributes"]["last_analysis_stats"]

        attributes = report["data"]["attributes"]

        return {

            "provider": "VirusTotal",

            "success": True,

            "analysis_id": analysis_id,

            "stats": stats,

            "reputation": attributes.get("reputation", 0),

            "categories": attributes.get("categories", {}),

            "last_analysis_date": attributes.get("last_analysis_date"),

            "last_final_url": attributes.get("last_final_url"),

            "times_submitted": attributes.get("times_submitted", 0),

            "threat_names": attributes.get("threat_names", []),

            "votes": attributes.get("total_votes", {}),

            "harmless": stats.get("harmless", 0),

            "malicious": stats.get("malicious", 0),

            "suspicious": stats.get("suspicious", 0),

            "undetected": stats.get("undetected", 0)

        }