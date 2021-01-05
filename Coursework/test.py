from graphics import *
import time

WIDTH, HEIGHT = 400, 400
RADIUS = 40

def main():
    win = GraphWin('Lab Four', WIDTH, HEIGHT)

    c = Circle(Point(100, 50), RADIUS)
    c.draw(win)
    c.setFill('red')

    s = Rectangle(Point(300, 300), Point(350, 350))
    s.draw(win)
    s.setFill('blue')

    while True:
        c.move(10, 0)
        s.move(-10, 0)
        win.after(100)

main()