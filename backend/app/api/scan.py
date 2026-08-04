from fastapi import APIRouter

from app.schemas.scan import ScanRequest
from app.services.orchestrator import ScanOrchestrator

router = APIRouter()

orchestrator = ScanOrchestrator()


@router.post("/scan")
async def scan_url(request: ScanRequest):

    result = await orchestrator.analyze(str(request.url))

    return result