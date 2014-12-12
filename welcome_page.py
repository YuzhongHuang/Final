import pygame as pyg
from pygame.locals import *
import test

"""Button class sourced from Simon H. Larsen, http://lagusan.com/button-drawer-python-2-6/"""

class Button:
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pyg.Rect(x,y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = int(length//len(text))
        myFont = pyg.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):           
        for i in range(1,10):
            s = pyg.Surface((length+(i*2),height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pyg.draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
            surface.blit(s, (x-i,y-i))
        pyg.draw.rect(surface, color, (x,y,length,height), 0)
        pyg.draw.rect(surface, (190,190,190), (x,y,length,height), 1)  
        return surface
    
    def pressed(self, mouse_pos):
        if mouse_pos[0] > self.rect.topleft[0] and mouse_pos[1] > self.rect.topleft[1] and mouse_pos[0] < self.rect.bottomright[0] and mouse_pos[1] < self.rect.bottomright[1]:
            # print "Some button was pressed!"
            return True
        else: return False

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
    
     # Make a blue 2 player button
    play_button = Button()
    play = play_button.create_button(screen,(205,133,63), (x/4),300,(x/2) ,(y/5) , 0, "Play!", (255,255,255))
    playpos = play.get_rect()
    playpos.centerx = screen.get_rect().centerx   
    screen.blit(play, playpos)
    pyg.display.flip()
    
    # Make a purple rules button
    rules_button = Button()
    rule = rules_button.create_button(screen,(205,133,63), (x/4), (3*y/5), (x/2), (y/5), 0, "Rules", (255,255,255))
    rulespos = rule.get_rect()
    rulespos.centerx = screen.get_rect().centerx   
    screen.blit(rule, rulespos)
    pyg.display.flip()
    
    # Display title text
    # font = pyg.font.Font(None, 80)
    # text = font.render("Fruit Ninja", 1, (10, 10, 10))
    # textpos = text.get_rect()
    # textpos.centerx = screen.get_rect().centerx
    # screen.blit(text, textpos)
    # pyg.display.flip()
    
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