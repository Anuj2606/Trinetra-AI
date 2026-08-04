from pydantic import BaseModel

class ScanRequest(BaseModel):
    url: str


class RiskResponse(BaseModel):
    risk_score: int
    risk_level: str
    confidence: int
    reasons: list[str]


class ScanResponse(BaseModel):
    url: str
    risk: RiskResponse
    ai_summary: str
    providers: dict