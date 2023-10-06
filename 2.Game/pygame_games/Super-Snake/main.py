import pygame

from snake import Snake
from apple import Apple
from diamond import Diamond
from stones import Stones
from functions import *
from config import *


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SUPER SNAKE')
clock = pygame.time.Clock()

pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.set_volume(0.2)


def show_controls():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.font.quit()
                quit()

        gameDisplay.blit(CONTROLS, (0, 0))

        draw_text("GREETINGS", czarny, 38, display_width / 2, display_height / 2 - 220)
        draw_text("Use arrows to navigate your little friend on the bord.", czarny, 28, display_width / 2,
                  display_height / 2 - 150)
        draw_text("Collect apples    , to increase your score and grow.", czarny, 28, display_width / 2,
                  display_height / 2 - 100)
        draw_text("Be careful not to hit walls and sudenlly appearing", czarny, 28, display_width / 2,
                  display_height / 2 - 50)
        draw_text("rocks     and most importantly don't bite yourself!", czarny, 28, display_width / 2,
                  display_height / 2 - 0)
        draw_text("Use diamonds to unlock special powers.", czarny, 28, display_width / 2, display_height / 2 + 50)

        gameDisplay.blit(APPLE_BIG, (278, display_height / 2 - 110))
        gameDisplay.blit(STONE, (173, display_height / 2 - 0))

        button("MENU", 50, 500, 200, 70, czerwony, LIGHT_RED, action='menu')
        button("NEXT", 350, 500, 200, 70, czerwony, LIGHT_RED, action='next')
        button("QUIT", 650, 500, 200, 70, czerwony, LIGHT_RED, action='quit')

        pygame.display.update()

        clock.tick(15)


def show_controls_next():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.font.quit()
                quit()

        gameDisplay.blit(CONTROLS, (0, 0))

        draw_text("     will allow you to go through the walls", czarny, 28, display_width / 2,
                  display_height / 2 - 220)
        draw_text("and crash those sneaky stones.", czarny, 28, display_width / 2, display_height / 2 - 170)
        draw_text("This effect will remain for 10 seconds.", czarny, 28, display_width / 2, display_height / 2 - 120)
        draw_text("     will make snake shorter and easier to maneuver.", czarny, 28, display_width / 2,
                  display_height / 2 - 70)
        draw_text("Whenever you want,", czarny, 28, display_width / 2, display_height / 2 - 20)
        draw_text("you can press P to pause the game.", czarny, 28, display_width / 2, display_height / 2 + 30)
        draw_text("GOOD LUCK!", czarny, 35, display_width / 2, display_height / 2 + 100)

        gameDisplay.blit(BLACK_DIAMOND_BIG, (150, display_height / 2 - 225))
        gameDisplay.blit(WHITE_DIAMOND_BIG, (75, display_height / 2 - 75))

        button("MENU", 50, 500, 200, 70, czerwony, LIGHT_RED, action='menu')
        button("PREVIOUS", 350, 500, 200, 70, czerwony, LIGHT_RED, action='previous')
        button("QUIT", 650, 500, 200, 70, czerwony, LIGHT_RED, action='quit')

        pygame.display.update()

        clock.tick(15)


def show_game_intro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.font.quit()
                quit()

        gameDisplay.blit(START, (0, 0))

        button("PLAY", 350, 250, 200, 70, czerwony, LIGHT_RED, action='play')
        button("CONTROLS", 350, 350, 200, 70, czerwony, LIGHT_RED, action='controls')
        button("QUIT", 350, 450, 200, 70, czerwony, LIGHT_RED, action='quit')

        pygame.display.update()

        clock.tick(15)


def button(text, x, y, width, height, inactive, active, text_color=czarny, action=None):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (x + width > cursor[0] > x and y + height > cursor[1] > y):
        gameDisplay.blit(ACTIVE_B, (x, y))

        if click[0] == 1 and action != None:
            if action == 'play' or action == 'again':
                gameLoop()
            elif action == 'controls' or action == 'previous':
                show_controls()
            elif action == 'quit':
                pygame.quit()
                pygame.font.quit()
                quit()
            elif action == 'menu':
                show_game_intro()
            elif action == 'next':
                show_controls_next()
    else:
        gameDisplay.blit(INACTIVE_B, (x, y))

    draw_text(gameDisplay, text, text_color, int(round(height / 2)), x + width / 2, y + height / 4)


