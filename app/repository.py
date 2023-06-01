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
    def favorite_by_access_token(access_token):
        with SessionLocal() as db:
            return db.query(Token, PersonItems).join(PersonItems, Token.id_person == PersonItems.id_person).filter(
                Token.access_token == access_token).first()

    def add_favorite_item(self, access_token: str, item: ItemModel) -> None:
        with SessionLocal() as db:
            print(self.favorite_by_access_token(access_token))
            query = db.query(PersonItems).filter_by(id_person=access_token)
            favorite: list = query.one().favorite
            favorite.append(item.__dict__)
            query.update(({"favorite": json.dumps(favorite)}))
            db.commit()

    def delete_favorite_item(self, access_token: str, item: ItemModel) -> None:
        with SessionLocal() as db:
            ...

    def add_basket_item(self, access_token: str, item: ItemModel) -> None:
        ...

    def delete_basket_item(self, access_token: str, item: ItemModel) -> None:
        ...

    def buy_item(self, access_token: str, item: ItemModel) -> None:
        ...

    def cancel_purchase(self, access_token: str, item: ItemModel) -> None:
        ...

    def add_review(self, access_token: str, item: ItemModel, chtoto) -> None:
        ...

    def delete_review(self, access_token: str, item: ItemModel, chtoto) -> None:
        ...

    def edit_review(self, access_token: str, item: ItemModel, chtoto) -> None:
        ...
