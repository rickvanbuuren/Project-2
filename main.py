"""Kickoff PyGame example
Copyright 2017, Sjors van Gelderen
"""

import math
import pygame
# import database
from database import *

class Game:
    def __init__(self):
        # Set up resolution
        width = 640
        height = 480
        size = (width, height)

        red = (255, 0, 0)
        blue = (0, 0, 255)
        
        # Start PyGame
        pygame.init()
        
        # Set the resolution
        self.screen = pygame.display.set_mode(size)

        # Downloads score info
        self.score = download_top_score()
        
        # Set up the default font
        self.font = pygame.font.Font(None, 30)
        
        # Create an enemy
        self.enemy = Enemy(width * 0.8, height * 0.5, width * 0.1)
        
        # Create the player
        self.player = Player(width * 0.2, height * 0.5, width * 0.1)

        self.button1 = Button("start", 100, 100, 120, 120, red, blue)
        self.button2 = Button("start", 300, 50, 110, 67, red, blue)
        self.button3 = Button("start", 200, 150, 120, 120, red, blue)
        self.button4 = Button("start", 200, 200, 120, 120, red, blue)

    # Update game logic
    def update(self):
        # Update entities
        self.player.update()
        self.enemy.update(self.player, self)
        # self.button1.IsClicked()

    # Draw everything
    def draw(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))
        
        # Draw the entities
        self.enemy.draw(self.screen)
        self.player.draw(self.screen)
        
        self.button1.draw(self.screen)
        self.button2.draw(self.screen)
        self.button3.draw(self.screen)
        self.button4.draw(self.screen)
        
        
        # Draw the score text
        self.score_text = self.font.render("Score: {}".format(self.score),
                                           1, (255, 255, 255))
        self.screen.blit(self.score_text, (16, 16))
        
        # Flip the screen
        pygame.display.flip()
        
    def update_score(self):
        self.score += 10
        upload_score("abbadi", self.score)
        
    # The game loop
    def game_loop(self):
        while not process_events():
            self.update()
            self.draw()
            

class Player:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= 1
        elif keys[pygame.K_RIGHT]:
            self.x += 1

        if keys[pygame.K_UP]:
            self.y -= 1
        elif keys[pygame.K_DOWN]:
            self.y += 1
    
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0),
                           (int(self.x), int(self.y)), int(self.r))


class Enemy:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.health = 255

    def update(self, player, game):
        # If this enemy is colliding with the player
        if math.sqrt((player.x - self.x) ** 2 +
                     (player.y - self.y) ** 2) < self.r + player.r:
            self.health -= 1
            if self.health == 0:
                game.update_score()
                self.health = 255

    def draw(self, screen):
        pygame.draw.circle(screen, (self.health, 0, 0),
                           (int(self.x), int(self.y)), int(self.r))


class Button:
    def __init__(self, text, xPos, yPos, width, height, color, hover_color):
        self.text = text
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, 30)

    # def text_objects(self, text, font, color = WHITE):
    #     text_surface = font.render(text, True, color)
    #     return text_surface, text_surface.get_rect()

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()

        red = (255, 0, 0)
        blue = (0, 0, 255)

        if self.xPos + self.width > mouse[0] > self.xPos and self.yPos + self.height > mouse[1] > self.yPos:
            pygame.draw.rect(screen, self.hover_color, (int(self.xPos), int(self.yPos), int(self.width), int(self.height)), 0)
        else:
            pygame.draw.rect(screen, self.color, (int(self.xPos), int(self.yPos), int(self.width), int(self.height)), 0)

        # smallText = self.font
        # textSurf, textRect = text_objects("GO!", smallText)
        # textRect.center = ( (self.xPos+(self.width/2)), (self.yPos+(self.height/2)) )
        # self.screen.gameDisplay.blit(textSurf, textRect)

        # self.text = self.font.render("Score: {}".format(self.text), 1, (255, 255, 255))
        # self.screen.blit(self.text, (16, 16))
        

# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
    
    return False


# Main program logic
def program():
    game = Game()
    game.game_loop()


# Start the program
program()