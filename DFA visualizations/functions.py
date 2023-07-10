import math
import pygame as py

functions_square = []
functions_circle = []

function_circle_color = []
function_square_color = []

_circleClicked = False
_squareClicked = False
_spacePressed = False


def makeSquare(x, y, w=20, h=20, c=[0,255,0]):
    functions_square.append([x, y, w, h])
    function_square_color.append(c)

def makeCircle(x, y, r=10, c=[255, 0, 0]):
    functions_circle.append([x, y, r])
    function_circle_color.append(c)

def colorSquare(c, i=1):
    global function_square_color
    function_square_color[i-1] = c

def colorCircle(c, i=1):
    global function_circle_color
    function_circle_color[i-1] = c

def moveSquare(x, y, i=1):
    global functions_square
    functions_square[i-1][0] = x
    functions_square[i-1][1] = y

def moveCircle(x, y, i=1):
    global functions_circle
    functions_circle[i-1][0] = x
    functions_circle[i-1][1] = y

def changeCircleColor(red, green, blue, i=1):
    global function_circle_color
    function_circle_color[i-1][0] = red
    function_circle_color[i-1][1] = green
    function_circle_color[i-1][2] = blue

def changeSquareColor(red, green, blue, i=1):
    global function_square_color
    function_square_color[i-1][0] = red
    function_square_color[i-1][1] = green
    function_square_color[i-1][2] = blue

def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[0])**2)

def interactAt(pos1):
    for i in range(len(functions_circle)):
        circle = functions_circle[i]
        if distance(pos1, circle) <= 10:
            global _circleClicked
            _circleClicked = i+1
            break
    for i in range(len(functions_square)):
        square = functions_square[i]
        if pos1[0] >= square[0] and pos1[0] <= square[0] + square[2] \
        and pos1[1] >= square[1] and pos1[1] <= square[1] + square[3]:
            global _squareClicked
            _squareClicked = i+1
            break

def keypress(keymod):
    if keymod & py.K_SPACE:
        global _spacePressed
        _spacePressed = True
                
def interacted():
    return _circleClicked or _squareClicked or _spacePressed

def circleClicked():
    global _circleClicked
    return _circleClicked

def squareClicked():
    global _squareClicked
    return _squareClicked

def spacePressed():
    global _spacePressed
    return _spacePressed

def clearInteract():
    global _circleClicked
    global _squareClicked
    global _spacePressed
    _circleClicked = False
    _squareClicked = False
    _spacePressed = False

makeSquare(270, 240)
makeCircle(250, 250)
