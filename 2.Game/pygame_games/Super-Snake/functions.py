import pygame
import random
from config import *


def rotate(segment, image):
    if segment[0] == "right":
        rotatedImage = pygame.transform.rotate(image, 0)
    elif segment[0] == "left":
        rotatedImage = pygame.transform.rotate(image, 180)
    elif segment[0] == "up":
        rotatedImage = pygame.transform.rotate(image, 90)
    elif segment[0] == "down":
        rotatedImage = pygame.transform.rotate(image, 270)
    return rotatedImage


def draw_text(gameDisplay, text, color, size, x, y):
    font = pygame.font.Font('fonts/flup.ttf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)


def score(gameDisplay, score):
    font = pygame.font.Font('fonts/flup.ttf', 25)
    text = font.render(str(score), True, czarny)
    gameDisplay.blit(text, [14, 14])


def randLocationGen(stonesList, snakeList):
    randX = round((random.randrange(block_size, display_width - 2 * block_size)) / block_size) * block_size
    randY = round((random.randrange(block_size, display_height - 2 * block_size)) / block_size) * block_size

    for stone in stonesList:
        for element in snakeList:
            if (randX == stone[0] and randY == stone[1]) or (randX == element[1] and randY == element[2]):
                print("!TEXT!" + str(randX) + str(element[1]) + str(randY) + str(element[2]))
                return randLocationGen(stonesList, snakeList)

    return randX, randY


def pause():
    draw_text("PAUSE", czarny, 60, display_width / 2, display_height / 2 - 130)
    draw_text("Press P to continue", czarny, 30, display_width / 2, display_height / 2)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return


