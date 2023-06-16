from fastapi import APIRouter, Depends, Response
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from database_model import Item
from model import *
from repository import Repository
from service import Service

buyer_service = APIRouter(
    tags=["BuyerService"],
    prefix="/item"
)


@buyer_service.post("/add_favorite_item")
async def add_favorite_item(body: AddItemModel, service: Service = Depends(Service),
                            db: Session = Depends(Repository().get_db)):
    return service.add_favorite_item(id_item=body.id_item, access_token=body.access_token, db=db)


@buyer_service.post("/delete_favorite_item")
async def add_favorite_item(body: AddItemModel, service: Service = Depends(Service),
                            db: Session = Depends(Repository().get_db)):
    return service.delete_favorite_item(id_item=body.id_item, access_token=body.access_token, db=db)


@buyer_service.post("/add_basket_item")
async def add_basket_item(body: AddItemModel, service: Service = Depends(Service),
                          db: Session = Depends(Repository().get_db)):
    return service.add_basket_item(body.access_token, body.id_item, db)


@buyer_service.post("/delete_basket_item")
async def delete_basket_item(body: AddItemModel, service: Service = Depends(Service),
                             db: Session = Depends(Repository().get_db)):
    return service.delete_basket_item(body.access_token, body.id_item, db)


@buyer_service.post("/add_review_item")
async def add_review_item(model: AddReviewItemModel, service: Service = Depends(Service),
                          db: Session = Depends(Repository().get_db)):
    return service.add_review(add_review_model=model, db=db)


@buyer_service.post("/get_item_reviews")
async def get_item_reviews(model: GetReviewsItemModel, service: Service = Depends(Service),
                           db: Session = Depends(Repository().get_db)):
    return service.get_item_reviews(model, db)


@buyer_service.post("/add_item")
async def add_item(model: ItemModel, service: Service = Depends(Service), db: Session = Depends(Repository().get_db)):
    return service.create_item(model, db)


@buyer_service.post("/get_items")
async def get_items(access_token: str, service: Service = Depends(Service), db: Session = Depends(Repository().get_db)):
    return service.get_all_items(access_token, db)


@buyer_service.post("/add_img")
async def add_item(id_item: str, file: str, db: Session = Depends(Repository().get_db), service: Service = Depends(Service)):
    return service.add_img(id_item=id_item, file=file, db=db)

@buyer_service.get('/images/{image_id}')
async def get_image(image_id: str, db: Session = Depends(Repository().get_db)):
    # Получите изображение из базы данных по идентификатору
    image = db.query(Item).filter(Item.id_item == image_id).first()
    if image is None:
        return Response(status_code=404)

    # Верните изображение в ответе
    return Response(content=image.img, media_type='image/jpeg')


@buyer_service.post("/get_item")
async def get_item(id_item: str, db: Session = Depends(Repository().get_db), service: Service = Depends(Service)):
    return service.item_by_id(id_item, db)
