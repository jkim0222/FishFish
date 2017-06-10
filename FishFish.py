from graphics import *
import time

n_tropis = 4
n_tropi_copies = 5

_tropil = ['red72.gif',  'green72.gif',  'blue72.gif',  'yellow72.gif']
_tropir = ['red72r.gif', 'green72r.gif', 'blue72r.gif', 'yellow72r.gif']

tropis = []

n_blacks = 4

_blackl = ['shark.gif',  'octopus.gif',  'turtle.gif',  'swordfish.gif']
_blackr = ['sharkr.gif', 'octopusr.gif', 'turtler.gif', 'swordfishr.gif']

blacks = []

tank_x = 800
tank_y = 500

def prep():
    for i in range(n_tropis):
        tropis.append([[Image(Point(0, 0), _tropil[i]),
                        Image(Point(0, 0), _tropir[i])]])

    for i in range(n_tropis):
        for j in range(n_tropi_copies - 1):
            tropis[i].append([Image(Point(0, 0), _tropil[i]),
                              Image(Point(0, 0), _tropir[i])])

    for j in range(n_blacks):
        blacks.append([Image(Point(0, 0), _blackl[i]),
                       Image(Point(0, 0), _blackr[i])])

def move_a_boat_with_a_fishing_line(win, boat, bx, by, line, fy):
    p = boat.getAnchor()
    boat.move(bx - p.getX(), 0)


def move_fishes(win):
    for i in range(n_tropis):
        for j in range(n_tropi_copies):
            p = tropis[i][j][i % 2].getAnchor()
            x = p.getX()
            if x == 0:
                if i % 2 == 0:
                    tropis[i][j][i % 2].move(tank_x - 36, 286 + 72 * i)
                else:
                    tropis[i][j][i % 2].move(36, 286 + 72 * i)
                tropis[i][j][i % 2].draw(win)
                break

            if i % 2 == 0:
                tropis[i][j][i % 2].move(- 4 - (n_tropis - i) * 3, 0)
            else:
                tropis[i][j][i % 2].move(4 + (n_tropis - i) * 3, 0)

            if i % 2 == 0 and x > (tank_x - 36 - 40):
                break
            elif i % 2 == 1 and x < (36 + 40):
                break

def main():
    win = GraphWin("Fish Fish", tank_x, tank_y)

    # Underwater
    underwater = Image(Point(400, 250), 'underwater.gif')
    underwater.draw(win)

    # Boat
    bx = 100
    by = 140
    fy = 180

    boat = Image(Point(bx, by), 'boat.gif')
    boat.draw(win)

    line = Line(Point(bx - 60, by - 30), Point(bx - 60, fy))
    line.draw(win)

    while True:
        k = win.checkKey()
        if k == 'Right':
            bx += 10
        elif k == 'Left':
            bx - 10
        elif k == 'Up':
            fy -= 10
        elif k == 'Down':
            fy += 10
        elif k == 'Q' or k == 'q':
            break

        move_fishes(win)
        line.undraw()
        move_a_boat_with_a_fishing_line(win, boat, bx, by, line, fy)
        line = Line(Point(bx - 60, by - 30), Point(bx - 60, fy))
        line.draw(win)

        time.sleep(0.01)

    win.close()

prep()
main()