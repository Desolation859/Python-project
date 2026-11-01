ochenki = [5, 4, 3, 2, 3, 4, 5, 4, 3, 2]
print(ochenki, ochenki[-1])
print(ochenki[2:-1])
print(ochenki[::-1])
good_ochenki = [i for i in ochenki if i >= 4]
print(good_ochenki)
for i in range(len(ochenki)):
    if ochenki[i] == 3:
        ochenki[i] = 4
print(ochenki)