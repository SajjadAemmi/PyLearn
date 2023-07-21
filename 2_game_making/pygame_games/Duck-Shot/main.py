import pygame
import random
import time
import sys
import os

pygame.init()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Duck:
    def __init__(self):
        self.direction = random.choice(['l', 'r'])
        if self.direction == 'r':
            self.x = -50
        elif self.direction == 'l':
            self.x = game.w + 50

        self.y = random.randint(0, game.h // 2)

        self.image = pygame.image.load(
            resource_path(
                random.choices(
                    population=['images/duck.png', 'images/stork.png', 'images/twitter.png'],
                    weights=[0.49, 0.49, 0.02],
                    k=1
                )[0]
            )
        )

        self.speed = 8
        self.area = game.display.blit(self.image, [self.x, self.y])

    def show(self):
        if self.direction == 'r':
            self.area = game.display.blit(self.image, [self.x, self.y])
        elif self.direction == 'l':
            self.area = game.display.blit(pygame.transform.flip(self.image, True, False), [self.x, self.y])

    def fly(self):
        if self.direction == 'r':
            self.x += self.speed
        elif self.direction == 'l':
            self.x -= self.speed


class Gun:
    def __init__(self):
        self.x = game.w // 2
        self.y = game.h // 2
        self.image = pygame.image.load(resource_path('images/shooter.png'))
        self.area = game.display.blit(self.image, [self.x, self.y])
        self.score = 0
        self.sound = pygame.mixer.Sound(resource_path("shotgun.wav"))
        pygame.mixer.music.set_volume(0.2)

    def show(self):
        self.area = game.display.blit(self.image, [self.x, self.y])

    def fire(self, ducks):
        self.sound.play()
        for duck in ducks:
            if self.area.colliderect(duck.area):
                ducks.remove(duck)
                self.score += 1


class Game:
    def __init__(self):
        self.w = 852
        self.h = 480
        self.background = pygame.image.load(resource_path('images/background.jpg'))
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Duck Hunt')
        pygame.display.set_icon(pygame.image.load(resource_path('images/shooter.png')))
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.font = pygame.font.SysFont('Arial', 20)

    def play(self):

        gun = Gun()
        ducks = []
        pygame.mouse.set_visible(False)
        counter = 0
        r = random.randint(10, 30)

        while True:
            counter += 1

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEMOTION:
                    gun.x = pygame.mouse.get_pos()[0]
                    gun.y = pygame.mouse.get_pos()[1]

                if event.type == pygame.MOUSEBUTTONDOWN:
                    gun.fire(ducks)

            if counter == r:
                new_duck = Duck()
                ducks.append(new_duck)
                counter = 0
                r = random.randint(10, 30)

            for duck in ducks:
                duck.fly()

            # show
            self.display.blit(self.background, [0, 0])
            gun.show()
            for duck in ducks:
                duck.show()

            game.display.blit(self.font.render("Score: " + str(gun.score), True, (0, 0, 0)), [10, 10])

            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.play()
