shop = {"Apple": 50, "Banana": 30, "Cherry": 80}
discount = {}
for item, price in shop.items():
    discount[item] = price * 0.8
print(discount)