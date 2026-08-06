"""
Google Safe Browsing Provider

Checks URLs against Google's Safe Browsing database.
"""

from app.core.config import settings
from app.core.exceptions import InvalidAPIKeyError
from app.core.http_client import HTTPClient
from app.services.providers.base import BaseProvider


class SafeBrowsingProvider(BaseProvider):

    BASE_URL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

    def __init__(self):
        self.client = HTTPClient()

    async def analyze(self, url: str):

        if not settings.SAFE_BROWSING_API_KEY:
            raise InvalidAPIKeyError(
                "SAFE_BROWSING_API_KEY not found in .env"
            )

        endpoint = (
            f"{self.BASE_URL}?key={settings.SAFE_BROWSING_API_KEY}"
        )

        payload = {
            "client": {
                "clientId": "TrinetraAI",
                "clientVersion": "1.0"
            },
            "threatInfo": {
                "threatTypes": [
                    "MALWARE",
                    "SOCIAL_ENGINEERING",
                    "UNWANTED_SOFTWARE",
                    "POTENTIALLY_HARMFUL_APPLICATION"
                ],
                "platformTypes": [
                    "ANY_PLATFORM"
                ],
                "threatEntryTypes": [
                    "URL"
                ],
                "threatEntries": [
                    {
                        "url": url
                    }
                ]
            }
        }

        response = await self.client.post(
            endpoint,
            json=payload
        )

        matches = response.get("matches", [])

        return {
            "provider": "Google Safe Browsing",
            "success": True,
            "unsafe": len(matches) > 0,
            "threat_count": len(matches),
            "matches": matches
        }