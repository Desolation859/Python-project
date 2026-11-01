height = 9
c = height // 2
for i in range(height):
    for j in range(height):
        if abs(i - c) + abs(j - c) <= c:
            fill = True
        else:
            fill = False
        if fill == True:
            print('*', end='')
        else:
            print(' ', end='')
    print()