# pyrefly: ignore [missing-import]
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.scan import ScanRequest
from app.services.orchestrator import ScanOrchestrator

from app.database.database import get_db
from app.crud.scan_crud import ScanCRUD
from app.utils.validators import validate_url
from app.core.logger import app_logger

router = APIRouter()

orchestrator = ScanOrchestrator()

@router.post("/scan")
async def scan(
    request: ScanRequest,
    db: Session = Depends(get_db)
):
    if not validate_url(request.url):
        raise HTTPException(
            status_code=400,
            detail="Invalid URL format. Please enter a valid, fully-qualified domain name (e.g. http://example.com)"
        )

    app_logger.info("Scan started")

    try:
        result = await orchestrator.analyze(request.url)
    except Exception:
        app_logger.exception("Scan analysis failed")
        raise HTTPException(
            status_code=502,
            detail="Unable to complete the scan. Please try again later."
        )

    try:
        ScanCRUD.save_scan(db, result)
    except Exception as persistence_error:
        try:
            db.rollback()
        except Exception:
            app_logger.exception("Database rollback failed after scan persistence error")
        raise HTTPException(
            status_code=503,
            detail="Scan completed but could not be saved. Please try again later."
        ) from persistence_error

    app_logger.info("Scan completed risk_score={}", result.get("risk", {}).get("risk_score"))
    return result