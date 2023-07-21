from functions import *
from config import *

class Snake:
    def __init__(self, lead_x, lead_y):
        self.direction = "right"
        self.list = [["right", lead_x-2*block_size, lead_y],
                     ["right", lead_x-block_size, lead_y],
                     ["right", lead_x, lead_y]]
                          
        self.head = ["right", lead_x, lead_y]
        self.length = 3
        self.superTimer = 0
        
    def superSnake(self, FPS):
        self.superTimer = 10*FPS
        
    def update(self, lead_x, lead_y):
        self.head = []
        self.head.append(self.direction)
            
        self.head.append(lead_x)
        self.head.append(lead_y)
        
        self.list.append(self.head)
        
        if len(self.list) > self.length:
            del self.list[0]

        if self.superTimer > 0:
            self.superTimer -= 1

    def show(self, gameDisplay, FPS):
        if self.superTimer > 0:
            self.view(gameDisplay, SUPERHEAD, SUPERTAIL, SUPERBODY, SUPERTURNLEFT, SUPERTURNRIGHT)
            gameDisplay.blit(TIMERBACKGROUND, (800, 529))
            font = pygame.font.Font('flup.ttf', 25)
            text = font.render(str(self.superTimer/FPS), True, czarny)
            gameDisplay.blit(text, [830,537])
        else:
            self.view(gameDisplay, HEAD, TAIL, BODY, TURNLEFT, TURNRIGHT)
                
    def view(self, gameDisplay, head, tail, body, turnleft, turnright):
        gameDisplay.blit(rotate(self.list[-1],head), (self.list[-1][1],self.list[-1][2]))       
        gameDisplay.blit(rotate(self.list[1],tail), (self.list[0][1],self.list[0][2]))
            
        for i in range(1, self.length-1):     
            if self.list[i][0] == self.list[i+1][0]:
                gameDisplay.blit(rotate(self.list[i],body), (self.list[i][1],self.list[i][2]))
            
            elif (self.list[i][0] == "down" and self.list[i+1][0] == "right") or (self.list[i][0] == "right" and self.list[i+1][0] == "up") or (self.list[i][0] == "up" and self.list[i+1][0] == "left") or (self.list[i][0] == "left" and self.list[i+1][0] == "down"):       
                gameDisplay.blit(rotate(self.list[i+1],turnleft), (self.list[i][1],self.list[i][2]))
            
            elif (self.list[i][0] == "right" and self.list[i+1][0] == "down") or (self.list[i][0] == "down" and self.list[i+1][0] == "left") or (self.list[i][0] == "left" and self.list[i+1][0] == "up") or (self.list[i][0] == "up" and self.list[i+1][0] == "right"):        
                gameDisplay.blit(rotate(self.list[i+1],turnright), (self.list[i][1],self.list[i][2]))
        
    def isDead(self, other):
        for eachSegment in self.list[:-1]:
            if eachSegment[1] == self.head[1] and eachSegment[2] == self.head[2]:
                HIT.play()
                pygame.mixer.music.set_volume(0.2)
                return True
                
        if self.superTimer <= 0:
            for eachStone in other.list:
                if eachStone[0] == self.head[1] and eachStone[1] == self.head[2]:
                    HIT.play()
                    return True
                    
            if self.head[1] >= display_width-block_size or self.head[1] < block_size or self.head[2] >= display_height-block_size or self.head[2] < block_size:
                HIT.play()
                return True
                
        return False
        
    def trim(self):
        if len(self.list) > 13:
            self.list = self.list[10:]
            self.length -= 10
