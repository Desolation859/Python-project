total = 0
for i in range(1, 21):
    if i % 2 == 0:
        print(f"Число {i} - чётное!")
        total += i
    else:
        print(f"Число {i} - нечётное!")
print(total)