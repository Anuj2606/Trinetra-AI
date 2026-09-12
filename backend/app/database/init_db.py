from app.database.database import Base, engine
from app.core.logger import app_logger

# Import all models
from app.models import User, Scan, ProviderResult


def init_db():
    Base.metadata.create_all(bind=engine)
    app_logger.info("Database schema initialization completed")


if __name__ == "__main__":
    init_db()
    print("Database tables created successfully.")