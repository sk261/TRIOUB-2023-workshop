import pygame as py
import numpy as np
from functions import *
import DFA

py.init()

current_func = DFA.q0

screen = py.display.set_mode([500, 500])

running = True

_click_anim = []
click_anim_time = 300
_click_pos = []
_click_CD = 0
_click_CD_time = 10
_mousedown = False

while running:
    # Did the user click the window close button?
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            keypress(event.mod)
    if not np.array(py.mouse.get_pressed()).any():
        _mousedown = False
    elif _click_CD < py.time.get_ticks() and not _mousedown:
        _mousedown = True
        position = py.mouse.get_pos()
        interactAt(position)
        _click_anim.append(py.time.get_ticks() + click_anim_time)
        _click_CD = py.time.get_ticks() + _click_CD_time
        _click_pos.append(position)

    if interacted():
        new_func = current_func()
        if not new_func is None:
            current_func = new_func
        clearInteract()

    screen.fill((0,0,0))
    for i in range(len(functions_circle)):
        py.draw.circle(screen, function_circle_color[i], functions_circle[i][0:2], functions_circle[i][2])
    for i in range(len(functions_square)):
        py.draw.rect(screen, function_square_color[i], functions_square[i])

    # Click animation
    for i in range(len(_click_anim)-1, -1, -1):
        click_anim = _click_anim[i]
        click_pos = _click_pos[i]
        if click_anim > py.time.get_ticks():
            # draw 4 lines in the diagonal directions
            # 10 pixels out
            time_diff = click_anim - py.time.get_ticks()
            perc_change = abs(1 - (time_diff / click_anim_time))
            # up + left
            
            py.draw.line(screen, [200, 200, 200], \
            [click_pos[0] if perc_change < .5 else click_pos[0] - 20*(perc_change-.5), \
            click_pos[1] if perc_change < .5 else click_pos[1] - 20*(perc_change-.5)], \
            [click_pos[0] - 10*perc_change, click_pos[1] - 10*perc_change])
            
            # up + right
            py.draw.line(screen, [200, 200, 200], \
            [click_pos[0] if perc_change < .5 else click_pos[0] + 20*(perc_change-.5), \
            click_pos[1] if perc_change < .5 else click_pos[1] - 20*(perc_change-.5)], \
            [click_pos[0] + 10*perc_change, click_pos[1] - 10*perc_change])
            # down + left
            py.draw.line(screen, [200, 200, 200], \
            [click_pos[0] if perc_change < .5 else click_pos[0] - 20*(perc_change-.5), \
            click_pos[1] if perc_change < .5 else click_pos[1] + 20*(perc_change-.5)], \
            [click_pos[0] - 10*perc_change, click_pos[1] + 10*perc_change])
            # down + right
            
            py.draw.line(screen, [200, 200, 200], \
            [click_pos[0] if perc_change < .5 else click_pos[0] + 20*(perc_change-.5), \
            click_pos[1] if perc_change < .5 else click_pos[1] + 20*(perc_change-.5)], \
            [click_pos[0] + 10*perc_change, click_pos[1] + 10*perc_change])
        else:
            del _click_anim[i]
            del _click_pos[i]
            
    py.display.update()

py.quit()
