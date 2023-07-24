import math
import random
# BAD BAD BAD
from game_variables import *


class Bird(arcade.AnimatedTimeSprite):

    def __init__(self, center_x, center_y, death_height):
        super().__init__(center_x=center_x, center_y=center_y)
        self.score = 0
        self.textures = []
        rnd = random.SystemRandom()
        # Randomly choose a bird color
        color = rnd.choice(list(BIRDS))
        for i in range(4):
            self.textures.append(arcade.load_texture(BIRDS[color][i % 3]))

        self.cur_texture_index = 0
        self.vel = 0
        self.dy = 0
        self.death_height = death_height
        self.dead = False

    def set_velocity(self, velocity):
        self.vel = velocity

    def update(self, dt=0):
        if self.dead:
            self.angle = -90
            if self.center_y > self.death_height + self.height//2:
                self.center_y -= 4
            return

        if self.vel > 0:
            # self.center_y += (1 - math.cos((JUMP_DY - self.vel) * math.pi)) * JUMP_STEP
            self.center_y += DY
            # self.center_y += self.vel
            # self.vel = 0
            self.vel -= DY
            if self.angle < 30:
                self.angle = min(self.angle + ANGLEP, 30)
        else:
            if self.angle > -90:
                self.angle = max(self.angle + ANGLEM, -90)
            self.center_y -= GRAVITY

    def flap(self):
        self.vel = JUMP_DY

    def die(self):
        self.dead = True
        arcade.play_sound(SOUNDS['die'])
