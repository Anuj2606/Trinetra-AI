"""
Provider Runner

Executes providers safely without crashing the application.
"""

import traceback


class ProviderRunner:

    @staticmethod
    async def run(provider_name: str, coroutine):

        try:

            result = await coroutine

            result["success"] = True

            return result

        except Exception as e:

            print(f"\n❌ {provider_name} Failed")

            traceback.print_exc()

            return {

                "provider": provider_name,

                "success": False,

                "error": str(e)

            }