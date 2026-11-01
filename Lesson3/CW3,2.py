number = int(input())
result = 0
for i in range(len(str(number))):
    result += number % 10
    number //= 10
print(result)