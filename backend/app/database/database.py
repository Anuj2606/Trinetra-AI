from sqlalchemy import create_engine
from sqlalchemy.engine import URL, make_url
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings


def _build_database_url() -> URL:
    if settings.DATABASE_URL:
        database_url = make_url(settings.DATABASE_URL)
    else:
        required_settings = {
            "DATABASE_HOST": settings.DATABASE_HOST,
            "DATABASE_PORT": settings.DATABASE_PORT,
            "DATABASE_NAME": settings.DATABASE_NAME,
            "DATABASE_USER": settings.DATABASE_USER,
            "DATABASE_PASSWORD": settings.DATABASE_PASSWORD,
        }
        missing_settings = [
            name
            for name, value in required_settings.items()
            if value is None
        ]
        if missing_settings:
            raise ValueError(
                "Missing database configuration: "
                + ", ".join(missing_settings)
            )

        database_url = URL.create(
            drivername="postgresql+psycopg2",
            username=settings.DATABASE_USER,
            password=settings.DATABASE_PASSWORD,
            host=settings.DATABASE_HOST,
            port=settings.DATABASE_PORT,
            database=settings.DATABASE_NAME,
        )

    if settings.DATABASE_SSLMODE and "sslmode" not in database_url.query:
        database_url = database_url.update_query_dict(
            {"sslmode": settings.DATABASE_SSLMODE}
        )

    return database_url


database_url = _build_database_url()
DATABASE_URL = database_url.render_as_string(hide_password=False)

engine = create_engine(
    database_url,
    pool_pre_ping=True,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    pool_timeout=settings.DATABASE_POOL_TIMEOUT,
    pool_recycle=settings.DATABASE_POOL_RECYCLE,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()