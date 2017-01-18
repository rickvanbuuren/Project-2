import pygame
import sys
import time
from Player import Player
from Background import Background
from pygame.locals import *
from CONSTANTS import *

pygame.init()

class Main():
    def __init__(self, window, caption):
        self.window = window
        self.init = True
        self.caption = caption
        self.clock = pygame.time.Clock()
 

    def quit_condition(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return True
            return False

    def text_objects(self, text, font, color = WHITE):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()
    
    def display_text(self, display, size ,text, color, pos):
        used_font = size
        text_surface, text_rectangle = self.text_objects(text, used_font, color)
        text_rectangle.left, text_rectangle.top = pos
        display.blit(text_surface, text_rectangle)

    def create_button(self, display, content, x, y, w, h, ic, ac):
        mouse = pygame.mouse.get_pos()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(display, ac, [x, y, w, h])
        else:
            pygame.draw.rect(display, ic, [x, y, w, h])
        button_font = SMALL_FONT
        textSurf, textRect = self.text_objects(content, button_font)
        textRect.center = ((x+(w/2)), (y+(h/2)))
        display.blit(textSurf, textRect)
        


    def main_menu(self, display):
        BackGround = Background('resources/1960.png',[0,0])
        while not self.quit_condition():
            display.fill(WHITE)
            display.blit(BackGround.image, BackGround.rect)
            self.display_text(display, MED_FONT, "Euromast", BLACK, [self.window[0] * 0.415 - 35,20])
            ic, ac = BLACK, DARKBLACK
            self.create_button(display, "Start", self.window[0]/2 - 75, self.window[1] /2.5, 150, 50, ic, ac)
            self.create_button(display, "Highscores", self.window[0]/2 - 75, self.window[1] /2.5 + 60, 150, 50, ic, ac)
            self.create_button(display, "Help", self.window[0]/2 - 75, self.window[1] /2.5 + 120, 150, 50, ic, ac)
            self.create_button(display, "Quit", self.window[0]/2 - 75, self.window[1] /2.5 + 180, 150, 50, ic, ac)

            pygame.display.update()
            self.clock.tick(15)
        else:
            pygame.quit()
            sys.exit()


    def main(self):
        DISPLAYSURFACE = pygame.display.set_mode(self.window)
        pygame.display.set_caption(self.caption)
        while not self.quit_condition():
            if self.init:
                self.main_menu(DISPLAYSURFACE)
            else:
                DISPLAYSURFACE.fill(WHITE)
                self.display_text(DISPLAYSURFACE, "{Main game}", BLACK, [self.window[0] * 0.33,20])
                pygame.display.update()
                clock.tick(15)
        else:
            pygame.quit()
            sys.exit()


Euromast = Main((595, 800), "Euromast")
Euromast.main()