import drawsquare
import random
import turtle

def sliceofpi(darts):
    turtle.speed(0)
    turtle.delay(0)
    drawsquare.drawSquare(300, 0)
    turtle.penup()
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)

    dartsThrown = 0
    dartsInCircle = 0

    while dartsThrown < darts:
        inCircle = throwDart()
        if inCircle:
            dartsInCircle += 1
        dartsThrown += 1

    piApprox = 4*(dartsInCircle / dartsThrown)

    print(piApprox)
    return piApprox

def throwDart():
    impact = []
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    x = x * 150
    y = y * 150
    impact = [x, y]
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)

    withinCircle = False
    color = ""
    distanceFromCenter = x**2 + y**2
    if 150**2 >= distanceFromCenter:
        color = "green"
        withinCircle = True
    else:
        color = "red"

    turtle.pendown()
    turtle.dot(5, color)

    turtle.penup() # Reset back to center

    turtle.forward(-y)
    turtle.right(90)
    turtle.forward(-x)

    return withinCircle


def main():
    sliceofpi(1000)

if __name__ == '__main__':
    main()
