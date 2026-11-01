for i in range(1, 20):
    a = input("Кто-то заходит? (да/нет/стоп):")
    if a.lower() == "да":
        print("Двери открыты, заходите")
    elif a.lower() == "нет":
        continue
    else:
        print("Лифт застрял. Вызываем диспетчера")
        break