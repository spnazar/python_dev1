class Product:
    def __init__(self, name, price, rank):
        self.name = name  
        self.price = price  
        self.rank = rank 

class Basket:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return True
        return False

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

product1 = Product("Телефон", 50000, 4.5)
product2 = Product("Ноутбук", 75000, 4.8)
product3 = Product("Наушники", 2000, 4.2)

user1 = User("user1", "password123")
user2 = User("user2", "securepass456")

user1.add_to_basket(product1)
user1.add_to_basket(product3)

user2.add_to_basket(product2)
user2.add_to_basket(product1)

print(f"Покупки пользователя {user1.username}:")
for product in user1.basket.products:
    print(f"- {product.name} (Цена: {product.price}, Рейтинг: {product.rank})")

print("\n")

print(f"Покупки пользователя {user2.username}:")
for product in user2.basket.products:
    print(f"- {product.name} (Цена: {product.price}, Рейтинг: {product.rank})")
