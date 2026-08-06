# pyrefly: ignore [missing-import]
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.scan import ScanRequest
from app.services.orchestrator import ScanOrchestrator

from app.database.database import get_db
from app.crud.scan_crud import ScanCRUD
from app.utils.validators import validate_url

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

    result = await orchestrator.analyze(request.url)

    ScanCRUD.save_scan(db, result)

    return result