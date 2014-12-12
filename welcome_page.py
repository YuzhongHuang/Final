import pygame as pyg
from pygame.locals import *
import test
from buttons import Button

def welcome_main():
    x = 620
    y = 1000
        # Writes window title text
    pyg.init()
    screen = pyg.display.set_mode((x, y))   # screen is what is displayed
    pyg.display.set_caption('Fruit Ninja')

    # background = pyg.image.load("fruit_ninja.jpeg").convert()
    # screen.blit(background, [0,292])
    
    # Create and draw background on Surface
    background_image = pyg.image.load("fruit_ninja.jpeg").convert()
    screen.blit(background_image, [0, 0])
    pyg.display.flip()
    
     # Make a play button
    play_button = Button()
    play = play_button.create_button(screen,(205,133,63), (x/4),300,(x/2) ,(y/5) , 0, "Play!", (255,255,255))
    playpos = play.get_rect()
    playpos.centerx = screen.get_rect().centerx   
    screen.blit(play, playpos)
    pyg.display.flip()
    
    # Make a rules button
    rules_button = Button()
    rule = rules_button.create_button(screen,(205,133,63), (x/4), (3*y/5), (x/2), (y/5), 0, "Rules", (255,255,255))
    rulespos = rule.get_rect()
    rulespos.centerx = screen.get_rect().centerx   
    screen.blit(rule, rulespos)
    pyg.display.flip()
    
    # Sets up exiting via the red X or the ESC key
    while True:
        for event in pyg.event.get():
            if event.type == QUIT:
                pyg.quit()
                return
            # elif event.type == KEYDOWN:
            #     if event.key == K_ESCAPE:
            #         pyg.quit()
            #         return
            elif event.type == MOUSEBUTTONDOWN: # Only register click on mouse button down.
                mouse_pos = pyg.mouse.get_pos()
                if rules_button.pressed(mouse_pos):
                    print 'Rules'
                if play_button.pressed(mouse_pos):
                    # pyg.quit()
                    test.test_main()
                    pyg.quit()
                    
                    # print 'Play Game'

                    
if __name__ == '__main__':
    welcome_main()
