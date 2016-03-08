from graphics import *
from math import *
def main() :
    win = GraphWin("Quoridor",550,550)
    block= Rectangle(Point(50,50),Point(500,500))
    block.setFill("black")
    block.draw(win)
    for i in range(8) :
        l=Line(Point(50*i+100,50),Point(50*i+100,500))
        l.setFill('white')
        l.setWidth(10)
        l.draw(win)
    for i in range(8) :
        l=Line(Point(50,50*i+100),Point(500,50*i+100))
        l.setFill('white')
        l.setWidth(10)
        l.draw(win)

    p1= Circle(Point(275,72.5),20)
    p1.setFill('red')
    p1.draw(win)
    p2= Circle(Point(275,477.5),20)
    p2.setFill('blue')
    p2.draw(win)

    
    c1=win.getMouse()
    if c1.getX()> p1.getCenter():
        p1.move(50,0)
    else:
        p1.move(-50,0)

    win.getMouse()
    win.close()

main()
