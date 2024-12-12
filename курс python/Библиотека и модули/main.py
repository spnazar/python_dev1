from product import Product
from user import User

# Создаем товары
product1 = Product("Телефон", 50000, 4.5)
product2 = Product("Ноутбук", 75000, 4.8)
product3 = Product("Наушники", 2000, 4.2)

# Создаем пользователей
user1 = User("user1", "password123")
user2 = User("user2", "securepass456")

# Добавляем товары в корзины пользователей
user1.add_to_basket(product1)
user1.add_to_basket(product3)

user2.add_to_basket(product2)
user2.add_to_basket(product1)

# Выводим информацию о покупках
print(f"Покупки пользователя {user1.username}:")
for product in user1.basket.products:
    print(f"- {product.name} (Цена: {product.price}, Рейтинг: {product.rank})")

print("\n")

print(f"Покупки пользователя {user2.username}:")
for product in user2.basket.products:
    print(f"- {product.name} (Цена: {product.price}, Рейтинг: {product.rank})")
