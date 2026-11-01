balance = 0
target = 1000
while balance < target:
    a = int(input("Сколько денег кладем в копилку?: "))
    balance += a
else:
    print("Ура! На мечту накоплено!")