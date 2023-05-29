from model import ItemModel


class Repository:
    def add_favorite_item(self, item: ItemModel):
        ...

    def delete_favorite_item(self, item: ItemModel):
        ...

    def add_basket_item(self, item: ItemModel):
        ...

    def delete_basket_item(self, item: ItemModel):
        ...

    def buy_item(self, item: ItemModel):
        ...

    def cancel_purchase(self, item: ItemModel):
        ...

    def add_review(self, item: ItemModel, chtoto):
        ...

    def delete_review(self, item: ItemModel, chtoto):
        ...

    def edit_review(self, item: ItemModel, chtoto):
        ...



