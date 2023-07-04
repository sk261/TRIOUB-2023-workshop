from functions import *

def q0():
    if squareClicked():
        moveSquare(10, 10)
        return q1
    elif circleClicked():
        moveCircle(90, 90)

def q1():
    if squareClicked():
        print("success")