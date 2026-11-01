import time
import math

x = 1.0
multiplier_per_ms = 1.0001       # множитель за 1 миллисекунду
interval_seconds = 2          # вывод каждые N секунд

while True:
    interval_ms = int(interval_seconds * 1000)
    
    # За интервал в N миллисекунд x умножится на multiplier_per_ms в степени N
    x *= multiplier_per_ms ** interval_ms
    
    if x > 1000:
        output = f"{x:.2e}"
    else:
        output = str(x)
    
    print(output)
    
    time.sleep(interval_seconds)
