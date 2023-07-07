from datetime import datetime

from pydantic import BaseModel


class ItemModel(BaseModel):
    id_item: str
    id_category: int
    name: str
    description: str
    reviews: list | None
    amount: int
    rate: float | None = 0.0
    cost: int | None = 0
    img: str | None


class ReviewModel(BaseModel):
    login: str
    date: str
    rate: int
    title: str
    body: str


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