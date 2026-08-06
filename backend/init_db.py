from app.database.database import engine, Base
# Import all models so they are registered with Base
from app.models.user import User
from app.models.scan import Scan
from app.models.provider_result import ProviderResult

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created successfully!")
