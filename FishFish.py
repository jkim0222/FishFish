import time
from graphics import *

_images = ['red72.gif', 'green72.gif', 'yellow72.gif', 'blue72.gif']
_rimages = ['red72r.gif', 'green72r.gif', 'yellow72r.gif', 'blue72r.gif']

fishes = []

for i in range(4):
    fishes.append([Image(Point(0, 0), _images[i]), Image(Point(0, 0), _rimages[i])])

underwater = Image(Point(400, 250), 'underwater.gif')
boat = Image(Point(100, 140), 'boat.gif')

win = GraphWin("Fish Tank", 800, 500)

underwater.draw(win)
boat.draw(win)

fishes[0][1].move(72, 214)
fishes[0][1].draw(win)
fishes[1][0].move(799-72, 286)
fishes[1][0].draw(win)
fishes[2][1].move(72, 358)
fishes[2][1].draw(win)
fishes[3][0].move(799-72, 430)
fishes[3][0].draw(win)

while True:
    k = win.checkKey()
    if k == 'Right':
        boat.move(7, 0)
    elif k == 'Left':
        boat.move(-7, 0)
    elif k == 'Q' or k == 'q':
        break
    fishes[0][1].move(5, 0)
    fishes[1][0].move(-4, 0)
    fishes[2][1].move(3, 0)
    fishes[3][0].move(-2, 0)
    time.sleep(0.01)

win.close()