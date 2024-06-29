import json


class Cart:

    def __init__(self, id, products=None):
        self.id = id
        self.products = products if products is not None else {}

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)
