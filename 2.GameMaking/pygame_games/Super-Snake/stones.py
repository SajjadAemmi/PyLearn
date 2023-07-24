from functions import *
from config import *


class Stones:
    def __init__(self):
        self.list = []

    def add(self, other):
        newStoneX, newStoneY = randLocationGen(self.list, other.list)
        newStone = [newStoneX, newStoneY]
        self.list.append(newStone)
        
    def show(self, gameDisplay):
        for i in range(len(self.list)):
            gameDisplay.blit(STONE, (self.list[i][0],self.list[i][1]))
            
    def destroy(self, stone):
        self.list.remove(stone)
