import pygame
import time

from pygame.locals import *

pygame.init()

block = pygame.sprite.Group()
class Block(pygame.sprite.Sprite):
    def __init__(self,x,y,c):
        pygame.sprite.Sprite.__init__(self, block)
        self.image = pygame.Surface((x,y))
        self.image.fill(c)
        self.rect = self.image.get_rect()