import time
for h in range(24):
    for m in range(60):
        for s in range(60):
            print(f"Часы: {h}, минуты: {m}, секунды: {s}")
            time.sleep(1)