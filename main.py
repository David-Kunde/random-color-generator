import turtle as tt
import random
import time

wn = tt.Screen()
wn.setup(width=640, height=640)
wn.title('RANDOM COLOR GENERATOR')
wn.setup(width=680, height=440)
wn.colormode(255)

while True:
    color1 = range(1, 255)
    color2 = range(1, 255)
    color3 = range(1, 255)

    col1 = random.choice(color1)
    col2 = random.choice(color2)
    col3 = random.choice(color3)

    background_color = col1, col2, col3
    print(background_color)
    wn.bgcolor(background_color)
    time.sleep(0.1)

tt.done()
