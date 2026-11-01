secret = "python123"
a = input("Пароль?: ")
if a == secret:
    print("Доступ разрешен")
else:
    print("Пароль неверный, доступ заблокирован")