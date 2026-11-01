import time
while True:
    a = time.time()
    time.sleep(2)
    b = time.time()
    print(f"Прошло {b - a} секунд")