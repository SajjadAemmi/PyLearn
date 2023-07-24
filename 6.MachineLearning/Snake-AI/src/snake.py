import random
from math import sqrt
import pygame
from src.color import Color
from config import *


class Snake:
    def __init__(self, config):
        self.x = game_width // 2
        self.y = game_height // 2
        self.body = []
        self.body_color_1 = Color.green
        self.body_color_2 = Color.green_dark
        self.w = 20
        self.h = 20
        self.pre_direction = None
        self.direction = random.randint(0, 3)
        self.x_change = 0
        self.y_change = 0
        self.speed = 20
        self.score = 0
        self.config = config
        self.border_radius = 4

    def eat(self):
        self.score += 1

    def move(self):
        if self.direction == 0:
            self.x_change = 0
            self.y_change = -1

        elif self.direction == 1:
            self.x_change = 1
            self.y_change = 0

        elif self.direction == 2:
            self.x_change = 0
            self.y_change = 1

        elif self.direction == 3:
            self.x_change = -1
            self.y_change = 0

        self.body.insert(0, [self.x, self.y])
        if len(self.body) > self.score:
            self.body.pop()

        self.x += self.x_change * self.speed
        self.y += self.y_change * self.speed

    def draw(self, display):
        pygame.draw.rect(display, self.body_color_1, [self.x, self.y, self.w, self.h], border_radius=self.border_radius)
        for index, item in enumerate(self.body):
            if index % 2 == 0:
                pygame.draw.rect(display, self.body_color_2, [item[0], item[1], self.w, self.h], border_radius=self.border_radius)
            else:
                pygame.draw.rect(display, self.body_color_1, [item[0], item[1], self.w, self.h], border_radius=self.border_radius)

    def collision_with_body(self, direction) -> bool:
        for part in self.body:
            if direction == 0:
                if abs(self.x - part[0]) < self.config.wall_offset and abs(self.y - 8 - part[1]) == 0:
                    return True
                if abs(self.x - part[0]) == 0 and abs(self.y - 20 - part[1]) < self.config.wall_offset:
                    return True

            if direction == 1:
                if abs(self.x + 20 - part[0]) < self.config.wall_offset and abs(self.y - part[1]) == 0:
                    return True
                if abs(self.x + 20 - part[0]) == 0 and abs(self.y - part[1]) < self.config.wall_offset:
                    return True

            if direction == 2:
                if abs(self.x - part[0]) < self.config.wall_offset and abs(self.y + 20 - part[1]) == 0:
                    return True
                if abs(self.x - part[0]) == 0 and abs(self.y + 20 - part[1]) < self.config.wall_offset:
                    return True

            if direction == 3:
                if abs(self.x - 20 - part[0]) < self.config.wall_offset and abs(self.y - part[1]) == 0:
                    return True
                if abs(self.x - 20 - part[0]) == 0 and abs(self.y - part[1]) < self.config.wall_offset:
                    return True

        return False

    def collision_with_wall(self, direction) -> bool:
        if direction == 0:
            if self.y - self.config.wall_offset > 0:
                return False

        elif direction == 1:
            if self.x + self.config.wall_offset * 2 < game_width:
                return False

        elif direction == 2:
            if self.y + self.config.wall_offset * 2 < game_height:
                return False

        elif direction == 3:
            if self.x - self.config.wall_offset > 0:
                return False

        return True

    def distance(self, direction, method, apple):
        if direction == 0:
            x = self.x
            y = self.y - 8

        elif direction == 1:
            x = self.x + 8
            y = self.y

        elif direction == 2:
            x = self.x
            y = self.y + 8

        elif direction == 3:
            x = self.x - 8
            y = self.y

        if method == 'manhattan':
            return abs(x - apple.x) + abs(y - apple.y)
        elif method == 'euclidean':
            return sqrt(abs(x - apple.x) ** 2 + abs(y - apple.y) ** 2)
        elif method == 'chess':
            return max(abs(x - apple.x), abs(y - apple.y))

    def vision(self, apple):
        # up
        if self.x == apple.x and self.y > apple.y:
            for part in self.body:
                if self.x == part[0] and self.y > part[1] > apple.y:
                    break
            else:
                return '0'

        # up right
        if abs(self.x - apple.x) == abs(self.y - apple.y) and self.x < apple.x and self.y > apple.y:
            for part in self.body:
                if abs(self.x - part[0]) == abs(self.y - part[1]) and self.x < part[0] < apple.x and self.y > part[1] > apple.y:
                    break
            else:
                return '01'

        # right
        if self.x < apple.x and self.y == apple.y:
            for part in self.body:
                if self.x < part[0] < apple.x and self.y == part[1]:
                    break
            else:
                return '1'

        # down right
        if abs(self.x - apple.x) == abs(self.y - apple.y) and self.x < apple.x and self.y < apple.y:
            for part in self.body:
                if abs(self.x - part[0]) == abs(self.y - part[1]) and self.x < part[0] < apple.x and self.y < part[1] < apple.y:
                    break
            else:
                return '12'

        # down
        if self.x == apple.x and self.y < apple.y:
            for part in self.body:
                if self.x == part[0] and self.y < part[1] < apple.y:
                    break
            else:
                return '2'

        # down left
        if abs(self.x - apple.x) == abs(self.y - apple.y) and self.x > apple.x and self.y < apple.y:
            for part in self.body:
                if abs(self.x - part[0]) == abs(self.y - part[1]) and self.x > part[0] > apple.x and self.y < part[1] < apple.y:
                    break
            else:
                return '23'

        if self.x > apple.x and self.y == apple.y:
            for part in self.body:
                if self.x > part[0] > apple.x and self.y == part[1]:
                    break
            else:
                return '3'
        
        if abs(self.x - apple.x) == abs(self.y - apple.y) and self.x > apple.x and self.y > apple.y:
            for part in self.body:
                if abs(self.x - part[0]) == abs(self.y - part[1]) and self.x > part[0] > apple.x and self.y > part[1] > apple.y:
                    break
            else:
                return '30'

        return None

    def decision(self, direction):
        # up
        if direction == '0':
            if self.direction != 2:
                self.direction = 0

        # up right
        elif direction == '01':
            if self.direction != 2:
                self.direction = 0
            elif self.direction != 3:
                self.direction = 1

        # right
        elif direction == '1':
            if self.direction != 3:
                self.direction = 1

        # down right
        elif direction == '12':
            if self.direction != 3:
                self.direction = 1
            elif self.direction != 0:
                self.direction = 2

        # down
        elif direction == '2':
            if self.direction != 0:
                self.direction = 2
        
        # down left
        elif direction == '23':
            if self.direction != 0:
                self.direction = 2
            elif self.direction != 1:
                self.direction = 3

        # left
        elif direction == '3':
            if self.direction != 1:
                self.direction = 3

        # up left
        elif direction == '30':
            if self.direction != 1:
                self.direction = 3
            elif self.direction != 2:
                self.direction = 0
