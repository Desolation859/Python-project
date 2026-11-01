import time
a = time.time()
for i in range(1, 1000001):
    continue
b = time.time()
print(f"Время цикла: {b - a} секунд")