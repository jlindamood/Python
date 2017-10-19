import turtle
import random

#Create the 3 turtles
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()
turtles = [turtle1, turtle2, turtle3]
turtle.hideturtle()

#Position the turtles at the starting line
for turtleObject in turtles:
    turtleObject.penup()
    turtleObject.back(turtle.window_width() * .5)
    turtleObject.shape("turtle")
turtle1.left(90)
turtle1.forward(100)
turtle1.right(90)
turtle1.color("red")
turtle3.right(90)
turtle3.forward(100)
turtle3.left(90)
turtle3.color("blue")

while True:
    for turtleObject in turtles:
        steps = random.randint(1, 15)
        turtleObject.forward(steps)
        if (turtleObject.xcor() > (turtle.window_width() * .5)):
            print("A turtle won!")
            exit(0)
