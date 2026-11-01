contacts = {"Anna": 123, "Ivan": 456}
contacts["Maria"] = 789
contacts["Anna"] = 999
print(contacts.get("Petr", "Не найден"))