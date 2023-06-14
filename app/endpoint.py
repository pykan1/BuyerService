from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

from model import *
from repository import Repository
from service import Service

buyer_service = APIRouter(
    tags=["BuyerService"],
    prefix="/item"
)


@buyer_service.post("/add_favorite_item")
async def add_favorite_item(body: AddItemModel, service: Service = Depends(Service)):
    return service.add_favorite_item(item=body.item, access_token=body.access_token)


@buyer_service.post("/delete_favorite_item")
async def add_favorite_item(body: AddItemModel, service: Service = Depends(Service)):
    return service.delete_favorite_item(item=body.item, access_token=body.access_token)


@buyer_service.post("/add_basket_item")
async def add_basket_item(body: AddItemModel, service: Service = Depends(Service)):
    return service.add_basket_item(body.access_token, body.item)


@buyer_service.post("/delete_basket_item")
async def delete_basket_item(body: AddItemModel, service: Service = Depends(Service)):
    return service.delete_basket_item(body.access_token, body.item)


@buyer_service.post("/add_review_item")
async def add_review_item(model: AddReviewItemModel, service: Service = Depends(Service)):
    return service.add_review(add_review_model=model)


@buyer_service.post("/get_item_reviews")
async def get_item_reviews(model: GetReviewsItemModel, service: Service = Depends(Service)):
    return service.get_item_reviews(model)


@buyer_service.post("/add_item")
async def add_item(model: ItemModel, service: Service = Depends(Service)):
    return service.create_item(model)


@buyer_service.post("/get_items")
async def get_items(access_token: str, service: Service = Depends(Service)):
    return service.get_all_items(access_token)
