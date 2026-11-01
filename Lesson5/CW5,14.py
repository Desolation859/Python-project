name = input("Имя?: ")
if len(name) <= 3:
    print("Слишком короткое имя, будет сложно запомнить!")
strenght = int(input("Сила?: "))
if strenght <= 5:
    strenght += 5
    print("Маловато силы, дарю тебе +5!")
print(strenght)
weapon = input("Оружие?: ")
if weapon.lower() == "меч":
    print("Меч - отличный выбор для ближнего боя!")
price = 100
money = int(input("Монет?: "))
if money >= price:
    print("Тебе хватает на супер-зелье!")
health = int(input("Здоровье?: "))
if health == 0:
    print("Игра окончена!")
else:
    print("Ты еще в строю, герой!")