from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

from model import ItemModel, ItemBodyModel
from repository import Repository
from service import Service

buyer_service = APIRouter(
    tags=["BuyerService"]
)


@buyer_service.post("/add_favorite_item")
async def add_favorite_item(body: ItemBodyModel, service: Service = Depends(Service)):
    return service.add_favorite_item(item=body.item, access_token=body.access_token)


@buyer_service.post("/delete_favorite_item")
async def add_favorite_item(body: ItemBodyModel, service: Service = Depends(Service)):
    return service.delete_favorite_item(item=body.item, uuid=body.access_token)


@buyer_service.post("/add_basket_item")
async def add_basket_item(item: ItemModel):
    ...


@buyer_service.post("/delete_basket_item")
async def delete_basket_item(item: ItemModel):
    ...
