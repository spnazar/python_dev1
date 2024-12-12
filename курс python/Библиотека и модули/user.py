from basket import Basket

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.basket = Basket()

    def add_to_basket(self, product):
        self.basket.add_product(product)

    def remove_from_basket(self, product_name):
        if not self.basket.remove_product(product_name):
            print(f"Товар '{product_name}' не найден в корзине.")
