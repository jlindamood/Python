import drawsquare

def lab3(numberSquares):
    drawsquare.drawSquare(100, 0)
    counter = 0
    while counter < numberSquares-1:
        drawsquare.drawSquare(100, 360/numberSquares)
        counter += 1

def main():
    x = int(input("How many squares do you want to draw?"))
    lab3(x)

if __name__ == '__main__':
    main()
