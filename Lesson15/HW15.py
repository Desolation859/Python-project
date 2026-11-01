# Junior and Senior (calories addition)
total_km = 0
calories_burned = 0
def log_run(km):
    global total_km
    total_km += km
    global calories_burned
    calories_burned += km * 70
    return total_km, calories_burned
def show_progress():
    print(f"\nВсего пройденное растояние: {total_km}\nКалорий потеряно: {calories_burned}\n")
    print()
# Middle
def log_walk(km):
    global total_km
    total_km += km * 0.5
    global calories_burned
    calories_burned += km * 35
    return total_km, calories_burned
print(f"\nМеню типа активности:\nБег\nХодьба\nСтоп\n")
while True:
    question = input("Какую активность выбираете?: ").lower()
    question2 = int(input("Пройденное расстояние?: "))
    if question == "бег" and question2 >= 0:
        log_run(question2)
    elif question == "ходьба" and question2 >= 0:
        log_walk(question2)
    elif question == "стоп":
        break
    else:
        print("Отрицательное значение либо неверный тип данных")
show_progress()