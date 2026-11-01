distance = int(input("Дистанция?: "))
status = input("Состояние погоды (Дождь или Солнце)?: ")
if distance < 2 and status == "Солнце":
    print("Идите пешком")
elif distance > 10 or status == "Дождь":
    print("Вызывайте такси")
else:
    print("Вызывайте автобус")