import threading
from unittest.mock import patch

from fastapi.testclient import TestClient

from app import main


def test_startup_does_not_wait_for_database_schema():
    schema_started = threading.Event()
    release_schema = threading.Event()

    def blocking_schema_initialization():
        schema_started.set()
        release_schema.wait(timeout=5)

    try:
        with patch.object(main, "init_db", blocking_schema_initialization):
            with TestClient(main.app) as client:
                assert schema_started.wait(timeout=1)
                response = client.get("/health")

                assert response.status_code == 200
                assert response.json() == {"status": "healthy"}
    finally:
        release_schema.set()
