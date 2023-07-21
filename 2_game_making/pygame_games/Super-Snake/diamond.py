from functions import *
from config import *

class Diamond:
    def __init__(self):
        self.timer = 0
        self.x = None
        self.y = None
        
    def renew(self, stones, snake, FPS):
        self.timer = 10*FPS
        self.x, self.y = randLocationGen(stones.list, snake.list)
    
    def kill(self):
        self.timer = 0
        self.x = None
        self.y = None
        
    def show(self, gameDisplay, color):
        if self.timer > 0:
            self.timer -= 1
            if color == 'red':
                gameDisplay.blit(RED_DIAMOND, (self.x, self.y))
            elif color =='white':
                gameDisplay.blit(WHITE_DIAMOND, (self.x, self.y))
            elif color =='black':
                gameDisplay.blit(BLACK_DIAMOND, (self.x, self.y))
        else:
            self.kill()
