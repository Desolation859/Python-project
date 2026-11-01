def fire():
    print("Огненный шар - нанесено 50 урона огнём!")
def ice():
    print("Ледяные кристалы - нанесено 50 урона холодом!")
def heal():
    print("Лечебное заклинание - вылечено 50 здоровья!")
question = ''
while True:
    question = input("Какое заклинание использовать? (fire, ice, heal): ")
    if question == "fire":
        fire()
    elif question == "ice":
        ice()
    elif question == "heal":
        heal()