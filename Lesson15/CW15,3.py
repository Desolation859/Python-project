budget = 5000
def spend(amount):
    global budget
    budget -= amount
print(budget)
spend(1000)
print(budget)