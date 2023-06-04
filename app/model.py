from datetime import datetime

from pydantic import BaseModel


class ItemModel(BaseModel):
    id_item: str
    id_category: int
    name: str
    description: str
    reviews: str
    amount: int


class ItemBodyModel(BaseModel):
    item: ItemModel
    access_token: str


class ReviewModel(BaseModel):
    login: str
    date: datetime
    rate: int
    title: str
    body: str

