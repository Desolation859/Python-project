def max(a, b, c):
    if a > b and a > c:
        print(f"Самое большое число: {a}")
        return a
    elif b > a and b > c:
        print(f"Самое большое число: {b}")
        return b
    else:
        print(f"Самое большое число: {c}")
    return c