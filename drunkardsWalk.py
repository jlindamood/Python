import turtle
import random

def drunkardsWalk():
    turtle.speed(0)
    turtle.delay(0)
    turtle.screensize(100, 100)
    winWidth = turtle.window_width()
    winHeight = turtle.window_height()

    steps = 0
    yCor = 0
    xCor = 0
    headingInt = 0
    heading = 0

    while (xCor <= winWidth and yCor <= winHeight):
        headingInt = random.randint(1, 4)
        heading = (headingInt-1) * 90
        turtle.setheading(heading)
        turtle.pendown()
        turtle.forward(20)
        steps += 20
        xCor = abs(turtle.xcor())
        yCor = abs(turtle.ycor())

    print(steps)
    return steps

def main():
    drunkardsWalk()

if __name__ == '__main__':
    main()
