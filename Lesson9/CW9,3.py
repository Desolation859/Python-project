items = 0
while items < 3:
    a = input("Что положим в рюкзак?: ")
    items += 1
    if items == 1 or items == 2:
        print(f"{a} добавлен. Места осталось: {3 - items}")

print("Рюкзак полон, погнали!")