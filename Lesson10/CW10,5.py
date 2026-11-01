good = 0
for i in range(15):
    a = input("Эта ягода хорошая?: ")
    if a.lower() == "да":
        total += 1
    elif a.lower() == "нет":
        print("Эту выбрасываем!")
    else:
        print("Не правильный вариант ответа.")
print(f"В варенье пойдет {total} ягод!")