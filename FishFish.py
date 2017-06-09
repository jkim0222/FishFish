from graphics import *
import time

_tropil = ['red72.gif',  'green72.gif',  'blue72.gif',  'yellow72.gif']
_tropir = ['red72r.gif', 'green72r.gif', 'blue72r.gif', 'yellow72r.gif']
_blackl = ['shark.gif',  'octopus.gif',  'turtle.gif',  'swordfish.gif']
_blackr = ['sharkr.gif', 'octopusr.gif', 'turtler.gif', 'swordfishr.gif']

tropis = []
blacks = []

for i in range(4):
    for j in range(8):
        tropis.append([Image(Point(0, 0), _tropil[i]),
                       Image(Point(0, 0), _tropir[i])])
    for j in range(8):
        blacks.append([Image(Point(0, 0), _blackl[i]),
                       Image(Point(0, 0), _blackr[i])])

underwater = Image(Point(400, 250), 'underwater.gif')
boat = Image(Point(100, 140), 'boat.gif')

lines = []

for i in range(50):
    lines.append(Line(Point(40, 110), Point(40, 140 + 7 * i)))

win = GraphWin("Fish Fish", 800, 500)

underwater.draw(win)
boat.draw(win)
line = 0
lines[line].draw(win)

tropis[0][1].move(72, 214)
tropis[0][1].draw(win)
tropis[8][0].move(799-72, 286)
tropis[8][0].draw(win)
tropis[16][1].move(72, 358)
tropis[16][1].draw(win)
tropis[24][0].move(799-72, 430)
tropis[24][0].draw(win)

while True:
    k = win.checkKey()
    if k == 'Right':
        boat.move(7, 0)
    elif k == 'Left':
        boat.move(-7, 0)
    elif k == 'Up':
        line.move(0, -5)
    elif k == 'Down':
        line.move(0, 5)
    elif k == 'Q' or k == 'q':
        break
    tropis[0][1].move(5, 0)
    tropis[8][0].move(-4, 0)
    tropis[16][1].move(3, 0)
    tropis[24][0].move(-2, 0)
    time.sleep(0.01)

win.close()