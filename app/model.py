from datetime import datetime

from pydantic import BaseModel


class ItemModel(BaseModel):
    id_item: str
    id_category: int
    name: str
    description: str
    reviews: list | None
    amount: int


class ReviewModel(BaseModel):
    login: str
    date: str
    rate: int
    title: str
    body: str


class AddItemModel(BaseModel):
    item: ItemModel
    access_token: str


class GetReviewsItemModel(BaseModel):
    id_item: str
    access_token: str


class AddReviewItemModel(BaseModel):
    id_item: str
    review: ReviewModel
    access_token: str


class OrderModel(BaseModel):
    coordinates: str
    item: ItemModel
    time: str
    access_token: str