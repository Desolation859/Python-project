def apply_discount(price, category):
    if category == "student":
        price *= 0.85
    elif category == "pensioner":
        price *= 0.8
    print(price)
    return price
apply_discount(5000,"student")