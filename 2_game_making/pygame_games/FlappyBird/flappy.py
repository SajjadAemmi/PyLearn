from itertools import cycle
import random
import sys

import pygame
from pygame.locals import *

pygame.init()

class Bird:
    def __init__(self):
        PLAYERS_LIST = (
            # red bird
            ('sprites/redbird-upflap.png', 'sprites/redbird-midflap.png', 'sprites/redbird-downflap.png'),
            # blue bird
            ('sprites/bluebird-upflap.png', 'sprites/bluebird-midflap.png', 'sprites/bluebird-downflap.png'),
            # yellow bird
            ('sprites/yellowbird-upflap.png', 'sprites/yellowbird-midflap.png', 'sprites/yellowbird-downflap.png'),
        )

        # select random player sprites
        r = random.choice(PLAYERS_LIST)
        self.images = (pygame.image.load(r[0]), pygame.image.load(r[1]), pygame.image.load(r[2]))

        self.w = self.images[0].get_width()
        self.h = self.images[0].get_height()

        self.Index = 0
        # player velocity, max velocity, downward accleration, accleration on flap
        self.VelY    =  -9   # player's velocity along Y, default same as playerFlapped
        self.MaxVelY =  10   # max vel along Y, max descend speed
        self.MinVelY =  -8   # min vel along Y, max ascend speed
        self.AccY    =   1   # players downward accleration
        self.Rot     =  45   # player's rotation
        self.VelRot  =   3   # angular speed
        self.RotThr  =  20   # rotation threshold
        self.FlapAcc =  -9   # players speed on flapping
        self.Flapped = False # True when player flaps

        self.IndexGen = cycle([0, 1, 2, 1])
        # iterator used to change playerIndex after every 5th iteration
        self.loopIter = 0

        # player shm for up-down motion on welcome screen
        self.Shm = {'val': 0, 'dir': 1}

        self.x = int(Game.width * 0.2)
        self.y = int((Game.height - self.images[0].get_height()) / 2)

    def move(self):
            # rotate the player
        if self.Rot > -90:
            self.Rot -= self.VelRot

        # player's movement
        if self.VelY < self.MaxVelY and not self.Flapped:
            self.VelY += self.AccY
        if self.Flapped:
            self.Flapped = False
            self.Rot = 45  # more rotation to cover the threshold (calculated in visible rotation)

        self.Height = self.images[self.Index].get_height()
        self.y += min(self.VelY, Game.BASEY - self.y - self.Height)

    def show(self):
        # Player rotation has a threshold
        visibleRot = self.RotThr
        if self.Rot <= self.RotThr:
            visibleRot = self.Rot
        
        playerSurface = pygame.transform.rotate(self.images[self.Index], visibleRot)
        self.rect = Game.screen.blit(playerSurface, (self.x, self.y + self.Shm['val']))
    
    def playerShm(self):
        """oscillates the value of playerShm['val'] between 8 and -8"""
        if abs(self.Shm['val']) == 8:
            self.Shm['dir'] *= -1

        if self.Shm['dir'] == 1:
            self.Shm['val'] += 1
        else:
            self.Shm['val'] -= 1
    
    def checkCrash(self):
        """returns True if player collders with base or pipes."""
        # if player crashes into ground
        if self.y + self.h >= Game.BASEY - 1:
            return [True, True]
        
        # if bird collided with upipe or lpipe
        for pipe in Game.pipes:
            if self.rect.colliderect(pipe.upperPartRect) or self.rect.colliderect(pipe.lowerPartRect):
                return [True, False]

        return [False, False]


