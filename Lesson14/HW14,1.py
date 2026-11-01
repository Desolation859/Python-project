# Junior
def calculate_tax(salary):
    if salary < 50000:
        tax = salary * 0.13
    else:
        tax = salary * 0.15
    return(tax)
# Middle
def get_net_salary(salary):
    net_worth = salary - calculate_tax(salary)
    return net_worth
# Senior
def apply_discount(price, category):
    if category == "student":
        price *= 0.85
    elif category == "pensioner":
        price *= 0.8
    return price
def generate_raport(salary, price, category):
    print(f"\nЗарплата после налога: {get_net_salary(salary)}\nТовар со скидкой: {apply_discount(price,category)}\nВсего: {get_net_salary(salary) - apply_discount(price,category)}")
salary = int(input("Зарплата?: "))
price = int(input("Цена?: "))
category = input("Категория, студент или пенсионер?: ")
generate_raport(salary,price,category)