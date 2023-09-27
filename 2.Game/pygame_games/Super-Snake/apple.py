from functions import *
from config import *


class Apple:
    def __init__(self, stones, snake):
        self.x, self.y = randLocationGen(stones.list, snake.list)

    def show(self, gameDisplay):
        gameDisplay.blit(APPLE, (self.x, self.y))
