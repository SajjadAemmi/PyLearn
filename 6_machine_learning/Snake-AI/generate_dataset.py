import argparse
import random
from tqdm import tqdm
from src.snake import Snake
from src.apple import Apple
import config


def add_data():
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
        
    direction = snake.direction

    if snake.direction != snake.pre_direction or random.random() < 0.05:
        f.write(','.join([str(w0), str(w1), str(w2), str(w3),
                        str(a0), str(a01), str(a1), str(a12), str(a2), str(a23), str(a3), str(a30), 
                        str(b0), str(b01), str(b1), str(b12), str(b2), str(b23), str(b3), str(b30),
                        str(direction)]) + '\n')
        return True

    else:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Snake AI')
    parser.add_argument("--count", default=1000000, help="count of generated rows you want", type=int)
    parser.add_argument("--dataset", default="./snake_train_dataset.csv", help="dataset path", type=str)
    args = parser.parse_args()

    f = open(args.dataset, 'w')
    f.write('w0,w1,w2,w3,a0,a01,a1,a12,a2,a23,a3,a30,b0,b01,b1,b12,b2,b23,b3,b30,direction' + '\n')
 
    rows = 0
    pbar = tqdm(total=100, position=0, leave=True)

    snake = Snake(config)
    apple = Apple(config)

    while rows < args.count:
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

        if snake.collision_with_wall(snake.direction):
            direction = (snake.direction + 1) % 4
            if snake.collision_with_wall(direction):
                direction = (snake.direction - 1) % 4
                if snake.collision_with_wall(direction):
                    snake = Snake(config)

            snake.direction = direction

        if add_data():
            rows += 1
            pbar.update((1/args.count)*100)

        snake.move()

    f.close()
