from graphics import *

def main():
    #create a window for the graphics to be drawn on
    win = GraphWin("Circle", 500, 500)
    
    #create a point for the center of the circle
    point1 = Point(250, 250)

    #create a circle at the point
    circ = Circle(point1, 50)

    #draw the circle
    circ.draw(win)

    #close the window on a click
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
