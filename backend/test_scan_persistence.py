import asyncio
import os
from datetime import datetime

import pytest
from fastapi import HTTPException

os.environ.setdefault("GEMINI_API_KEY", "test-key")
os.environ.setdefault("DATABASE_HOST", "localhost")
os.environ.setdefault("DATABASE_PORT", "5432")
os.environ.setdefault("DATABASE_NAME", "test_db")
os.environ.setdefault("DATABASE_USER", "test_user")
os.environ.setdefault("DATABASE_PASSWORD", "test_password")
os.environ.setdefault("DATABASE_SSLMODE", "disable")

from app.api.routes import scan as scan_route
from app.crud.scan_crud import ScanCRUD
from app.schemas.scan import ScanRequest


class FakeScan:
    def __init__(self, **values):
        self.__dict__.update(values)
        self.id = None


class FakeProviderResult:
    def __init__(self, **values):
        self.__dict__.update(values)


class FakeSession:
    def __init__(self, fail_on_commit=False, fail_on_rollback=False):
        self.items = []
        self.commit_count = 0
        self.fail_on_commit = fail_on_commit
        self.fail_on_rollback = fail_on_rollback

    def add(self, item):
        self.items.append(item)

    def flush(self):
        self.items[0].id = 42

    def commit(self):
        self.commit_count += 1
        if self.fail_on_commit:
            raise RuntimeError("database commit failed")

    def rollback(self):
        if self.fail_on_rollback:
            raise RuntimeError("database rollback failed")


def result_with_non_json_values():
    return {
        "url": "https://example.com",
        "risk": {"risk_score": 1, "risk_level": "SAFE", "confidence": 99},
        "fraud_analysis": {"attack_type": "Legitimate Website"},
        "ai_summary": "mock",
        "providers": {
            "mock": {
                "success": True,
                "when": datetime(2026, 1, 1),
                "values": {"a", "b"},
                "object": object(),
                "null_byte": "null\u0000byte",
            }
        },
    }


def test_success_persists_scan_and_provider_atomically(monkeypatch):
    monkeypatch.setattr("app.crud.scan_crud.Scan", FakeScan)
    monkeypatch.setattr("app.crud.scan_crud.ProviderResult", FakeProviderResult)
    db = FakeSession()

    scan = ScanCRUD.save_scan(db, result_with_non_json_values())

    assert scan.id == 42
    assert db.commit_count == 1
    assert len(db.items) == 2
    assert isinstance(db.items[1].response["when"], str)
    assert isinstance(db.items[1].response["values"], str)
    assert isinstance(db.items[1].response["object"], str)
    assert db.items[1].response["null_byte"] == "nullbyte"
    assert db.items[1].scan_id == scan.id


def test_database_failure_rolls_back_and_reraises(monkeypatch):
    monkeypatch.setattr("app.crud.scan_crud.Scan", FakeScan)
    monkeypatch.setattr("app.crud.scan_crud.ProviderResult", FakeProviderResult)
    db = FakeSession(fail_on_commit=True)

    with pytest.raises(RuntimeError, match="database commit failed"):
        ScanCRUD.save_scan(db, result_with_non_json_values())


def test_rollback_failure_does_not_escape_scan_as_http_500(monkeypatch):
    payload = result_with_non_json_values()
    monkeypatch.setattr(scan_route, "orchestrator", type(
        "FakeOrchestrator",
        (),
        {"analyze": lambda self, url: asyncio.sleep(0, result=payload)},
    )())
    monkeypatch.setattr(
        scan_route.ScanCRUD,
        "save_scan",
        lambda db, result: (_ for _ in ()).throw(RuntimeError("database commit failed")),
    )
    db = FakeSession(fail_on_rollback=True)

    with pytest.raises(HTTPException) as error:
        asyncio.run(scan_route.scan(ScanRequest(url=payload["url"]), db))

    assert error.value.status_code == 503