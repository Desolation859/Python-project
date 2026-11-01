product = {"title": "Ноутбук", "price": 50000, "discount": 10}
new_price = product["price"] - (product["discount"] * product["price"] / 100)
product["final_price"] = new_price
print(product)