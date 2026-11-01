import time
a = int(input("На сколько поставить таймер?: "))
def countdown(a):
    if a <= 0:
        print("Таймер закончился!")
        return
    time.sleep(1)
    a -= 1
    print(a)
    countdown(a)
countdown(a)