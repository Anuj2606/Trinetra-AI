from app.database.database import Base, engine

# Import all models
from app.models import User, Scan, ProviderResult


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database tables created successfully.")