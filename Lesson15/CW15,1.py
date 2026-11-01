energy = 10
def use_energy():
    global energy
    print(f"До {energy}")
    energy -= 5
use_energy()
print(f"После {energy}")