import threading

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import router
from app.core.config import settings
from app.core.logger import app_logger
from app.database.init_db import init_db

app = FastAPI(title="Trinetra AI API")


def _initialize_database_schema():
    try:
        init_db()
    except Exception as error:
        app_logger.warning(
            "Database schema initialization failed; API startup will continue ({})",
            type(error).__name__,
        )


@app.on_event("startup")
def initialize_database_schema():
    threading.Thread(
        target=_initialize_database_schema,
        name="database-schema-init",
        daemon=True,
    ).start()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        origin.strip()
        for origin in settings.CORS_ORIGINS.split(",")
        if origin.strip()
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)