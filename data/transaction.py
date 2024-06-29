import json
from data.cart import Cart




class Transaction:

    def __init__(self, private_key: str, public_key: str, cart: Cart,
                 is_completed: str = "UNCOMPLETED"):
        self.public_key = public_key
        self.private_key = private_key
        self.cart = cart
        self.is_completed = is_completed

    def json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)

    def get_price(self):
        return sum(product.price for product in self.cart.products.values())


class TransactionDto:

    def __init__(self, public_key: str, price: float):
        self.public_key = public_key
        self.price = price

    def json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)

