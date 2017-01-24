import pygame
import os
import sys

pygame.init()

class QuestionCard(pygame.sprite.Sprite):
    def __init__(self, color, image):
        super(QuestionCard, self).__init__()
        self.image = pygame.image.load(os.path.join('data', sys.path[0]+'/resources/questioncards/{}/{}'.format(color, image)))
        self.rect = self.image.get_rect()