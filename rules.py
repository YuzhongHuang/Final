# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 14:11:12 2014

@author: Meg McCauley
"""

import pygame as pyg
import welcome_page
import buttons
import test2

from pygame.locals import *

def rules_main():
    
    pyg.init()
    pyg.font.init()
    screen = pyg.display.set_mode((620, 1000))   # screen is what is displayed
    
    # Apply background image
    background_image = pyg.image.load("background.jpeg")
    background_image = pyg.transform.scale(background_image,(620, 1000))
    pyg.display.set_icon(background_image)
    pyg.display.set_caption("Fruit Ninja Rules")
    screen.blit(background_image,[0,0])
    pyg.display.flip()
    
    trans = pyg.Surface((620,1000)) #starts at (0,0) and builds (width,height)
    trans.set_alpha(75) # 0 is invisible, 255 is solid, 128 is recommended
    trans.fill((0,0,0))
    screen.blit(trans,(0,0)) # refreshes the screen starting at (right,down)

    # Create the main menu button
    main_button = buttons.Button()
    main = main_button.create_button(background_image,(205,133,63), 0, 0, 150, 80, 0, "Main",(255,255,255))
    main_pos = main.get_rect()    
    screen.blit(main,main_pos)
    pyg.display.flip()

    playing_button = buttons.Button()
    playing = playing_button.create_button(background_image,(205,133,63), 470, 765, 150, 80, 0, "Play",(255,255,255))
    playing_pos = playing.get_rect()    
    screen.blit(playing,playing_pos)
    pyg.display.flip()
    
    title_font = pyg.font.Font(None, 60)
    
    # For loop to wrap text from rules_text.py
    skipline = (None,0)
    text_height = 100
    rules_list = [('1. Wear the blue gloves',1),('provided.',1),skipline,
              ('2. Wave your hands on',1),('all the shapes that pop',1),('up to "cut" all the fruit.',1), skipline,
              ('3. Try to cut as much',1),('fruit within the timed',1),('limit of a minute.',1)]
    
    for i in range(len(rules_list)):
        objective = title_font.render(rules_list[i][0], 1, (255,255,255))
        objective_pos = objective.get_rect()
        text_height += 50
        objective_pos.top = text_height
        objective_pos.left = 100   # Stay the same
        screen.blit(objective, objective_pos)   # Do every loop
    pyg.display.flip()
    
    # Checking for events (quitting, pressing buttons, etc.)
    while True:
        for event in pyg.event.get():
            if event.type == QUIT:
                pyg.quit()
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pyg.quit()
                    return
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pyg.mouse.get_pos()
                if main_button.pressed(mouse_pos):
                    welcome_page.welcome_main()
                    return
                elif playing_button.pressed(mouse_pos):
                    pyg.quit()
                    test2.test_main()
                    return

if __name__ == '__main__':
    from buttons import Button
    pyg.init()
    rules_main()