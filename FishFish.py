import time
from graphics import *

_images = ['red72.gif', 'green72.gif', 'yellow72.gif', 'blue72.gif']
_rimages = ['red72r.gif', 'green72r.gif', 'yellow72r.gif', 'blue72r.gif']

fishes = []

for i in range(4):
    fishes.append([Image(Point(0, 0), _images[i]), Image(Point(0, 0), _rimages[i])])

win = GraphWin("Fish Tank", 800, 600)

fishes[0][1].move(72, 240)
fishes[0][1].draw(win)
fishes[1][0].move(799-72, 320)
fishes[1][0].draw(win)
fishes[2][1].move(72, 400)
fishes[2][1].draw(win)
fishes[3][0].move(799-72, 480)
fishes[3][0].draw(win)

while True:
    if win.checkKey():
        break
    fishes[0][1].move(16, 0)
    fishes[1][0].move(-8, 0)
    fishes[2][1].move(4, 0)
    fishes[3][0].move(-2, 0)
    time.sleep(0.1)

win.close()