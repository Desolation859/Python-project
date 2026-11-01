a = 0
b = 0
for i in range(5):
    a = int(input("Введите число: "))
    if a <= 0:
        continue
    else:
        b += a
        print(f"Принято число: {a}")
print(f"\nСумма: {b}")