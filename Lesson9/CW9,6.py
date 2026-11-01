days = 1
energy = 100
food = 2
while days < 5:
    print(f'\nДень: {days}\nЭнергия: {energy}\nЕда: {food}')
    action = input("Что делаем сегодня? (искать еду/строить шалаш/отдыхать): ")
    if action == "Искать еду":
        food += 2
        food -= 1
        energy -= 25
        days += 1
    elif action == "Строить шалаш":
        energy -= 25
        building = True
        days += 1
    elif action == "Отдыхать":
        if building == True:
            energy += 75
            energy -= 25
            days += 1
        else:
            energy += 50
            energy -= 25
            days += 1
    if energy <= 0 or food <= 0:
        print("Игра окончена!")
print("За вами приехали спасатели!")