from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.scan import Scan

router = APIRouter(prefix="/history", tags=["History"])


@router.get("/")
def get_history(db: Session = Depends(get_db)):

    scans = (
        db.query(Scan)
        .order_by(Scan.created_at.desc())
        .all()
    )

    return [
        {
            "id": scan.id,
            "url": scan.url,
            "risk_score": scan.risk_score,
            "risk_level": scan.risk_level,
            "attack_type": scan.attack_type,
            "created_at": scan.created_at,
        }
        for scan in scans
    ]