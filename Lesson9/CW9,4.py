hp = 100
action = ""
while hp > 0 and action != "Сдаться":
    action = input("Чем бьем? (Меч, магия, сдаться)?: ")
    if action == "Меч":
        hp -= 20
    elif action == "Магия":
        mana = int(input("Сколько маны?: "))
        if mana >= 50:
            hp -= 50
        else:
            hp -= 5
    elif action == "Сдаться":
        print("Герой сбежал!")

if hp <= 0:
    print("Победа!")