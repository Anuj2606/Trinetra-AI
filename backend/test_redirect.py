import asyncio
import httpx

async def resolve_url():
    url = "http://twitter.com/QAzADgAM"
    async with httpx.AsyncClient(follow_redirects=False) as client:
        try:
            response = await client.get(url)
            print(f"Status: {response.status_code}")
            if response.is_redirect:
                print(f"Redirects to: {response.headers.get('Location')}")
            else:
                print("No redirect")
        except Exception as e:
            print(f"Error: {e}")

asyncio.run(resolve_url())
