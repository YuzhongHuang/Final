import pygame as pyg
from pygame.locals import *
import test2
from buttons import Button
import buttons
import welcome_page

def score_main(score):
    x = 620
    y = 700
        # Writes window title text
    pyg.init()
    screen = pyg.display.set_mode((x, y))   # screen is what is displayed
    pyg.display.set_caption('Fruit Ninja')

    background_img = pyg.image.load("fruit_ninja.jpeg").convert()
    screen.blit(background_img, [0,0])
    pyg.display.flip()
    
    # Create and draw background on Surface
    # background = pyg.image.load("fruit_ninja.jpeg").convert()
    
    # background = pyg.Surface(screen.get_size())
    # background = background.convert()
    # background.fill((0, 0, 0))
    # pyg.display.flip()

    font = pyg.font.Font(None, 80)
    text = font.render("Your final score is %s" %(score), 1, (255, 255, 255))
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    
    if score>=100:
        screen.blit(text, (20, 350))
    elif score>=10 and score<100:
        screen.blit(text, (35, 350))
    else:
        screen.blit(text, (47, 350))
    # screen.blit(background, [200, 0])
    # Sets up exiting via the red X or the ESC key

    again_button = buttons.Button()
    again = again_button.create_button(screen,(205,133,63), 0, 480, 620, 80, 0, "Play More",(255,255,255))
    again_pos = again.get_rect()
    # again_pos.centerx = screen.get_rect().centerx        
    screen.blit(again,again_pos)
    # pyg.display.flip()

    quit_button = buttons.Button()
    quitting = quit_button.create_button(screen,(205,133,63), 0, 600, 620, 80, 0, "Quit Game",(255,255,255))
    quit_pos = quitting.get_rect()
    # quit_pos.centerx = screen.get_rect().centerx        
    screen.blit(quitting,quit_pos)
    pyg.display.flip()
    
    while True:
        pyg.init()
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
                if again_button.pressed(mouse_pos):
                    pyg.quit()
                    test2.test_main()
                    return
                elif quit_button.pressed(mouse_pos):
                    pyg.quit()
                    return
        # screen.blit(background, (0, 0))
        pyg.display.flip()
                    
if __name__ == '__main__':
    score_main(score)
