import pygame
from src.snake import Snake
from src.apple import Apple
from src.color import Color
import config


class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((config.game_width, config.game_height))
        self.ground_color = Color.khaki
        self.wall_color = Color.dark_khaki
        self.font = pygame.font.SysFont("calibri", 20)

    def play(self):
        global rows

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

            # collision with body
            for part in snake.body:
                if snake.x == part[0] and snake.y == part[1]:
                    snake = Snake(config)

            direction = snake.vision(apple)
            snake.pre_direction = snake.direction
            snake.decision(direction)

            # collision with wall
            if snake.collision_with_wall(snake.direction):
                direction = (snake.direction + 1) % 4
                if snake.collision_with_wall(direction):
                    direction = (snake.direction - 1) % 4
                    if snake.collision_with_wall(direction):
                        snake = Snake(config)

                snake.direction = direction

            snake.move()

            self.display.fill(self.ground_color)
            pygame.draw.rect(self.display, self.wall_color, ((0, 0), (config.game_width, config.game_height)), config.wall_offset)

            apple.draw(self.display)
            snake.draw(self.display)

            score_text = self.font.render(f'Score: {snake.score}', True, Color.black)
            score_rect = score_text.get_rect(center=(config.game_width / 2, config.game_height - 10))
            self.display.blit(score_text, score_rect)

            pygame.display.update()
            clock.tick(config.fps)


if __name__ == "__main__":
    pygame.display.set_caption('snake')
    pygame.font.init()
    game = Game()
    game.play()
