import turtle

turtle.ht()
turtle.speed(0)
turtle.shape("square")
turtle.penup()
turtle.setposition(turtle.window_width() *-.5, turtle.window_height() * .5)
turtle.pendown()

def drawSquare(size, color):
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.pen(fillcolor=color, pencolor=color, pensize=0)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.end_fill()

j = 0
while (j < 9):
    turtle.pendown()
    i = 0
    while (i < 4):
        if j % 2 == 0:
            color1 = "red"
            color2 = "black"
        if j % 2 == 1:
            color1 = "black"
            color2 = "red"
        drawSquare(turtle.window_height()/8, color1)
        turtle.forward(turtle.window_height()/8)
        drawSquare(turtle.window_height()/8, color2)
        turtle.forward(turtle.window_height()/8)
        i += 1
    turtle.penup()
    turtle.setposition(turtle.window_width() *-.5, turtle.window_height() * .5)
    turtle.right(90)
    turtle.forward(turtle.window_height()/8 * (j + 1))
    turtle.left(90)
    j += 1
