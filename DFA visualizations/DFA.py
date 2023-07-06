from functions import *

def q0():
    if squareClicked():
        moveSquare(10, 10)
        return q1
    elif circleClicked():
        moveCircle(90, 90)
        return q0
    return q0

def q1():
    if squareClicked():
        print("success")
    return q1
        