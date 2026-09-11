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

    try:
        result = await orchestrator.analyze(request.url)
    except Exception:
        app_logger.exception("Scan analysis failed for URL: {}", request.url)
        raise HTTPException(
            status_code=502,
            detail="Unable to complete the scan. Please try again later."
        )

    try:
        ScanCRUD.save_scan(db, result)
    except Exception:
        db.rollback()
        app_logger.exception("Scan persistence failed for URL: {}", request.url)
        raise HTTPException(
            status_code=503,
            detail="Scan completed but could not be saved. Please try again later."
        )

    return result