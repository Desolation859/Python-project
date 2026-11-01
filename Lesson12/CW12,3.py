symbol = input("Введите символ: ")
height = int(input("Введите высоту: "))
base = int(input("Введите основание: "))
base2 = 1
for j in range(height):
    print(f"{symbol * base2}")
    if base2 <= base:
        base2 += 1