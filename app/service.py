from sqlalchemy.orm import Session

from middleware import Middleware
from model import *
from repository import Repository


class Service:
    middleware = Middleware()
    def __init__(self):
        self._repository = Repository()

    def delete_favorite_item(self, access_token: str, id_item: str, db: Session):
        return self._repository.delete_favorite_item(access_token, id_item, db)

    def add_favorite_item(self, access_token, id_item: str, db: Session):
        return self._repository.add_favorite_item(access_token, id_item, db)

    def delete_basket_item(self, access_token, id_item: str, db: Session):
        return self._repository.delete_basket_item(access_token, id_item, db)

    def add_basket_item(self, access_token, id_item: str, db: Session):
        return self._repository.add_basket_item(access_token, id_item, db)

    def add_review(self, add_review_model: AddReviewItemModel, db: Session):
        return self._repository.add_review(add_review_model, db)

    def get_item_reviews(self, getReviewsItemModel: GetReviewsItemModel, db: Session):
        return self._repository.get_item_reviews(getReviewsItemModel, db)

    @middleware.valid_token
    def get_all_items(self, access_token, db: Session):
        return self._repository.get_items(db)

    def item_by_id(self, id_item: str, db: Session):
        return self._repository.item_by_id(id_item=id_item, db=db)

    def create_item(self, item: ItemModel, db: Session):
        return self._repository.add_item(item, db)


