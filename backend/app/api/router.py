from fastapi import APIRouter

from app.api.health import router as health_router
from app.api.routes.scan import router as scan_router
from app.api.routes.history import router as history_router
from app.api.routes.analytics import router as analytics_router
from app.api.routes.report import router as report_router

router = APIRouter()

router.include_router(health_router)

router.include_router(

    scan_router,

    tags=["Fraud Scan"]

)
router.include_router(report_router)

router.include_router(history_router)
router.include_router(analytics_router)