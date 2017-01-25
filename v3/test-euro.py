import pygame
import time

from Player import Player
from Block import Block
from pygame.locals import *
from CONSTANTS import *

pygame.init()

### Spelers hebben coordinaten, zo weten we waar ze zijn.

DISPLAYSURFACE = pygame.display.set_mode((800, 600))
DISPLAYSURFACER = DISPLAYSURFACE.get_rect()
DISPLAYSURFACE.fill((255, 255, 255))
b_blocks = {}
t_blocks = {}
running = True
clock = pygame.time.Clock()
players = 4
current_player = 0
current_view_player = 0
bp = Block(100,250,(0,0,0))
mp = Block(250,90,(0,0,0))
up = Block(50,250,(0,0,0))


def text_objects(text, font, color = WHITE):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

def display_text(display, size, text, color, pos):
    used_font = size
    text_surface, text_rectangle = text_object(text, used_font, color)
    text_rectangle.left, text_rectangle.top = pos
    display.blit(text_surface, text_rectangle)

def create_button(display, content, x, y, w, h, ic, ac, func=False, cargo=False):
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display, ac, [x,y,w,h])
        if func and pygame.mouse.get_pressed()[0] >= 1:
            # execute functions
            if func == draw_right or func == draw_left:
                func()
                time.sleep(.4)

    else:
        pygame.draw.rect(display, ic, [x,y,w,h])
    button_font = SMALL_FONT
    textSurf, textRect = text_objects(content, button_font)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    display.blit(textSurf, textRect)

def bp_init(tp = bp, y_range = 2, fp = 50, block_dict = b_blocks, size = (50, 25), block_colors = [(0,0,255), (255,0,0), (255,255,0), (0,0,0)]): # blue - red - yellow - black  / red - blue - black - yellow
    fp,sp = (0,0)
    o = 0
    for i in [i for i in range(4)]:
        for x in range(10):
            for y in range(y_range):
                block_dict.setdefault(i, {})[o] = {'block': Block(size[0],\
                        size[1],block_colors[i]), 'center': Block(10,5,(255, 255, 255)), \
                        'occupied': False, 'player': False}
                block_dict[i][o]['block'].image.blit(block_dict[i][o]['center'].image\
                        ,((block_dict[i][o]['block'].rect.width/2) - (block_dict[i][o]['center'].rect.width/2)\
                        ,block_dict[i][o]['block'].rect.height/2))
                tp.image.blit(block_dict[i][o]['block'].image,(fp,sp))
                fp += 50
                o += 1
            fp = 0
            sp +=25
        fp = 0
        o = 0

def draw_part(part=0):
    pass
def draw_left(current_player):
    pass
def draw_right():
    global current_view_player
    # Players 4(0,1,2,3) / Players 3(0,1,2) / Players 2(0,1)
    fp,sp=(0,0)
    o = 0
    if current_view_player+1 not in range(4):
        current_view_player = 0
        for key,value in b_blocks[0].items():
            bp.image.blit(value['block'].image, (fp,sp))
            if o == 1:
                fp=0
                o=0
                sp += 25
            else:
                fp+=50
                o+=1
        fp,sp = ((0,0))
        for key,value in t_blocks[0].items():
            up.image.blit(value['block'].image, (fp,sp))
            sp += 25
        current_view_player += 1
    else:
        for key, value in b_blocks[current_view_player].items():
            bp.image.blit(value['block'].image, (fp,sp))
            if o == 1:
                fp=0
                o=0
                sp += 25
            else:
                fp+=50
                o+=1
        fp,sp=(0,0)
        for key, value in t_blocks[current_view_player+1].items():
            up.image.blit(value['block'].image, (fp,sp))
            sp += 25
        current_view_player +=1
bp_init()
bp_init(up, 1, 50, t_blocks, (50,25),[(255,0,0), (0,0,255), (0,0,0), (255,255,0)]) # red - blue - black - yellow


ic,ac=(DARKBLACK,BLACK)

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == QUIT:
            running = False
    create_button(DISPLAYSURFACE, "Left", DISPLAYSURFACER.width/2 - 200, DISPLAYSURFACER.height - 100, 150, 50, ic, ac, draw_left)
    create_button(DISPLAYSURFACE, "Right", DISPLAYSURFACER.width/2 + 50, DISPLAYSURFACER.height - 100, 150, 50, ic, ac, draw_right)
    DISPLAYSURFACE.blit(bp.image, ((DISPLAYSURFACER.width/2)-(bp.rect.width/2), DISPLAYSURFACER.height - bp.rect.height))
    DISPLAYSURFACE.blit(mp.image, ((DISPLAYSURFACER.width/2)-(mp.rect.width/2), DISPLAYSURFACER.height - (bp.rect.height + mp.rect.height)))
    DISPLAYSURFACE.blit(up.image, ((DISPLAYSURFACER.width/2)-(up.rect.width/2), (DISPLAYSURFACER.height - bp.rect.height) - (bp.rect.height + mp.rect.height)))
    clock.tick(15)
    pygame.display.update()
