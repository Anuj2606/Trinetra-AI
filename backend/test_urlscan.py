import asyncio

from app.services.providers.urlscan_provider import URLScanProvider


async def main():

    provider = URLScanProvider()

    result = await provider.analyze(
        "https://google.com"
    )

    print(result)


asyncio.run(main())