functions_square = [270, 240, 20, 20]
functions_circle = [250, 250]

interacted = False

def moveSquare(x, y):
    functions_square = [x, y, functions_square[2], functions_square[3]]

def moveCircle(x, y):
    functions_circle = [x, y]

def squareClicked():
    interacted = True
    pass

def circleClicked():
    interacted = True
    pass

def spacePressed():
    interacted = True
    pass
