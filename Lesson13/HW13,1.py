weather = ''
def wake_up():
    print("Вы проснулись!")
def brush_teeth():
    print("Вы почистили зубы!")
def eat_breakfast():
    print("Вы поели завтрак!")
def choose_outfit():
    if weather == 'солнце':
        print("Одевай рубашку и джинсы!")
    elif weather == "дождь":
        print("Одевай рубашку, куртку, и теплые штаны!")
def ask_weather():
    weather = input("Какая на улице погода, солнечно или дождь?: ")
    return weather
wake_up()
brush_teeth()
eat_breakfast()
ask_weather()
choose_outfit()