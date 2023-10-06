import os
import pygame


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.font.init()
pygame.mixer.init()

display_width = 900
display_height = 600
block_size = 30
FPS = 10

bialy = (255, 255, 255)
czarny = (0, 0, 0)
czerwony = (255, 0, 0)
LIGHT_RED = (155, 0, 0)
ciemnyZielony = (0, 120, 0)

background = pygame.image.load('images/TLONOWE2.jpg')
wall = pygame.image.load('images/wall2.gif')

START = pygame.image.load('images/PRISMA1.jpg')
CONTROLS = pygame.image.load('images/PRISMA2.jpg')
GAMEOVER = pygame.image.load('images/GAMEOVER.png')

TIMERBACKGROUND = pygame.image.load('images/TIMERBACKGROUND.png')

ACTIVE_B = pygame.image.load('images/ACTIVE.png')
INACTIVE_B = pygame.image.load('images/INACTIVE.png')

POINT = pygame.mixer.Sound("sounds/sfx_point.wav")
HIT = pygame.mixer.Sound("sounds/sfx_hit.wav")
EVOLUTION = pygame.mixer.Sound("sounds/Star_Wars_-_Imperial_march.wav")
STONEDESTROY = pygame.mixer.Sound("sounds/STONEDESTROY.wav")

HEAD = pygame.image.load('images/snakehead30x30.png')
TAIL = pygame.image.load('images/snaketail30x30.png')
BODY = pygame.image.load('images/snakebody30x30.png')
TURNLEFT = pygame.image.load('images/turnleft30x30.png')
TURNRIGHT = pygame.image.load('images/turnright30x30.png')

SUPERHEAD = pygame.image.load('images/supersnakehead30x30.png')
SUPERTAIL = pygame.image.load('images/supersnaketail30x30.png')
SUPERBODY = pygame.image.load('images/supersnakebody30x30.png')
SUPERTURNLEFT = pygame.image.load('images/superturnleft30x30.png')
SUPERTURNRIGHT = pygame.image.load('images/superturnright30x30.png')

RED_DIAMOND = pygame.image.load('images/RED_DIAMOND.png')
WHITE_DIAMOND = pygame.image.load('images/WHITE_DIAMOND.png')
WHITE_DIAMOND_BIG = pygame.image.load('images/WHITE_DIAMOND_BIG.png')
BLACK_DIAMOND = pygame.image.load('images/BLACK_DIAMOND.png')
BLACK_DIAMOND_BIG = pygame.image.load('images/BLACK_DIAMOND_BIG.png')

STONE = pygame.image.load('images/stone.gif')
STONE_BIG = pygame.image.load('images/ROCK_BIG.png')

APPLE = pygame.image.load('images/NEWAPPLE.png')
APPLE_BIG = pygame.image.load('images/NEWAPPLE_BIG.png')
