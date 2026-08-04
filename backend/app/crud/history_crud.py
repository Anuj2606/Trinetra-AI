from sqlalchemy.orm import Session

from app.models.scan import Scan
from app.models.provider_result import ProviderResult


class HistoryCRUD:

    @staticmethod
    def get_all_scans(db: Session):

        return (
            db.query(Scan)
            .order_by(Scan.created_at.desc())
            .all()
        )

    @staticmethod
    def get_scan(db: Session, scan_id: int):

        scan = (
            db.query(Scan)
            .filter(Scan.id == scan_id)
            .first()
        )

        if not scan:
            return None

        providers = (
            db.query(ProviderResult)
            .filter(ProviderResult.scan_id == scan_id)
            .all()
        )

        return {
            "scan": scan,
            "providers": providers
        }