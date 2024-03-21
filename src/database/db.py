from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sin = 'psycopg2'
asin = "asyncpg"


SQLALCHEMY_DATABASE_URL = f"postgresql+{sin}://postgres:567234@localhost:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
