import pygame
import random


class Apple:
    def __init__(self, display):
        self.x_pos = 0
        self.y_pos = 0
        self.display = display
        self.radius = 10
        self.color = (100, 0, 0)

    def randomize(self):
        self.x_pos = random.randint(0, Game.width)
        self.y_pos = random.randint(0, Game.height)

    def draw(self):
        return pygame.draw.circle(
            self.display,
            self.color,
            [self.x_pos, self.y_pos], self.radius
        )


class Snake:
    def __init__(self, display):
        self.x_pos = Game.width / 2
        self.y_pos = Game.height / 2
        self.display = display
        self.body = []
        self.size = 0
        self.speed = 10
        self.color = (0, 200, 0)
        self.head_color = (0, 100, 0)
        self.width = 20
        self.height = 20

    def eat(self):
        self.size += 1

    def draw_body(self):
        for item in self.body:
            pygame.draw.rect(
                self.display,
                self.color,
                [item[0], item[1], self.width, self.height]
            )

    def draw_head(self):
        return pygame.draw.rect(
            self.display,
            self.head_color,
            [self.x_pos, self.y_pos, self.width, self.height]
        )

    def move(self, x_change, y_change):
        self.body.append((self.x_pos, self.y_pos))
        self.x_pos += x_change
        self.y_pos += y_change

        if len(self.body) > self.size:
            del (self.body[0])


class Game:

    width = 800
    height = 600

    def __init__(self):
        self.display = pygame.display.set_mode((Game.width, Game.height))
        pygame.display.set_caption('snake')
        self.color = (255, 255, 255)

    def play(self):

        clock = pygame.time.Clock()
        snake = Snake(self.display)
        apple = Apple(self.display)
        apple.randomize()

        x_change = 0
        y_change = 0

        self.score = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -10
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = 10
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        x_change = 0
                        y_change = -10
                    elif event.key == pygame.K_DOWN:
                        x_change = 0
                        y_change = 10

                print(event)

            self.display.fill(self.color)
            pygame.draw.rect(self.display, (0, 200, 0), ((0, 0), (self.width, self.height)), 10)

            snake.move(x_change, y_change)

            apple_rect = apple.draw()
            snake_rect = snake.draw_head()
            snake.draw_body()

            if snake.x_pos < 0 or snake.y_pos < 0 or snake.x_pos > Game.width or snake.y_pos > Game.height:
                self.play()

            # Detect collision with apple
            if apple_rect.colliderect(snake_rect):
                apple.randomize()
                self.score += 1
                snake.eat()

            # Collide with Self
            if len(snake.body) >= 1:
                for cell in snake.body:
                    if snake.x_pos == cell[0] and snake.y_pos == cell[1]:
                        self.play()

            pygame.font.init()
            font = pygame.font.SysFont("calibri", 20)
            score_text = 'Score: {}'.format(self.score)
            score = font.render(score_text, True, (255, 255, 255))
            score_rect = score.get_rect(center=(Game.width / 2, Game.height - 10))
            self.display.blit(score, score_rect)

            pygame.display.update()
            clock.tick(30)  # fps


game = Game()
game.play()
