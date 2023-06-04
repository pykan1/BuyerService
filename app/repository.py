from fastapi import Depends
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session
from database_model import *
from container import Container
from model import ItemModel, Review, ReviewModel
import json
import jwt
from fastapi import HTTPException

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
    def _get_token_data(token):
        try:
            return jwt.decode(
                jwt=token,
                key=Container().auth["secret_key"],
                algorithms=["HS256"]
            )
        except:
            raise HTTPException(status_code=406, detail={"message": "token invalid"})

    def add_favorite_item(self, access_token: str, item: ItemModel) -> None:
        with SessionLocal() as db:
            user = self._get_token_data(access_token)
            query = db.query(PersonItems).filter_by(id_person=user["uuid"])
            favorite = json.loads(query.one().favorite)
            favorite.append(item.__dict__)
            query.update(({"favorite": json.dumps(favorite)}))
            db.commit()

    def delete_favorite_item(self, access_token: str, item: ItemModel) -> None:
        with SessionLocal() as db:
            try:
                user = self._get_token_data(access_token)
                query = db.query(PersonItems).filter_by(id_person=user["uuid"])
                favorite: list = json.loads(query.one().favorite)
                favorite.remove(item.__dict__)
                query.update(({"favorite": json.dumps(favorite)}))
                db.commit()
            except:
                return None

    def add_basket_item(self, access_token: str, item: ItemModel) -> None:
        with SessionLocal() as db:
            user = self._get_token_data(access_token)
            query = db.query(PersonItems).filter_by(id_person=user["uuid"])
            basket: list = json.loads(query.one().basket)
            basket.append(item.__dict__)
            query.update({"basket": json.dumps(basket)})
            db.commit()

    def delete_basket_item(self, access_token: str, item: ItemModel) -> None:
        with SessionLocal() as db:
            try:
                user = self._get_token_data(access_token)
                query = db.query(PersonItems).filter_by(id_person=user["uuid"])
                basket: list = json.loads(query.one().favorite)
                basket.remove(item.__dict__)
                query.update(({"favorite": json.dumps(basket)}))
                db.commit()
            except:
                return None

    def buy_item(self, access_token: str, item: ItemModel) -> None:
        with SessionLocal() as db:
            ...

    def cancel_purchase(self, access_token: str, item: ItemModel) -> None:
        ...

    def add_review(self, access_token: str, item: ItemModel, review: ReviewModel) -> None:
        with SessionLocal() as db:
            query = db.query(Item).filter_by(id_item=item.id_item)
            reviews: list = json.loads(query.one().reviews)
            reviews.append(review)
            query.update({"reviews": json.dumps(reviews)})
            db.commit()


    def delete_review(self, access_token: str, item: ItemModel, chtoto) -> None:
        ...

    def edit_review(self, access_token: str, item: ItemModel, chtoto) -> None:
        ...
