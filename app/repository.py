from fastapi import Depends
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session
from database_model import *
from container import Container
from model import ItemModel
import json

meta = MetaData()
engine = create_engine(Container().db["url"], echo=True)
meta.create_all(engine)
conn = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Repository:
    @staticmethod
    def _get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @staticmethod
    def add_favorite_item(uuid: str, item: ItemModel) -> list:
        with SessionLocal() as db:
            query = db.query(PersonItems).filter_by(id_person=uuid)
            favorite = json.loads(str(query.one().favorite))
            favorite.append(item)
            query.update(({"favorite": str(favorite)}))
            db.commit()
            return favorite

    def delete_favorite_item(self, uuid: str, item: ItemModel) -> None:
        ...

    def add_basket_item(self, uuid: str, item: ItemModel) -> None:
        ...

    def delete_basket_item(self, uuid: str, item: ItemModel) -> None:
        ...

    def buy_item(self, uuid: str, item: ItemModel) -> None:
        ...

    def cancel_purchase(self, uuid: str, item: ItemModel) -> None:
        ...

    def add_review(self, uuid: str, item: ItemModel, chtoto) -> None:
        ...

    def delete_review(self, uuid: str, item: ItemModel, chtoto) -> None:
        ...

    def edit_review(self, uuid: str, item: ItemModel, chtoto) -> None:
        ...
