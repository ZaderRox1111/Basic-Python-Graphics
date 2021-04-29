from graphics import *
import math

#global constants
GRAVITY = 10

PARTICLE_SIZE = 10

#windows constants, turns off auto-animation
WIN_WIDTH = 1600
WIN_HEIGHT = 900
WINDOW = GraphWin("Moving Circle", WIN_WIDTH, WIN_HEIGHT, autoflush = False)

EXIT_KEY = 'e'
exitNotClicked = True

DT = 0.01

def main():
    t = 0

    particle1 = Particle(200, 100)

    while exitNotClicked:
        WINDOW.setBackground(color_rgb(10,10,10))

        #update and display the particles
        particle1.update(t)

        #update the time
        t += DT

        update(6000)

    WINDOW.getMouse()
    WINDOW.close()

class Particle:
    #set initial values
    def __init__(self, x, y):
        #setting initial values for the particle
        self.x = x
        self.y = y
        self.radius = PARTICLE_SIZE

        self.win = WINDOW

        self.xSpeed = 0 * DT
        self.ySpeed = 0 * DT

        #originally display the particle
        self.show()

    #function to update the particle
    def update(self, t):
        #update the speeds
        self.ySpeed += GRAVITY * DT

        #update positions
        self.x += self.xSpeed
        self.y += self.ySpeed

        #check for collisions with walls
        self.checkForCollision()

        #move the particle
        self.moveParticle()

    #function to show the particle on the screen
    def show(self):
        #create point to make circle, and draw circle
        self.point = Point(self.x, self.y)
        self.circle = Circle(self.point, self.radius)
        self.circle.setFill(color_rgb(150,150,150))

        self.circle.draw(self.win)

    def checkForCollision(self):
        #check colllsions with walls
        if (self.y > WIN_HEIGHT):
            #avoid infinite collision loop
            self.y = WIN_HEIGHT
            self.ySpeed *= -0.9
        elif (self.y < 0):
            self.y = 0
            self.ySpeed *= -0.9
        if (self.x > WIN_WIDTH):
            self.x = WIN_WIDTH
            self.xSpeed *= -0.9
        elif (self.x < 0):
            self.x = 0
            self.xSpeed *= -0.9

    def moveParticle(self):
        self.circle.move(self.xSpeed, self.ySpeed)

def clear():
    for item in WINDOW.items[:]:
        item.undraw()

if __name__ == "__main__":
    main()
