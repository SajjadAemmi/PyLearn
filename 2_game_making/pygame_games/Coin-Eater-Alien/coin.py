import random
import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, game_width, game_height):
        super(Coin, self).__init__()
        self.image = pygame.image.load("images/coin_gold.png").convert_alpha()
        self.x = random.randint(10, game_width - 10)
        self.y = random.randint(10, game_height - 10)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
