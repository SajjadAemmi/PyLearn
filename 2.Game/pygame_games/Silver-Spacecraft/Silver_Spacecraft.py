import pygame
import time
import random

pygame.init()

#colors
color = (0,0,0)
darkgray = (20,20,20)
white = (255,255,255)
red = (255,0,0)


class Enemy:
    def __init__(self):
        self.width = 48
        self.height = 48
        self.image = pygame.image.load('enemy.png')
        self.x_pos = random.randint(0, Game.width)
        self.y_pos = -300
        self.speed = 2
        self.area = Game.display.blit(self.image, (self.x_pos, self.y_pos))

    def draw(self):
        self.area = Game.display.blit(self.image, (self.x_pos, self.y_pos))

    def move(self):
        self.y_pos += self.speed


class Fire:
    def __init__(self, spacecraft):
        self.width = 16
        self.height = 16
        self.image = pygame.image.load('fire.png')
        self.x_pos = spacecraft.x_pos + spacecraft.width / 2
        self.y_pos = spacecraft.y_pos - 20
        self.area = Game.display.blit(self.image, (self.x_pos, self.y_pos))
        self.speed = 10

    def draw(self):
        self.area = Game.display.blit(self.image, (self.x_pos, self.y_pos))

    def move(self):
        self.y_pos -= self.speed


class Spacecraft:
    def __init__(self):
        self.width = 48
        self.height = 48
        self.image = pygame.image.load('spacecraft.png')
        self.x_pos = Game.width / 2
        self.y_pos = Game.height - 100
        self.area = Game.display.blit(self.image, (self.x_pos, self.y_pos))
        self.speed = 6

    def draw(self):
        self.area = Game.display.blit(self.image, (self.x_pos, self.y_pos))

    def move(self, x_change):
        self.x_pos += x_change


class Game:

    width = 800
    height = 600
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Silver Spacecraft')
    background = pygame.image.load('space.png')
    point_sound = pygame.mixer.Sound("sfx_point.wav")
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.set_volume(0.2)

    @staticmethod
    def play():

        pygame.mixer.music.play()
        spacecraft = Spacecraft()
        enemy = Enemy()
        clock = pygame.time.Clock()
        fire = None

        x_change = 0
        score = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -1
                    elif event.key == pygame.K_RIGHT:
                        x_change = +1
                    elif event.key == pygame.K_SPACE:
                        fire = Fire(spacecraft)

                # print(event)

            spacecraft.move(x_change)
            enemy.move()

            Game.display.fill(darkgray)
            Game.display.blit(Game.background, (0, 0))
            spacecraft.draw()
            enemy.draw()

            if fire != None:
                fire.draw()

            if fire != None:
                fire.move()

            if fire != None and fire.y_pos < 0:
                fire = None

            if spacecraft.x_pos > Game.width - spacecraft.width or spacecraft.x_pos < 0:
                Game.message_display('Game Over')
                Game.play()

            if enemy.y_pos > Game.height:
                enemy = Enemy()
                score += 1

            if fire != None and fire.area.colliderect(enemy.area):
                Game.point_sound.play()
                enemy = Enemy()

            if spacecraft.area.colliderect(enemy.area):
                Game.message_display('Game Over')
                Game.play()

            Game.score_display(score)
            pygame.display.update()
            clock.tick(120)

    @staticmethod
    def text_object(text, font):
        text_surf = font.render(text, True, red)
        return text_surf, text_surf.get_rect()

    @staticmethod
    def message_display(text):
        text_font = pygame.font.Font('freesansbold.ttf', 100)
        text_surf, text_rect = Game.text_object(text, text_font)
        text_rect.center = ((Game.width / 2), (Game.height / 2))
        Game.display.blit(text_surf, text_rect)
        pygame.display.update()
        time.sleep(2)

    @staticmethod
    def score_display(score):
        font = pygame.font.SysFont(None, 25)
        text_surf = font.render("score: " + str(score), True, white)
        Game.display.blit(text_surf, (0,0))


if __name__ == '__main__':
    Game.play()
