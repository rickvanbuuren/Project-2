import sys, pygame
from pygame.locals import *


pygame.init()

DISPLAYSURF = pygame.display.set_mode((640, 480, FULLSCREEN))
pygame.display.set_caption("Euromast")

black = (0,0,0)
white = (255, 255, 255)
red   = (255, 0, 0)
green = (0, 200, 0)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def main_menu():
    current = True

    while current:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.quit()

        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                pygame.quit()
                sys.quit()

        DISPLAYSURF.fill(white)
        title = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Test", title)
        TextRect.center = ((275),(430))
        DISPLAYSURF.blit(TextSurf, TextRect)
        pygame.display.update()


def game():
    current = True

    while current:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.quit()

        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()

main_menu()
game()
