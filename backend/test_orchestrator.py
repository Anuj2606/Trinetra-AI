import asyncio

from app.services.orchestrator import ScanOrchestrator


async def main():

    orchestrator = ScanOrchestrator()

    result = await orchestrator.analyze(

        "https://google.com"

    )

    print(result)


asyncio.run(main())