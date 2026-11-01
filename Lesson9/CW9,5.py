temp = 20
while temp < 100:
    power = input("Добавить мощности?: ")
    if power == "Да":
        temp += 25
    else:
        temp += 5
    if temp > 80:
        print("Осторожно, уже кипит!")