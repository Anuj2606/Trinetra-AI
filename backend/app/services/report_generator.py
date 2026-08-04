"""
Creates the final response returned to the frontend.
"""

from datetime import datetime


class ReportGenerator:

    def generate(
    self,
    url,
    providers,
    risk,
    ai_result=None,
    fraud=None,
):

        ai_summary = "AI explanation unavailable."

        if ai_result:
            ai_summary = ai_result.get(
                "analysis",
                ai_summary
            )

        return {

    "scan_id": datetime.now().strftime("%Y%m%d%H%M%S"),

    "generated_at": datetime.utcnow().isoformat(),

    "url": url,

    "risk": risk,

    "fraud_analysis": fraud,

    "ai_summary": ai_summary,

    "providers": providers

}