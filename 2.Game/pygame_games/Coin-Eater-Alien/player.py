import pygame
from typing import Tuple


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("images/alien_green_stand.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.score = 0

    def update(self, pos: Tuple):
        """Update the position of the player

        Arguments:
            pos {Tuple} -- the (X,Y) position to move the player
        """
        self.rect.center = pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)
