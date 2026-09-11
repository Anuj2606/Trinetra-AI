import json

from sqlalchemy.orm import Session

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

            db.commit()

            db.refresh(scan)

            # --------------------------
            # Save provider responses
            # --------------------------

            for provider, response in result["providers"].items():

                provider_row = ProviderResult(

                    scan_id=scan.id,

                    provider=provider,

                    success=response.get("success", False),

                    response=response

                )

                db.add(provider_row)

            db.commit()
        except Exception:
            db.rollback()
            raise

        return scan