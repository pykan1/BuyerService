from model import ItemModel
from repository import Repository


class Service:
    def __init__(self):
        self._repository = Repository()

    def delete_favorite_item(self, uuid, item: ItemModel):
        self._repository.delete_favorite_item(uuid, item)

    def add_favorite_item(self, access_token, item: ItemModel):
        self._repository.add_favorite_item(access_token, item)

    def delete_basket_item(self, uuid, item: ItemModel):
        self._repository.delete_basket_item(uuid, item)

    def add_basket_item(self, uuid, item: ItemModel):
        self._repository.add_basket_item(uuid, item)

    #еще запросы с репозитория должны быть
