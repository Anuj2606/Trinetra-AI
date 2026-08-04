from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.database import get_db
from app.models.scan import Scan

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/")
def analytics(db: Session = Depends(get_db)):

    total = db.query(func.count(Scan.id)).scalar() or 0

    safe = db.query(func.count(Scan.id)).filter(
        Scan.risk_level == "SAFE"
    ).scalar() or 0

    malicious = total - safe

    levels = (
        db.query(
            Scan.risk_level,
            func.count(Scan.id)
        )
        .group_by(Scan.risk_level)
        .all()
    )

    risk_levels = [
        {
            "name": level,
            "value": count
        }
        for level, count in levels
    ]

    return {
        "total": total,
        "safe": safe,
        "malicious": malicious,
        "risk_levels": risk_levels
    }