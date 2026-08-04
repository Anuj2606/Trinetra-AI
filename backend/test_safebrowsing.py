import asyncio

from app.services.providers.safebrowsing_provider import SafeBrowsingProvider


async def main():

    provider = SafeBrowsingProvider()

    result = await provider.analyze(
        "https://google.com"
    )

    print(result)


asyncio.run(main())