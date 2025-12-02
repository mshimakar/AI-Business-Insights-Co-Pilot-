import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your actual PostgreSQL connection string
# os.getenv('DB_URI') is recommended for production
DATABASE_URL = "postgresql://user:password@localhost/business_insights_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()