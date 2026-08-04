import asyncio

from app.services.providers.rdap_provider import RDAPProvider


async def main():

    provider = RDAPProvider()

    result = await provider.analyze(
        "https://google.com"
    )

    print(result)


asyncio.run(main())