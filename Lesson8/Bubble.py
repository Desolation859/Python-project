def bubble(abc):
    n = len(abc)
    for a in range(n):
        for b in range(0, n - a - 1):
            if abc[b] > abc[b + 1]:
                abc[b], abc[b + 1] = abc[b + 1], abc[b]
    return abc

a = [12, 63, 1245, 972178, 7238, 47329, 9182734, 2983547, 342756, 287346]
sorted_a = bubble(a)
print(sorted_a)