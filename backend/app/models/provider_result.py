from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    JSON,
    ForeignKey
)

from app.database.database import Base


class ProviderResult(Base):

    __tablename__ = "provider_results"

    id = Column(Integer, primary_key=True)

    scan_id = Column(
        Integer,
        ForeignKey("scans.id")
    )

    provider = Column(String(100))

    success = Column(Boolean)

    response = Column(JSON)