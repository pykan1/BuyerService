from datetime import datetime

from pydantic import BaseModel


class ReviewModel(BaseModel):
    login: str
    date: str
    rate: int
    title: str
    body: str

    def __json__(self):
        return self.dict()


class ItemModel(BaseModel):
    id_item: str = ""
    id_category: int = 0
    name: str = ""
    description: str = ""
    reviews: list = []
    amount: int = 0
    rate: float = 0.0
    cost: int = 0
    img: str = ""


class AccessTokenModel(BaseModel):
    access_token: str


class AddItemModel(BaseModel):
    id_item: str
    access_token: str


class GetReviewsItemModel(BaseModel):
    id_item: str
    access_token: str


class AddReviewItemModel(BaseModel):
    id_item: str
    review: ReviewModel
    access_token: str


class GetItemsByCategoryModel(AccessTokenModel):
    id_category: int


class OrderModel(BaseModel):
    coordinates: str
    item: ItemModel
    time: str
    access_token: str
