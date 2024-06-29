from data.cart import Cart
from data.product import Product


product_0 = Product(0, "Bike", 0.01)
product_1 = Product(1, "Car", 0.02)
product_2 = Product(2, "Book", 0.03)
product_3 = Product(3, "Laptop", 0.04)
product_4 = Product(4, "Phone", 0.05)
product_5 = Product(5, "Headphones", 600.0)
product_6 = Product(6, "Shoes", 700.0)
product_7 = Product(7, "Watch", 800.0)
product_8 = Product(8, "Bag", 900.0)
product_9 = Product(9, "Sunglasses", 1000.0)

products = {
    product_0.id: product_0,
    product_1.id: product_1,
    product_2.id: product_2,
    product_3.id: product_3,
    product_4.id: product_4,
    product_5.id: product_5,
    product_6.id: product_6,
    product_7.id: product_7,
    product_8.id: product_8,
    product_9.id: product_9
}

cart = Cart(1, {})

transactions = {}

