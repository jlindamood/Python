# by James L & Dylan S.
# for CS1133 Amy Larson

import turtle

def drawOlympicCircles(radius):
    turtle.pencolor("blue")
    drawCircle(radius)
    orientDown(radius)
    turtle.pencolor("yellow")
    drawCircle(radius)
    orientUp(radius)
    turtle.pencolor("black")
    drawCircle(radius)
    orientDown(radius)
    turtle.pencolor("green")
    drawCircle(radius)
    orientUp(radius)
    turtle.pencolor("red")
    drawCircle(radius)

def drawCircle(radius):
    turtle.circle(radius)

def orientDown(radius):
    turtle.penup()
    turtle.right(90)
    turtle.forward(radius)
    turtle.left(90)
    turtle.forward(radius)
    turtle.pendown()

def orientUp(radius):
    turtle.penup()
    turtle.left(90)
    turtle.forward(radius)
    turtle.right(90)
    turtle.forward(radius)
    turtle.pendown()

turtle.speed(1000)
drawOlympicCircles(100)