def gameLoop():
    gameExit = False
    gameOver = False

    points = 0
    speed = FPS

    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = block_size
    lead_y_change = 0

    snake = Snake(lead_x, lead_y)
    stones = Stones()
    apple = Apple(stones, snake)
    diamond = Diamond()
    trimer = Diamond()

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) and snake.direction != "right":
                    snake.direction = "left"
                elif (event.key == pygame.K_RIGHT) and snake.direction != "left":
                    snake.direction = "right"
                elif (event.key == pygame.K_UP) and snake.direction != "down":
                    snake.direction = "up"
                elif (event.key == pygame.K_DOWN) and snake.direction != "up":
                    snake.direction = "down"

                if event.key == pygame.K_p:
                    pause()

        if snake.direction == "left":
            lead_x_change = -block_size
            lead_y_change = 0
        elif snake.direction == "right":
            lead_x_change = block_size
            lead_y_change = 0
        elif snake.direction == "up":
            lead_y_change = -block_size
            lead_x_change = 0
        elif snake.direction == "down":
            lead_y_change = block_size
            lead_x_change = 0

        lead_x += lead_x_change
        lead_y += lead_y_change

        if lead_x == apple.x and lead_y == apple.y:
            apple = Apple(stones, snake)
            snake.length += 1
            points += 10
            POINT.play()

            if (points) % 40 == 0:
                stones.add(snake)

            if (points) % 70 == 0:
                speed += 1
                print(speed)

            if (points) % 150 == 0:
                diamond.renew(stones, snake, speed)

            if (points) % 280 == 0:
                trimer.renew(Stones, snake, speed)

        if lead_x == diamond.x and lead_y == diamond.y:
            points += 50
            diamond.kill()
            snake.superSnake(speed)
            EVOLUTION.play()

            if points % 280 == 0:
                trimer.renew(stones, snake, speed)

        if lead_x == trimer.x and lead_y == trimer.y:
            points += 50
            trimer.kill()
            snake.trim()

            if points % 150 == 0:
                diamond.renew(stones, snake, speed)

        if snake.superTimer > 0:
            if 15 <= snake.superTimer:
                pygame.mixer.music.set_volume(0.05)
            if 15 > snake.superTimer >= 10:
                pygame.mixer.music.set_volume(0.10)
            elif 10 > snake.superTimer >= 5:
                pygame.mixer.music.set_volume(0.15)
            elif 5 > snake.superTimer:
                pygame.mixer.music.set_volume(0.2)
            for stone in Stones.list:
                if stone[0] == snake.head[1] and stone[1] == snake.head[2]:
                    points += 20
                    Stones.destroy(stone)
                    STONEDESTROY.play()

            if lead_x >= display_width - block_size:
                lead_x = block_size
            elif lead_x < block_size:
                lead_x = display_width - 2 * block_size
            elif lead_y >= display_height - block_size:
                lead_y = block_size
            elif lead_y < block_size:
                lead_y = display_height - 2 * block_size

        snake.update(lead_x, lead_y)
        gameOver = snake.isDead(stones)

        gameDisplay.blit(background, (0, 0))
        apple.show(gameDisplay)
        stones.show(gameDisplay)
        diamond.show(gameDisplay, 'black')
        trimer.show(gameDisplay, 'white')
        snake.show(gameDisplay, FPS)
        gameDisplay.blit(wall, (0, 0))
        score(gameDisplay, points)

        pygame.display.update()
        clock.tick(speed)

        while gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

            gameDisplay.blit(GAMEOVER, (0, 0))
            draw_text(gameDisplay, "SCORE: " + str(points), czarny, 50, display_width / 2, display_height / 2 - 25)

            button("MENU", 100, 450, 200, 70, czerwony, LIGHT_RED, action='menu')
            button("PLAY AGAIN", 350, 450, 200, 70, czerwony, LIGHT_RED, action='again')
            button("QUIT", 600, 450, 200, 70, czerwony, LIGHT_RED, action='quit')

            pygame.display.update()
            clock.tick(15)

    pygame.quit()
    pygame.font.quit()
    quit()


pygame.mixer.music.play(loops=-1)
show_game_intro()
