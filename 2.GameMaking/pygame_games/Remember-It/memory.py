import pygame
import random
import time

pygame.init()

class Color:
    red = (150, 40, 40)
    blue = (20, 20, 200)
    green = (80, 180, 80)
    orange = (255, 127, 0)
    white = (255, 255, 255)
    light = (180,180,180)


class Gerdali:
    def __init__(self):
        self.r = 20
        self.x = random.randint(0, Game.w)
        self.y = random.randint(0, Game.h)
        self.color = random.choice([Color.red, Color.blue, Color.green, Color.orange])
        # self.image = pygame.image.load('2.png')
        self.image = str(random.randint(1, 5)) + '.png'
        self.loaded_image = pygame.image.load(self.image)
        self.area = pygame.draw.circle(Game.display, self.color, [self.x, self.y], self.r)

    def change_position(self):
        self.x = random.randint(0, Game.w)
        self.y = random.randint(0, Game.h)

    def show(self):
        self.area = pygame.draw.circle(Game.display, self.color, [self.x, self.y], self.r)
        Game.display.blit(self.loaded_image, [self.x - 16, self.y - 16])


class Game:

    w = 300
    h = 600
    display = pygame.display.set_mode((w, h))
    bg_color = Color.light
    font = pygame.font.SysFont("Arial", 20)

    @staticmethod
    def play():

        end_game = False
        clock = pygame.time.Clock()
        mylist = []
        last_gerdali = Gerdali()
        mylist.append(last_gerdali)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: #if user clicked

                    if end_game == True:
                        Game.play()

                    for item in mylist:
                        if item.area.collidepoint(event.pos): #if user clicked on a gerdali

                            if item == last_gerdali:
                                # change position of other gerdalies
                                for g in mylist:
                                    g.change_position()

                                # create new gerdali
                                while True:
                                    last_gerdali = Gerdali()
                                    if all((last_gerdali.image != item.image or last_gerdali.color != item.color) for item in mylist):
                                        mylist.append(last_gerdali)
                                        break
                            else:
                                message = Game.font.render("Game Over", True, Color.red)
                                Game.display.blit(message, (Game.w / 2, Game.h / 2))
                                end_game = True

            if end_game == False:
                Game.display.fill(Game.bg_color)
                for item in mylist:
                    item.show()

            pygame.display.update()
            clock.tick(24)

Game.play()
