import pygame
import random
import time


class Color:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (246, 83, 20)
    dark_red = (127, 0, 0)
    blue = (0, 161, 241)
    dark_blue = (0, 0, 127)
    green = (124, 187, 0)
    dark_green = (0, 127, 0)
    yellow = (255, 187, 0)
    dark_yellow = (127, 127, 0)


class Button:
    def __init__(self, normal_color, press_color, x, y):

        self.radius = 90
        self.normal_color = normal_color
        self.press_color = press_color
        self.color = normal_color
        self.x = x
        self.y = y

    def draw(self):
        self.area = pygame.draw.circle(Game.screen, self.color, [self.x, self.y], self.radius)

    def press(self):
        self.color = self.press_color

    def release(self):
        self.color = self.normal_color


class Game:
    width = 400
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Memory Tiles")
    error_img = pygame.image.load('error.png')
    tick_img = pygame.image.load('tick.png')
    pattern = []
    mode = 'show'

    @staticmethod
    def draw(buttons):
        Game.screen.fill(Color.white)

        for button in buttons:
            button.draw()

    @staticmethod
    def play():

        b1 = Button(Color.red, Color.dark_red, 100, 100)
        b2 = Button(Color.blue, Color.dark_blue, 100, 300)
        b3 = Button(Color.green, Color.dark_green, 300, 100)
        b4 = Button(Color.yellow, Color.dark_yellow, 300, 300)

        buttons = [b1, b2, b3, b4]
        Game.mode = 'show'
        clock = pygame.time.Clock()
        index = 0
        Game.pattern = []

        while True:

            if Game.mode == 'show':
                Game.pattern.append(random.choice(buttons))

                for button in Game.pattern:
                    button.press()
                    Game.draw(buttons)
                    pygame.display.update()
                    time.sleep(0.5)
                    button.release()
                    Game.draw(buttons)
                    pygame.display.update()
                    time.sleep(0.5)

                index = 0
                Game.mode = 'guess'

            if Game.mode == 'guess':

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # 1 is the left mouse button, 2 is middle, 3 is right.
                        if event.button == 1:
                            for button in buttons:
                                if button.area.collidepoint(event.pos):
                                    button.press()
                                    Game.draw(buttons)
                                    pygame.display.update()
                                    time.sleep(0.5)
                                    button.release()
                                    Game.draw(buttons)
                                    pygame.display.update()
                                    time.sleep(0.5)

                                    if Game.pattern[index] == button:
                                        index += 1
                                    else:
                                        Game.screen.blit(Game.error_img, (Game.width / 2 - 24, Game.height / 2 - 32))
                                        pygame.display.update()
                                        time.sleep(0.5)
                                        Game.play()

                if index == len(Game.pattern):
                    index = 0
                    Game.screen.blit(Game.tick_img, (Game.width / 2 - 24, Game.height / 2 - 32))
                    pygame.display.update()
                    time.sleep(0.5)
                    Game.mode = 'show'
            clock.tick(30)

Game.play()
