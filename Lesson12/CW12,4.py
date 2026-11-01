rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
question = input("Шифрация или дешифрация?: ").lower()
question2 = int(input("Какой шаг?: "))
result = ''
if question == "шифрация":
    sentence = input("Введите предложение: ").lower()
    for i in sentence:
        num = rus.index(i)
        new = (num + question2) % len(rus)
        result += rus[new]
else:
    sentence = input("Введите предложение: ").lower()
print(result)