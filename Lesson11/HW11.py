for i in range(7):
    item = input("Что кладем в посылку?: ").lower()
    if item == "стекло":
        print("Опасно! Пропускаем этот предмет!")
        continue
    else:
        print(f"{item} был добавлен в посылку!")
print("Посылка собрана и готова к отправке!")