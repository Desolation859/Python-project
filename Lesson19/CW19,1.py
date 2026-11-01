scores = {"Math": 95, "English": 82, "Code": 100}
a = 0
for subj, score in scores.items():
    print(f"{subj} - {score}")
    if score > a:
        a = score
print(a)