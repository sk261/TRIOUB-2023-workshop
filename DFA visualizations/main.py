import pygame as py
import numpy as np
from functions import *
import DFA

py.init()

current_func = DFA.q0

screen = py.display.set_mode([500, 500])

running = True
while running:
    # Did the user click the window close button?
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    py.mouse.get_pressed()
    if interacted:
        new_func = current_func()
        if not new_func is None:
            current_func = new_func
        interacted = False
    py.draw.circle(screen, [255,0,0], functions_circle, 10)
    py.draw.rect(screen, [0,255,0], functions_square)
    py.display.update()

py.quit()
