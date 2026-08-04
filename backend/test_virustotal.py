import asyncio

from app.services.providers.virustotal_provider import VirusTotalProvider


async def main():

    provider = VirusTotalProvider()

    result = await provider.analyze(

        "https://google.com"

    )

    print(result)


asyncio.run(main())