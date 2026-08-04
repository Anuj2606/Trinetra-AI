from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.scan import ScanRequest
from app.services.orchestrator import ScanOrchestrator

from app.database.database import get_db
from app.crud.scan_crud import ScanCRUD

router = APIRouter()

orchestrator = ScanOrchestrator()

@router.post("/scan")
async def scan(
    request: ScanRequest,
    db: Session = Depends(get_db)
):

    result = await orchestrator.analyze(request.url)

    ScanCRUD.save_scan(db, result)

    return result