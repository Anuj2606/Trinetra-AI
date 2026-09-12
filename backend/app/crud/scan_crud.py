import json

from sqlalchemy.orm import Session

from app.core.logger import app_logger
from app.models.scan import Scan
from app.models.provider_result import ProviderResult


class ScanCRUD:

    @staticmethod
    def save_scan(
        db: Session,
        result: dict
    ):

        scan = Scan(

            url=result["url"],

            risk_score=result["risk"]["risk_score"],

            risk_level=result["risk"]["risk_level"],

            confidence=result["risk"]["confidence"],

            attack_type=result["fraud_analysis"]["attack_type"],

            ai_summary=result["ai_summary"]

        )

        try:
            db.add(scan)
            db.flush()

            for provider, response in result["providers"].items():
                provider_row = ProviderResult(
                    scan_id=scan.id,
                    provider=provider,
                    success=response.get("success", False),
                    response=json.loads(json.dumps(response, default=str).replace("\\u0000", "")),
                )
                db.add(provider_row)

            db.commit()
        except Exception as error:
            app_logger.exception(
                "Scan persistence failed type={} message={}",
                type(error).__name__,
                str(error),
            )
            try:
                db.rollback()
            except Exception as rollback_error:
                app_logger.exception(
                    "Scan persistence rollback failed type={} message={}",
                    type(rollback_error).__name__,
                    str(rollback_error),
                )
            raise

        return scan