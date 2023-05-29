from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

from database.database_model import *
from model import *
from fastapi_jwt_auth import AuthJWT

meta = MetaData()
engine = create_engine(Container().db["url"], echo=True)
meta.create_all(engine)
conn = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class DatabaseRepository:

    @staticmethod
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()