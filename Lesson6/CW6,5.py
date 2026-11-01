balance = 1000
a = int(input("Сумма которую хотите потратить?: "))
if a <= balance:
    balance -= a
    print(f"Покупка прошла успешно! Остаток: {balance}")
else:
    print("У вас недостаточно денег на счету!")