"""
RDAP Provider

Fetches domain registration information and calculates domain age.
"""

from urllib.parse import urlparse
from datetime import datetime, timezone

from dateutil.parser import parse

from app.core.http_client import HTTPClient
from app.services.providers.base import BaseProvider


class RDAPProvider(BaseProvider):

    BASE_URL = "https://rdap.org/domain"

    def __init__(self):
        self.client = HTTPClient()

    async def analyze(self, url: str):

        domain = urlparse(url).netloc.replace("www.", "")

        response = await self.client.get(
            f"{self.BASE_URL}/{domain}"
        )

        events = response.get("events", [])

        created = None
        expires = None

        for event in events:

            action = event.get("eventAction", "").lower()

            if action == "registration":
                created = event.get("eventDate")

            elif action == "expiration":
                expires = event.get("eventDate")

        age_days = None

        if created:

            created_date = parse(created)

            age_days = (
                datetime.now(timezone.utc) - created_date
            ).days

        registrar = None

        entities = response.get("entities", [])

        if entities:

            registrar = entities[0].get("handle")

        return {

            "provider": "RDAP",

            "success": True,

            "domain": domain,

            "created": created,

            "expires": expires,

            "age_days": age_days,

            "registrar": registrar,

            "status": response.get("status", [])

        }