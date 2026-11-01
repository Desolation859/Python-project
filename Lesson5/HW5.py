name = input("\nФамилия?: ").upper()
if len(name) == 0:
    print("Ошибка: Фамилия не может быть пустой!")
print(f'Пассажир: {name}')
limit = 20
weight = float(input("Вес чемодана?: "))
if weight > limit:
    print(f'У вас перевес! Лишний вес: {weight - limit} кг.')
else:
    print("Вес в норме, приятного полета!")
price = 5000
money = int(input("Баланс на карте?: "))
if money < price:
    print("Недостаточно средств для покупки билета!\n")
else:
    print(f'Билет куплен! Ваш остаток: {money - price} руб.\n')