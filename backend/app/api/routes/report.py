from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os
import tempfile

router = APIRouter(prefix="/report", tags=["Reports"])


@router.post("/")
def generate_report(result: dict):

    styles = getSampleStyleSheet()

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    doc = SimpleDocTemplate(tmp.name)

    story = []

    story.append(Paragraph("<b>Trinetra AI Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>URL:</b> {result['url']}", styles["BodyText"]))

    story.append(
        Paragraph(
            f"<b>Risk Score:</b> {result['risk']['risk_score']}",
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            f"<b>Threat Level:</b> {result['risk']['risk_level']}",
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            result["ai_summary"],
            styles["BodyText"],
        )
    )

    doc.build(story)

    return FileResponse(
        tmp.name,
        filename="Trinetra_Report.pdf",
        media_type="application/pdf",
    )