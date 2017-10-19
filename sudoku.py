# By James Mason Lindamood, LINDA140.
# For CSCI 1133. Programming Exam #1

import turtle
import random
import math

# Global Variables and settings
# Board answers are saved, although an independent method solutionCheck() is also implemented below.
board1 = [[0, 0, 0, 3],
		  [0, 1, 0, 4],
		  [4, 2, 3, 1],
		  [1, 3, 4, 2]]

board1A = [[2, 4, 1, 3],
		   [3, 1, 2, 4],
		   [4, 2, 3, 1],
		   [1, 3, 4, 2]]

board2 = [[4, 3, 0, 0],
		  [1, 2, 3, 0],
		  [0, 0, 2, 0],
		  [2, 1, 0, 0]]

board2A = [[4, 3, 1, 2],
		   [1, 2, 3, 4],
		   [3, 4, 2, 1],
		   [2, 1, 4, 3]]

board3 = [[0, 4, 0, 1],
		  [3, 0, 4, 0],
		  [1, 0, 0, 4],
		  [0, 2, 1, 0]]

board3A = [[2, 4, 3, 1],
		   [3, 1, 4, 2],
		   [1, 3, 2, 4],
		   [4, 2, 1, 3]]

board4 = [[1, 0, 3, 0],
		  [0, 4, 2, 1],
		  [0, 0, 0, 2],
		  [0, 0, 4, 0]]

board4A = [[1, 2, 3, 4],
		   [3, 4, 2, 1],
		   [4, 3, 1, 2],
		   [2, 1, 4, 3]]

board5 = [[0, 4, 3, 2],
		  [3, 0, 0, 0],
		  [4, 1, 0, 0],
		  [0, 0, 4, 1]]

board5A = [[1, 4, 3, 2],
		   [3, 2, 1, 4],
		   [4, 1, 2, 3],
		   [2, 3, 4, 1]]

boards = [board1, board2, board3, board4, board5]
boardsA = [board1A, board2A, board3A, board4A, board5A]

# Coordinate turtles for writing values
a1 = turtle.Turtle()
a2 = turtle.Turtle()
a3 = turtle.Turtle()
a4 = turtle.Turtle()
b1 = turtle.Turtle()
b2 = turtle.Turtle()
b3 = turtle.Turtle()
b4 = turtle.Turtle()
c1 = turtle.Turtle()
c2 = turtle.Turtle()
c3 = turtle.Turtle()
c4 = turtle.Turtle()
d1 = turtle.Turtle()
d2 = turtle.Turtle()
d3 = turtle.Turtle()
d4 = turtle.Turtle()

coordinates = [[a1, b1, c1, d1], 
			   [a2, b2, c2, d2], 
			   [a3, b3, c3, d3], 
			   [a4, b4, c4, d4]]

for el in coordinates:
	for el2 in el:
		el2.speed(0)
		el2.ht()
		el2.penup()


# Screen writing turtle settings
screen = turtle.Screen()

turtle.speed(0)
turtle.hideturtle()
turtle.pencolor("black")
turtle.fillcolor("black")

def drawSquare(size):
	turtle.forward(size)
	turtle.left(90)
	turtle.forward(size)
	turtle.left(90)
	turtle.forward(size)
	turtle.left(90)
	turtle.forward(size)
	turtle.left(90)

def drawBoard(size, boardArg):

	startingPos = turtle.pos()

	#Draw thick edges
	turtle.width(10)

	drawSquare(size/2)
	turtle.penup()
	turtle.sety(turtle.ycor() + size/2)
	turtle.pendown()

	drawSquare(size/2)
	turtle.penup()
	turtle.setx(turtle.xcor() + size/2)
	turtle.pendown()

	drawSquare(size/2)
	turtle.penup()
	turtle.sety(turtle.ycor() - size/2)
	turtle.pendown()

	drawSquare(size/2)
	turtle.penup()

	#Draw thin edges
	turtle.width(5)

	#Vertical thin edges
	turtle.setx(turtle.xcor() + size/4)
	turtle.pendown()
	turtle.left(90)
	turtle.forward(size)
	turtle.left(90)
	turtle.forward(size/2)
	turtle.left(90)
	turtle.forward(size)

	#Horizontal thin edges
	turtle.right(90)
	turtle.forward(size/4)
	turtle.right(90)
	turtle.forward(size/4)
	turtle.right(90)
	turtle.forward(size)
	turtle.left(90)
	turtle.forward(size/2)
	turtle.left(90)
	turtle.forward(size)
	turtle.penup()

	#Reset turtle back to bottom left
	turtle.setpos(startingPos)

	#Set draw turtles according to the board parameter
	#Could rewrite this to use loops, but it works.
	a4.setpos(size/10, size/15)
	b4.setpos(size/10, size/15)
	c4.setpos(size/10, size/15)
	d4.setpos(size/10, size/15)
	b4.setx(a4.xcor() + size/4)
	c4.setx(b4.xcor() + size/4)
	d4.setx(c4.xcor() + size/4)

	a3.setpos(size/10, size/15 + size/4)
	b3.setpos(size/10, size/15 + size/4)
	c3.setpos(size/10, size/15 + size/4)
	d3.setpos(size/10, size/15 + size/4)
	b3.setx(a3.xcor() + size/4)
	c3.setx(b3.xcor() + size/4)
	d3.setx(c3.xcor() + size/4)

	a2.setpos(size/10, size/15 + 2*size/4)
	b2.setpos(size/10, size/15 + 2*size/4)
	c2.setpos(size/10, size/15 + 2*size/4)
	d2.setpos(size/10, size/15 + 2*size/4)
	b2.setx(a2.xcor() + size/4)
	c2.setx(b2.xcor() + size/4)
	d2.setx(c2.xcor() + size/4)

	a1.setpos(size/10, size/15 + 3*size/4)
	b1.setpos(size/10, size/15 + 3*size/4)
	c1.setpos(size/10, size/15 + 3*size/4)
	d1.setpos(size/10, size/15 + 3*size/4)
	b1.setx(a1.xcor() + size/4)
	c1.setx(b1.xcor() + size/4)
	d1.setx(c1.xcor() + size/4)

	for x in range(len(boardArg)):
		for y in range(len(boardArg[x])):
			if boardArg[x][y] != 0:
				coordinates[x][y].write(str(boardArg[x][y]), move=False, align="left", font=("Arial", 18, "normal"))

