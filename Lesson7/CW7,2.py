cost = int(input("Цена?: "))
coupon = input("Имеется купон?: ")
if cost > 5000 or coupon == "Да":
    print("Вам положен подарок!")
else:
    print("Покупайте больше для бонусов!")