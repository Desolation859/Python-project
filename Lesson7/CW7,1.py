user = input("Пользователь?: ")
password = input("Пароль?: ")
if user == "admin" and password == "12345":
    print("Доступ к секретам открыт!")
else:
    print("Ошибка входа!")