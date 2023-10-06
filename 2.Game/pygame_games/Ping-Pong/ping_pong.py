import pygame
from sys import exit

pygame.init()


class Color:
    red = (255, 0, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    white = (255, 255, 255)
    orange = (255, 127, 0)


class Rocket:
    def __init__(self, color, x, y):
        self.width = 10
        self.height = 50
        self.color = color
        self.x = x
        self.y = y
        self.y_change = 0
        self.speed = 10
        self.score = 0
        self.area = pygame.draw.rect(Game.screen, self.color, [self.x, self.y, self.width, self.height])

    def draw(self):
        self.area = pygame.draw.rect(Game.screen, self.color, [self.x, self.y, self.width, self.height])

    def move(self):
        self.y += self.y_change * self.speed

        if self.y > Game.height - self.height - 10:
            self.y = Game.height - self.height - 10
        elif self.y < 10:
            self.y = 10


class Ball:
    def __init__(self):
        self.width = 15
        self.height = 15
        self.radius = 8
        self.x, self.y = Game.width // 2, Game.height // 2
        self.speed = 10
        self.x_change = 1
        self.y_change = 1
        self.area = pygame.draw.circle(Game.screen, Color.orange, [self.x, self.y], self.radius)

    def draw(self):
        self.area = pygame.draw.circle(Game.screen, Color.orange, [self.x, self.y], self.radius)

    def move(self):
        self.x += self.x_change * self.speed
        self.y += self.y_change * self.speed

        if self.y < 10:
            self.y_change *= -1
            self.y = 10

        elif self.y >= Game.height - 10:
            self.y_change *= -1
            self.y = Game.height - self.height - 10

    def reset(self):
        self.x, self.y = Game.width // 2, Game.height // 2


class Game:
    width = 700
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong Pong!")
    font = pygame.font.SysFont("calibri", 40)

    @staticmethod
    def play():
        i = Rocket(Color.red, 10., Game.height / 2)
        cpu = Rocket(Color.blue, Game.width - 20, Game.height / 2)
        ball = Ball()
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEMOTION:
                    i.y = pygame.mouse.get_pos()[1]

            Game.screen.fill(Color.black)

            pygame.draw.rect(Game.screen, Color.white, ((0, 0), (Game.width, Game.height)), 10)
            pygame.draw.aaline(Game.screen, Color.white, (Game.width / 2, 5), (Game.width / 2, Game.height))

            score1 = Game.font.render(str(i.score), True, Color.white)
            score2 = Game.font.render(str(cpu.score), True, Color.white)

            Game.screen.blit(score1, (Game.width / 2 - 100, Game.height / 2))
            Game.screen.blit(score2, (Game.width / 2 + 100, Game.height / 2))

            i.draw()
            cpu.draw()
            ball.draw()

            i.move()
            cpu.move()
            ball.move()

            # Ai
            if ball.x >= Game.width / 2:
                if cpu.y < ball.y + ball.radius:
                    cpu.y_change = 1
                if cpu.y > ball.y - ball.radius:
                    cpu.y_change = -1

            if i.area.colliderect(ball.area):
                ball.x = 30
                ball.x_change *= -1

            if cpu.area.colliderect(ball.area):
                ball.x = cpu.x - ball.width
                ball.x_change *= -1

            if ball.x < 5:
                cpu.score += 1
                ball.reset()

            elif ball.x > Game.width - 5:
                i.score += 1
                ball.reset()

            pygame.display.update()
            clock.tick(30)


Game.play()
