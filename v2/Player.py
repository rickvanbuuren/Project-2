import pygame

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super(Player, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((color))
        self.rect = self.surf.get_rect()
