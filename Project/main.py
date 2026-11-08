price = int(input("Сумма покупки: "))
discount = int(input("Ваша скидка в процентах: "))
new_price = price * (1 - discount / 100)
print(new_price)