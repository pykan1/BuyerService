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
