"""
Gemini Provider

Generates explainable AI summaries.
If Gemini is unavailable, the scan still succeeds.
"""

from google import genai

from app.core.config import settings
from app.services.providers.base import BaseProvider


class GeminiProvider(BaseProvider):

    MODELS = [
        "gemini-3.6-flash",
        "gemini-2.5-pro",
        "gemini-2.5-flash",
    ]

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    async def analyze(self, risk):

        prompt = f"""
You are an expert cybersecurity analyst.

Risk Score: {risk["risk_score"]}

Risk Level: {risk["risk_level"]}

Confidence: {risk["confidence"]}

Reasons:

{chr(10).join(risk["reasons"])}

Write a concise professional report.

Format:

Summary:

Threats:

Recommendation:
"""

        last_error = None

        for model in self.MODELS:

            try:

                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                return {

                    "provider": "Gemini",

                    "success": True,

                    "model": model,

                    "analysis": response.text

                }

            except Exception as e:

                last_error = str(e)

                continue

        return {

            "provider": "Gemini",

            "success": False,

            "analysis": "AI explanation unavailable at this time.",

            "error": last_error

        }