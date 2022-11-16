from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Pretender93*@localhost/fastapi'

# responsible for connecting to postgres database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# make use of session to talk to sql database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


#  function below gets a session to our database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
