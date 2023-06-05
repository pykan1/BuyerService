from model import *
from repository import Repository


class Service:
    def __init__(self):
        self._repository = Repository()

    def delete_favorite_item(self, uuid, item: ItemModel):
        return self._repository.delete_favorite_item(uuid, item)

    def add_favorite_item(self, access_token, item: ItemModel):
        return self._repository.add_favorite_item(access_token, item)

    def delete_basket_item(self, access_token, item: ItemModel):
        return self._repository.delete_basket_item(access_token, item)

    def add_basket_item(self, access_token, item: ItemModel):
        return self._repository.add_basket_item(access_token, item)

    def add_review(self, add_review_model: AddReviewItemModel):
        return self._repository.add_review(add_review_model)

    def get_item_reviews(self, getReviewsItemModel: GetReviewsItemModel):
        return self._repository.get_item_reviews(getReviewsItemModel)

    def create_item(self, item: ItemModel):
        return self._repository.add_item(item)
