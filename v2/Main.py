import pygame
import sys
import time
import inputbox
import random

from Player import Player
from Background import Background
from pygame.locals import *
from CONSTANTS import *

pygame.init()

class Main():
    def __init__(self, window, caption):
        self.window = window
        self.init = True
        self.player_count = 0
        self.players = []
        self.caption = caption
        self.clock = pygame.time.Clock()
		
    def dice(min = 1, max = 6):
        return random.randint(min, max)

    def quit_condition(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return True
            return False

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def text_objects(self, text, font, color = WHITE):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()
    
    def display_text(self, display, size ,text, color, pos):
        used_font = size
        text_surface, text_rectangle = self.text_objects(text, used_font, color)
        text_rectangle.left, text_rectangle.top = pos
        # text_rectangle.width = self.window[0] * 0.80
        display.blit(text_surface, text_rectangle)

    def create_button(self, display, content, x, y, w, h, ic, ac, func=False, cargo=False):
        mouse = pygame.mouse.get_pos()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(display, ac, [x, y, w, h])
            if func and pygame.mouse.get_pressed()[0] >= 1:
                pygame.time.wait(100)
                print(func.__name__)
                if func == self.main:
                    self.init = False
                    func()
                elif func == self.rule_menu or func == self.main_menu or func == self.player_menu or func == self.player_name_menu or func == self.switch_board_left:
                    if cargo:
                        self.player_count = cargo
                    func(display)
                else:
                    func()
        else:
            pygame.draw.rect(display, ic, [x, y, w, h])
        button_font = SMALL_FONT
        textSurf, textRect = self.text_objects(content, button_font)
        textRect.center = ((x+(w/2)), (y+(h/2)))
        display.blit(textSurf, textRect)

    def rule_menu(self, display):
        rules = open("resources/text.txt", "r")
        display.fill(WHITE)
        while not self.quit_condition():
            
            self.create_button(display, "Terug", 0, 0, 150, 50, DARKBLACK, BLACK, self.main_menu)
            h = 70
            for rule in rules:
                self.display_text(display, TINY_FONT, rule, BLACK, [1, h])
                h += 20
            pygame.display.update()
            self.clock.tick(15)
            # please delete me

        else:
            self.quit_game()


    def main_menu(self, display):
        BackGround = Background('resources/1960.png',[0,0])

        self.players = []
        self.player_count = 0
        
        while not self.quit_condition():
            display.fill(WHITE)
            display.blit(BackGround.image, BackGround.rect)
            self.display_text(display, MED_FONT, "Euromast", BLACK, [self.window[0] * 0.415 - 35,20])
            ic, ac = BLACK, DARKBLACK
            self.create_button(display, "Start", self.window[0]/2 - 75, self.window[1] /2.5, 150, 50, ic, ac, self.player_menu)
            self.create_button(display, "Ranglijst", self.window[0]/2 - 75, self.window[1] /2.5 + 60, 150, 50, ic, ac)
            self.create_button(display, "Spelregels", self.window[0]/2 - 75, self.window[1] /2.5 + 120, 150, 50, ic, ac, self.rule_menu)
            self.create_button(display, "Afsluiten", self.window[0]/2 - 75, self.window[1] /2.5 + 180, 150, 50, ic, ac, self.quit_game)
            pygame.display.update()
            self.clock.tick(15)
        else:
            self.quit_game()

    def player_menu(self, display):
        display.fill(WHITE)
        ic, ac = BLACK, DARKBLACK
        while not self.quit_condition():
            self.create_button(display, "2 Spelers", self.window[0]/2 - 50, self.window[1] /2.5, 100, 50, ic, ac, self.player_name_menu, 2)
            self.create_button(display, "3 Spelers", self.window[0]/2 - 50, self.window[1] /2.5 + 60, 100, 50, ic, ac, self.player_name_menu, 3)
            self.create_button(display, "4 Spelers", self.window[0]/2 - 50, self.window[1] /2.5 + 120, 100, 50, ic, ac, self.player_name_menu, 4)

            pygame.display.update()
            self.clock.tick(15)
        else:
            self.quit_game()

    def switch_board_left(self, display):
        boardColors = [LIME, PURPLE, MAROON, TEAL]
        print("left")
        self.built_tower(display, boardColors[0])

    def switch_board_right(self, display):
        pass

    def built_tower(self, display, color):
        posX_start = self.window[0] * 0.3
        posY_start = self.window[0] * 0.3

        boxWidth = 50
        boxHeight = 25

        distance = 4
        
        posX = [posX_start, posX_start + (boxWidth * 1) + (distance * 1)]
        
        posY = [posY_start, 
        posY_start + (boxHeight * 1) + (distance * 1), 
        posY_start + (boxHeight * 2) + (distance * 2), 
        posY_start + (boxHeight * 3) + (distance * 3),
        posY_start + (boxHeight * 4) + (distance * 4),
        posY_start + (boxHeight * 5) + (distance * 5),
        posY_start + (boxHeight * 6) + (distance * 6),
        posY_start + (boxHeight * 7) + (distance * 7),
        posY_start + (boxHeight * 8) + (distance * 8),
        posY_start + (boxHeight * 9) + (distance * 9)]


        i = 0

        for y in range(0, 10):
            for x in range(0, 2):
                Torenblokje = pygame.draw.rect(display, color, (posX[i], posY[y], boxWidth, boxHeight))
                print("in loop")
            Torenblokje = pygame.draw.rect(display, color, (posX[i+1], posY[y], boxWidth, boxHeight))     

    def player_name_menu(self, display):
        display.fill(WHITE)

        while not self.quit_condition():
            if len(self.players) != self.player_count:

                for i in range(self.player_count):
                    self.players.append(inputbox.ask(display, "Naam van Speler " + str(i + 1)))
            else:
                self.init = False
                self.main()
        else:
            self.quit_game()


    def main(self):
        DISPLAYSURFACE = pygame.display.set_mode(self.window)
        pygame.display.set_caption(self.caption)
        px, py = self.window[0]/2 - 25, self.window[1]-50
        ic, ac = BLACK, DARKBLACK
        playerColors = [BLUE, FUCHSIA, YELLOW, GREEN]
        DISPLAYSURFACE.fill(WHITE)
        self.built_tower(DISPLAYSURFACE, BLUE)
        keyboard = pygame.key.get_pressed()

        for i in range(len(self.players)):
            pygame.draw.circle(DISPLAYSURFACE, playerColors[i], [int(self.window[0] * 0.3 + 10 + (i * 25)), int(600 - 20)], 10)

        while not self.quit_condition():
            yc = 0
            if self.init:
                self.main_menu(DISPLAYSURFACE)
            else:
                self.create_button(DISPLAYSURFACE, "Hoofdmenu", 0, 0, 120, 50, ic, ac, self.main_menu)
                self.create_button(DISPLAYSURFACE, "End Turn", 680, 550, 120, 50, ic, ac, self.main_menu)
                self.create_button(DISPLAYSURFACE, "<---", 800 - 670, 600 - 100, 90, 40, ic, ac, self.switch_board_left)
                self.create_button(DISPLAYSURFACE, "--->", 800 - 440, 600 - 100, 90, 40, ic, ac, self.switch_board_right)  

                py -= yc
                pygame.display.update()
                self.clock.tick(15)
        else:
            self.quit_game()


Euromast = Main((800, 600), "Euromast")
Euromast.main()
