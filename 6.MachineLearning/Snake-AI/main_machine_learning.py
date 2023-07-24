import argparse

import pygame
import numpy as np
import torch

from src.snake import Snake
from src.apple import Apple
from src.model import Model
from src.color import Color
import config


def get_data():
    w0 = snake.y - config.wall_offset  # up
    w1 = config.game_width - config.wall_offset - snake.x  # right
    w2 = config.game_height - config.wall_offset - snake.y  # down
    w3 = snake.x - config.wall_offset  # left

    if snake.x == apple.x and snake.y > apple.y:
        a0 = abs(snake.x - apple.x) + abs(snake.y - apple.y)
    else:
        a0 = 0

    if abs(snake.x - apple.x) == abs(snake.y - apple.y) and snake.x < apple.x and snake.y > apple.y:
        a01 = abs(snake.x - apple.x) + abs(snake.y - apple.y)
    else:
        a01 = 0

    if snake.x < apple.x and snake.y == apple.y:
        a1 = abs(snake.x - apple.x) + abs(snake.y - apple.y)
    else:
        a1 = 0

    if abs(snake.x - apple.x) == abs(snake.y - apple.y) and snake.x < apple.x and snake.y < apple.y:
        a12 = abs(snake.x - apple.x) + abs(snake.y - apple.y)
    else:
        a12 = 0

    if snake.x == apple.x and snake.y < apple.y:
        a2 = abs(snake.x - apple.x) + abs(snake.y - apple.y)
    else:
        a2 = 0

    if abs(snake.x - apple.x) == abs(snake.y - apple.y) and snake.x > apple.x and snake.y < apple.y:
        a23 = abs(snake.x - apple.x) + abs(snake.y - apple.y)
    else:
        a23 = 0

    if snake.x > apple.x and snake.y == apple.y:
        a3 = abs(snake.x - apple.x) + abs(snake.y - apple.y)
    else:
        a3 = 0

    if abs(snake.x - apple.x) == abs(snake.y - apple.y) and snake.x > apple.x and snake.y > apple.y:
        a30 = abs(snake.x - apple.x) + abs(snake.y - apple.y)
    else:
        a30 = 0

    for part in snake.body:
        if snake.x == part[0] and snake.y > part[1]:
            b0 = abs(snake.x - part[0]) + abs(snake.y - part[1])
            break
    else:
        b0 = 0

    for part in snake.body:
        if snake.x < part[0] and snake.y > part[1]:
            b01 = abs(snake.x - part[0]) + abs(snake.y - part[1])
            break
    else:
        b01 = 0

    for part in snake.body:
        if snake.x < part[0] and snake.y == part[1]:
            b1 = abs(snake.x - part[0]) + abs(snake.y - part[1])
            break
    else:
        b1 = 0

    for part in snake.body:
        if snake.x < part[0] and snake.y < part[1]:
            b12 = abs(snake.x - part[0]) + abs(snake.y - part[1])
            break
    else:
        b12 = 0

    for part in snake.body:
        if snake.x == part[0] and snake.y < part[1]:
            b2 = abs(snake.x - part[0]) + abs(snake.y - part[1])
            break
    else:
        b2 = 0

    for part in snake.body:
        if snake.x > part[0] and snake.y < part[1]:
            b23 = abs(snake.x - part[0]) + abs(snake.y - part[1])
            break
    else:
        b23 = 0

    for part in snake.body:
        if snake.x > part[0] and snake.y == part[1]:
            b3 = abs(snake.x - part[0]) + abs(snake.y - part[1])
            break
    else:
        b3 = 0

    for part in snake.body:
        if snake.x > part[0] and snake.y > part[1]:
            b30 = abs(snake.x - part[0]) + abs(snake.y - part[1])
            break
    else:
        b30 = 0

    return np.array([w0, w1, w2, w3,
                    a0, a01, a1, a12, a2, a23, a3, a30,
                    b0, b01, b1, b12, b2, b23, b3, b30,
                    ], dtype=np.float32)


class Game:
    def __init__(self):        
        self.display = pygame.display.set_mode((config.game_width, config.game_height))
        self.ground_color = Color.khaki
        self.wall_color = Color.dark_khaki
        self.font = pygame.font.SysFont("calibri", 20)

    def play(self):
        global snake, apple

        snake = Snake(config)
        apple = Apple(config)
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            # Detect collision with apple
            if snake.x == apple.x and snake.y == apple.y:
                snake.eat()
                apple = Apple(config)

            snake.x_change_old, snake.y_change_old = snake.x, snake.y

            with torch.no_grad():
                data = get_data()
                data = data.reshape(1, 20)
                data = torch.tensor(data)
                result = model(data)
                snake.direction = np.argmax(result)

            snake.move()
     
            self.display.fill(self.ground_color)
            pygame.draw.rect(self.display, self.wall_color, ((0, 0), (config.game_width, config.game_height)), config.wall_offset)

            apple.draw(self.display)
            snake.draw(self.display)

            if snake.x < 0 or snake.y < 0 or snake.x > config.game_width or snake.y > config.game_height:
                self.play()

            score = self.font.render(f'Score: {snake.score}', True, Color.black)
            score_rect = score.get_rect(center=(config.game_width / 2, config.game_height - 10))
            self.display.blit(score, score_rect)

            pygame.display.update()
            clock.tick(config.fps)  # fps


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Snake AI')
    parser.add_argument("--weights", default="./weights/snake.pt", help="weights path", type=str)
    args = parser.parse_args()

    model = Model()
    model.load_state_dict(torch.load(args.weights, map_location=torch.device('cpu')))

    pygame.display.set_caption('snake')
    pygame.font.init()
    game = Game()
    game.play()