# This method is largely useless because each puzzle has one answer... but implemented for grading purposes.

def solutionCheck(checkBoard):

	boardArg1 = checkBoard[:]
	
	# Check each column. Forms a list equivalent to each column, sorts them, then checks if two elements are equal.
	for x in range(4):
		columnCheck = []
		for y in range(4):
			columnCheck.append(boardArg1[x][y])
	
		columnCheck.sort()
		
		for z in range(3):
			if columnCheck[z] == columnCheck[z+1] and columnCheck[z] != 0:
				print(columnCheck)
				print("Column failed!")
				return False

	# Checks each sub-square. Forms a list equivalent to each box, sorts them, then checks if two elements are equal.
	box1 = [boardArg1[0][0], boardArg1[0][1], boardArg1[1][0], boardArg1[1][1]]
	box1.sort()
	for x in range(3):
		if box1[x] == box1[x+1] and box1[x] != 0:
			print(box1)
			print("Box 1 failed")
			return False

	box2 = [boardArg1[0][2], boardArg1[0][3], boardArg1[1][2], boardArg1[1][3]]
	box2.sort()
	for x in range(3):
		if box2[x] == box2[x+1] and box2[x] != 0:
			print(box2)
			print("Box 2 failed")
			return False

	box3 = [boardArg1[3][0], boardArg1[3][1], boardArg1[2][1], boardArg1[2][0]]
	box3.sort()
	for x in range(3):
		if box3[x] == box3[x+1] and box3[x] != 0:
			print(box3)
			print("Box 3 failed")
			return False

	box4 = [boardArg1[2][2], boardArg1[2][3], boardArg1[3][2], boardArg1[3][3]]
	box4.sort()
	for x in range(3):
		if box4[x] == box4[x+1] and box4[x] != 0:
			print(box4)
			print("Box 4 failed")
			return False

	# Checks each row. Sorts each row, then checks if two elements are equal.
	for row in boardArg1:
		row.sort()
		for x in range(3):
			if row[x] == row[x+1] and row[x] != 0:
				print(row)
				print("Row failed!")
				return False

	# If this method makes it to this point, it has to result in True.
	columnCheck = []
	row = []
	return True


def sudoku():

	boardNumber = random.randint(1, 5)
	chosenBoard = boards[boardNumber - 1]
	chosenBoardAnswer = boardsA[boardNumber - 1]

	drawBoard(300, chosenBoard)

	screen.textinput("Play Sudoku!", "Each iteration will ask for an input. Coordinates are given by 1-4 + 1-4. I.E., Column 1, Row 1 will be '11'. You may rewrite values. Enter any input to continue.")
	realtimeCorrection = screen.textinput("Realtime Correction:", "Do you want to play with realtime correction? Input Y/N")

	while True:
		column = int(screen.numinput("Column Choice", "Which column? 1-4", 1, minval=1, maxval=4))
		row = int(screen.numinput("Row Choice", "Which row? 1-4", 1, minval=1, maxval=4))
		value = int(screen.numinput("Value Input", "What number to write? 1-4", 1, minval=1, maxval=4))

		if realtimeCorrection == "Y":
			realtimeCorrectionBoard = chosenBoard[:]
			realtimeCorrectionBoard[row-1][column-1] = value
			if value != chosenBoardAnswer[row - 1][column - 1] and solutionCheck(realtimeCorrectionBoard) == False:
				screen.textinput("Incorrect answer!", "The value you input is not a correct solution. Input any key to retry.")
				continue

		turtleToWrite = coordinates[row - 1][column - 1]

		if chosenBoard[row - 1][column - 1] != 0:
			turtleToWrite.clear()

		chosenBoard[row - 1][column - 1] = value
		turtleToWrite.write(str(value), move=False, align="left", font=("Arial", 18, "normal"))

		if chosenBoard == chosenBoardAnswer and solutionCheck(chosenBoard):
			screen.textinput("Winner, winner, chicken dinner!", "Your solution is correct. Input any key to close the program.")
			break

def main():
	sudoku()

main()