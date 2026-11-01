def check_password(input_password):
    secret = 12345
    if input_password == secret:
        print("Открыто")
    else:
        print("Не правильный пароль")
check_password(12345)