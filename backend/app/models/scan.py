from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text,
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func

from app.database.database import Base


class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    url = Column(Text, nullable=False)

    risk_score = Column(Integer, nullable=False)

    risk_level = Column(String(50), nullable=False)

    confidence = Column(Float, nullable=False)

    attack_type = Column(String(100))

    ai_summary = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )