import uuid
from typing import List, Type

from fastapi import Depends
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session
from database_model import *
from container import Container
from model import ItemModel, ReviewModel, AddReviewItemModel, GetReviewsItemModel, OrderModel
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
            favorite: list = query.one().favorite
            favorite.append(item.__dict__)
            query.update(({"favorite": favorite}))
            db.commit()

    def delete_favorite_item(self, access_token: str, item: ItemModel) -> None:
        with SessionLocal() as db:
            try:
                user = self._get_token_data(access_token)
                query = db.query(PersonItems).filter_by(id_person=user["uuid"])
                favorite: list = query.one().favorite
                favorite.remove(item.__dict__)
                query.update(({"favorite": favorite}))
                db.commit()
            except:
                return None

    def add_basket_item(self, access_token: str, item: ItemModel) -> None:
        with SessionLocal() as db:
            user = self._get_token_data(access_token)
            query = db.query(PersonItems).filter_by(id_person=user["uuid"])
            basket: list = query.one().basket
            basket.append(item.__dict__)
            query.update({"basket": basket})
            db.commit()

    def delete_basket_item(self, access_token: str, item: ItemModel) -> None:
        with SessionLocal() as db:
            try:
                user = self._get_token_data(access_token)
                query = db.query(PersonItems).filter_by(id_person=user["uuid"])
                basket: list = query.one().basket
                basket.remove(item.__dict__)
                query.update(({"basket": basket}))
                db.commit()
            except:
                return None

    def buy_item(self, access_token: str, item: ItemModel) -> None:
        with SessionLocal() as db:
            ...

    def cancel_purchase(self, access_token: str, item: ItemModel) -> None:
        ...

    def get_item_reviews(self, model: GetReviewsItemModel):
        with SessionLocal() as db:
            user = self._get_token_data(model.access_token)
            reviews = db.query(Item).filter_by(id_item=model.id_item).one().reviews
            return reviews

    def add_review(self, model: AddReviewItemModel) -> None:
        with SessionLocal() as db:
            user = self._get_token_data(model.access_token)
            query_person = db.query(PersonItems).filter_by(id_person=user["uuid"])
            query_item = db.query(Item).filter_by(id_item=model.id_item)

            reviews_item: list = query_item.one().reviews
            reviews_person: list = query_person.one().reviews

            if not reviews_item:
                reviews_item = []
            if not reviews_person:
                reviews_person = []

            reviews_item.append(model.review.__dict__)
            reviews_person.append(model.review.__dict__)

            query_item.update({"reviews": reviews_item})
            query_person.update({"reviews": reviews_person})
            db.commit()

    def delete_review(self, model: AddReviewItemModel) -> None:
        with SessionLocal() as db:
            try:
                # сделать какую то проверку на то удаление комента,
                # ну типо он просто удаляется,
                # а вообще бы какое нибудь индефицирование пользователя
                user = self._get_token_data(model.access_token)
                query_person = db.query(PersonItems).filter_by(id_person=user["uuid"])
                query_item = db.query(Item).filter_by(id_item=model.id_item)

                reviews_item: list = query_item.one().reviews
                reviews_person: list = query_person.one().reviews

                if not reviews_item:
                    reviews_item = []
                if not reviews_person:
                    reviews_person = []

                reviews_item.remove(model.review.__dict__)
                reviews_person.remove(model.review.__dict__)

                query_item.update({"reviews": reviews_item})
                query_person.update({"reviews": reviews_person})
                db.commit()
            except:
                return None

    def add_order(self, model: OrderModel):
        with SessionLocal() as db:
            user = self._get_token_data(model.access_token)
            query = db.query(PersonItems).filter_by(id_person=user["uuid"])
            orders: list = query.one().orders
            orders.append()

    def edit_review(self, model: AddReviewItemModel) -> None:
        ...

    @staticmethod
    def add_item(item: ItemModel) -> None:
        print(type(item.id_category))
        with SessionLocal() as db:
            db.add(Item(
                id_item=uuid.uuid4(),
                id_category=item.id_category,
                name=item.name,
                description=item.description,
                reviews=item.reviews,
                amount=item.amount
            ))
            db.commit()
        return None

    async def update_rate_items(self, items: list[Type[Item]]):
        with SessionLocal() as db:
            for i in items:
                query = db.query(Item).filter_by(id_item=i.id_item)
                sum_rate = 0
                reviews: list[ReviewModel] = query.one().reviews
                for j in reviews:
                    sum_rate += j.rate
                query.update({"rate": sum_rate / len(reviews)})
            print("commit all items")
            db.commit()

    def get_items(self, access_token) -> list[Type[Item]]:
        with SessionLocal() as db:
            items = db.query(Item).all()
            self.update_rate_items(items)
            return items




