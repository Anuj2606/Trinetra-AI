import asyncio

from app.services.providers.gemini_provider import GeminiProvider


async def main():

    provider = GeminiProvider()

    result = await provider.analyze(

        {
            "risk_score":15,

            "risk_level":"LOW",

            "confidence":95,

            "reasons":[

                "Domain is trusted",

                "No malicious detections",

                "Google Safe Browsing reports safe"

            ]

        }

    )

    print(result["analysis"])


asyncio.run(main())