class Pipe:
    PIPES_LIST = ('sprites/pipe-green.png', 'sprites/pipe-red.png')
    pipeindex = random.choice(PIPES_LIST)
    images = (
        pygame.transform.flip(pygame.image.load(pipeindex), False, True),
        pygame.image.load(pipeindex),
    )
    GAPSIZE = 150 # gap between upper and lower part of pipe
    
    def __init__(self):
        self.VelX = -4
        gapY = random.randrange(0, int(Game.BASEY * 0.6 - Pipe.GAPSIZE))  # y of gap between upper and lower pipe
        gapY += int(Game.BASEY * 0.2)
        pipeHeight = self.images[0].get_height()
        pipeX = Game.width + 10
        self.upperPart = {'x': pipeX, 'y': gapY - pipeHeight}
        self.lowerPart = {'x': pipeX, 'y': gapY + Pipe.GAPSIZE}
    
    def move(self):
        self.upperPart['x'] += self.VelX
        self.lowerPart['x'] += self.VelX
    
    def show(self):
        self.upperPartRect = Game.screen.blit(self.images[0], (self.upperPart['x'], self.upperPart['y']))
        self.lowerPartRect = Game.screen.blit(self.images[1], (self.lowerPart['x'], self.lowerPart['y']))


class Game:
    FPS = 30
    width = 288
    height = 512
    BASEY = height * 0.79
    images, sounds = {}, {}
    BACKGROUNDS_LIST = ('sprites/background-day.png', 'sprites/background-night.png')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Flappy Bird')

    # numbers sprites for score display
    images['numbers'] = (
        pygame.image.load('sprites/0.png'), pygame.image.load('sprites/1.png'),
        pygame.image.load('sprites/2.png'), pygame.image.load('sprites/3.png'),
        pygame.image.load('sprites/4.png'), pygame.image.load('sprites/5.png'),
        pygame.image.load('sprites/6.png'), pygame.image.load('sprites/7.png'),
        pygame.image.load('sprites/8.png'), pygame.image.load('sprites/9.png')
    )

    # game over sprite
    images['gameover'] = pygame.image.load('sprites/gameover.png')
    # message sprite for welcome screen
    images['message'] = pygame.image.load('sprites/message.png')
    # base (ground) sprite
    images['base'] = pygame.image.load('sprites/base.png')

    # sounds
    soundExt = '.wav' if 'win' in sys.platform else '.ogg'

    sounds['die']    = pygame.mixer.Sound('audio/die' + soundExt)
    sounds['hit']    = pygame.mixer.Sound('audio/hit' + soundExt)
    sounds['point']  = pygame.mixer.Sound('audio/point' + soundExt)
    sounds['swoosh'] = pygame.mixer.Sound('audio/swoosh' + soundExt)
    sounds['wing']   = pygame.mixer.Sound('audio/wing' + soundExt)

    @staticmethod
    def newGame():
        while True:
            # select random background sprites
            randBg = random.choice(Game.BACKGROUNDS_LIST)
            Game.images['background'] = pygame.image.load(randBg).convert()

            Game.bird = Bird()
            Game.pipes = [Pipe()]

            movementInfo = Game.showWelcomeAnimation()
            crashInfo = Game.play(movementInfo)
            Game.showGameOverscreen(crashInfo)

    @staticmethod
    def showWelcomeAnimation():
        """Shows welcome screen animation of flappy bird"""
        messagex = int((Game.width - Game.images['message'].get_width()) / 2)
        messagey = int(Game.height * 0.12)

        basex = 0
        # amount by which base can maximum shift to left
        baseShift = Game.images['base'].get_width() - Game.images['background'].get_width()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    # make first flap sound and return values for mainGame
                    Game.sounds['wing'].play()
                    return {
                        'playery': Game.bird.y + Game.bird.Shm['val'],
                        'basex': basex,
                        'playerIndexGen': Game.bird.IndexGen,
                    }

            # adjust playery, playerIndex, basex
            if (Game.bird.loopIter + 1) % 5 == 0:
                Game.bird.Index = next(Game.bird.IndexGen)
            Game.bird.loopIter = (Game.bird.loopIter + 1) % 30
            basex = -((-basex + 4) % baseShift)
            Game.bird.playerShm()

            # draw sprites
            Game.screen.blit(Game.images['background'], (0,0))
            Game.bird.show()

            Game.screen.blit(Game.images['message'], (messagex, messagey))
            Game.screen.blit(Game.images['base'], (basex, Game.BASEY))

            pygame.display.update()
            Game.clock.tick(Game.FPS)

    @staticmethod
    def play(movementInfo):
        score = loopIter = 0
        basex = movementInfo['basex']
        baseShift = Game.images['base'].get_width() - Game.images['background'].get_width()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    if Game.bird.y > -2 * Game.bird.images[0].get_height():
                        Game.bird.VelY = Game.bird.FlapAcc
                        Game.bird.Flapped = True
                        Game.sounds['wing'].play()

            # check for score
            Game.bird.MidPos = Game.bird.x + Game.bird.images[0].get_width() / 2
            for pipe in Game.pipes:
                pipeMidPos = pipe.upperPart['x'] + pipe.images[0].get_width() / 2
                if pipeMidPos <= Game.bird.MidPos < pipeMidPos + 4:
                    score += 1
                    Game.sounds['point'].play()

            # playerIndex basex change
            if (loopIter + 1) % 3 == 0:
                Game.bird.Index = next(Game.bird.IndexGen)
            loopIter = (loopIter + 1) % 30
            basex = -((-basex + 100) % baseShift)

            Game.bird.move()
            for pipe in Game.pipes:
                pipe.move() # move pipes to left

            # add new pipe when first pipe is about to center of screen
            if len(Game.pipes) > 0 and Game.pipes[-1].upperPart['x'] < Game.width / 2:
                Game.pipes.append(Pipe())

            # remove first pipe if its out of the screen
            if len(Game.pipes) > 0 and Game.pipes[0].upperPart['x'] < -Game.pipes[0].images[0].get_width():
                Game.pipes.pop(0)
             
            # draw sprites
            Game.screen.blit(Game.images['background'], (0,0))
            Game.bird.show()
            for pipe in Game.pipes:
                pipe.show()

            Game.screen.blit(Game.images['base'], (basex, Game.BASEY))
            Game.showScore(score) # print score so player overlaps the score
            pygame.display.update()

            # check for crash here
            crashTest = Game.bird.checkCrash()
            if crashTest[0]:
                return {
                    'y': Game.bird.y,
                    'groundCrash': crashTest[1],
                    'basex': basex,
                    'score': score,
                    'playerVelY': Game.bird.VelY,
                    'playerRot': Game.bird.Rot
                }

            Game.clock.tick(Game.FPS)

    @staticmethod
    def showGameOverscreen(crashInfo):
        """crashes the player down ans shows gameover image"""
        score = crashInfo['score']
        playerx = Game.width * 0.2
        playery = crashInfo['y']
        playerHeight = Game.bird.images[0].get_height()
        playerVelY = crashInfo['playerVelY']
        playerAccY = 2
        playerRot = crashInfo['playerRot']
        playerVelRot = 7

        basex = crashInfo['basex']

        # play hit and die sounds
        Game.sounds['hit'].play()
        if not crashInfo['groundCrash']:
            Game.sounds['die'].play()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    if playery + playerHeight >= Game.BASEY - 1:
                        return

            # player y shift
            if playery + playerHeight < Game.BASEY - 1:
                playery += min(playerVelY, Game.BASEY - playery - playerHeight)

            # player velocity change
            if playerVelY < 15:
                playerVelY += playerAccY

            # rotate only when it's a pipe crash
            if not crashInfo['groundCrash']:
                if playerRot > -90:
                    playerRot -= playerVelRot

            # draw sprites
            Game.screen.blit(Game.images['background'], (0,0))
            for pipe in Game.pipes:
                pipe.show()

            Game.screen.blit(Game.images['base'], (basex, Game.BASEY))
            Game.showScore(score)

            playerSurface = pygame.transform.rotate(Game.bird.images[1], playerRot)
            Game.screen.blit(playerSurface, (playerx,playery))
            Game.screen.blit(Game.images['gameover'], (50, 180))
            pygame.display.update()
            
            Game.clock.tick(Game.FPS)

    @staticmethod
    def showScore(score):
        """displays score in center of screen"""
        scoreDigits = [int(x) for x in list(str(score))]
        totalWidth = 0 # total width of all numbers to be printed

        for digit in scoreDigits:
            totalWidth += Game.images['numbers'][digit].get_width()

        Xoffset = (Game.width - totalWidth) / 2

        for digit in scoreDigits:
            Game.screen.blit(Game.images['numbers'][digit], (Xoffset, Game.height * 0.1))
            Xoffset += Game.images['numbers'][digit].get_width()


if __name__ == '__main__':
    Game.newGame()
