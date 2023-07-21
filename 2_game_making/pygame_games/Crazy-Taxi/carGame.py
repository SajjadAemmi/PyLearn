import pygame
import random
import time

pygame.init()

class Color:
    black = (0, 0, 0)
    gray = (127, 127, 127)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)


class Enemy:

    speed = 5

    def __init__(self):

        self.image = pygame.image.load('car.png')
        self.x = random.randint(0, W - 64)
        self.y = -64
        self.area = display.blit(self.image, [self.x, self.y])

    def show(self):
        self.area = display.blit(self.image, [self.x, self.y])

    def move(self):
        self.y += self.speed


class Car:
    def __init__(self, x, y):
        self.speed = 2
        self.image = pygame.image.load('mycar.png')
        self.x = x
        self.y = y
        self.area = display.blit(self.image, [self.x, self.y])
        self.x_direction = -1

    def show(self):
        self.area = display.blit(self.image, [self.x, self.y])

    def move(self):
        self.x += self.speed * self.x_direction

        if self.x < 0:
            self.x = 0

        if self.x > W - 64:
            self.x = W - 64

W = 200
H = 500

display = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri", 30)

car = Car(W // 2 - 32, H - 100)
enemy = Enemy()

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car.x_direction = -1

            if event.key == pygame.K_RIGHT:
                car.x_direction = 1

    car.move()
    enemy.move()

    if enemy.y > H:
        enemy = Enemy()

        # زیاد شو ولی از ۱۰۰ بیشتر نشو
        if Enemy.speed < 100:
            Enemy.speed += 1

    display.fill(Color.black)

    car.show()
    enemy.show()

    if car.area.colliderect(enemy.area):

        message = font.render('Game Over', True, Color.red)
        display.blit(message, [30, H // 2])
        pygame.display.update()

        time.sleep(4)
        break


    pygame.display.update()
    clock.tick(30)
