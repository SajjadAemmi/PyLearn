import random
import pygame
from src.color import Color


class Apple:
    def __init__(self, config):
        self.x = random.randint(40, config.game_width - 40) // 20 * 20
        self.y = random.randint(40, config.game_height - 40) // 20 * 20
        self.radius = 10
        self.color = Color.red

    def draw(self, display):
        return pygame.draw.circle(display, self.color, [self.x + self.radius, self.y + self.radius], self.radius)
