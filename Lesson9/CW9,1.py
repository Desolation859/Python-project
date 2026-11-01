password = input("Пароль от бункера?: ")

while password != "1234":
    password = input("Доступ запрещен! Попробуйте еще раз: ")

print("Добро пожаловать в систему.")