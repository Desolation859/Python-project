def toggle_light():
    print("Включен свет")
def toggle_tv():
    print("Включен телевизор")
def toggle_ac():
    print("Включен кондиционер")
while True:
    question = input("Что включить, свет, телевизор или кондиционер? (выбирайте цифрами): ").lower()
    if question == "1":
        toggle_light()
    elif question == "2":
        toggle_tv()
    elif question == "3":
        toggle_ac()
    elif question == "выход":
        print("Выполняется выход...")
        break