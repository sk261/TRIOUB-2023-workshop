import math
import pygame as py

functions_square = []
functions_square.append([270, 240, 20, 20])
functions_circle = []
functions_circle.append([250, 250])

function_circle_color = []
function_circle_color.append([255,0,0])
function_square_color = []
function_square_color.append([0, 255, 0])

_circleClicked = False
_squareClicked = False
_spacePressed = False

def moveSquare(x, y, i=0):
    global functions_square
    functions_square[i][0] = x
    functions_square[i][1] = y

def moveCircle(x, y, i=0):
    global functions_circle
    functions_circle[i][0] = x
    functions_circle[i][1] = y

def changeCircleColor(red, green, blue, i=0):
    global function_circle_color
    function_circle_color[i][0] = red
    function_circle_color[i][1] = green
    function_circle_color[i][2] = blue

def changeSquareColor(red, green, blue, i=0):
    global function_square_color
    function_square_color[i][0] = red
    function_square_color[i][1] = green
    function_square_color[i][2] = blue

def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[0])**2)

def interactAt(pos1):
    if distance(pos1, functions_circle) <= 10:
        global _circleClicked
        _circleClicked = True
    if pos1[0] >= functions_square[0] and pos1[0] <= functions_square[0] + functions_square[2] \
    and pos1[1] >= functions_square[1] and pos1[1] <= functions_square[1] + functions_square[3]:
        global _squareClicked
        _squareClicked = True

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
