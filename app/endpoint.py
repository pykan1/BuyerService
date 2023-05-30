from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

from model import ItemModel
from repository import Repository
from service import Service

buyer_service = APIRouter(
    tags=["BuyerService"]
)


@buyer_service.post("/add_favorite_item")
async def add_favorite_item(item: ItemModel):
    ...


@buyer_service.post("/add_basket_item")
async def add_basket_item(item: ItemModel):
    ...


@buyer_service.post("/delete_basket_item")
async def delete_bask(item: ItemModel):
    ...
