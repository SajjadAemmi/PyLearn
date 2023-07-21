import threading
import math
import os
import random
import time

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Silver SpaceCraft"
BULLET_SPEED = 4


class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.speed = 4
        self.width = 48
        self.height = 48
        self.center_x = random.randint(1, SCREEN_WIDTH)
        self.center_y = SCREEN_HEIGHT + self.height
        self.angle = 180
        self.bullet_list = []

    def move(self):
        self.center_y -= self.speed


class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.speed = 4
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.angle = host.angle

    def move(self):
        angle_rad = math.radians(self.angle)
        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)


class SpaceCraft(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.speed = 4
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 32
        self.width = 48
        self.height = 48
        self.angle = 0
        self.change_angle = 0
        self.bullet_list = []

    def rotate(self):
        self.angle += self.change_angle * self.speed

    def fire(self):
        self.bullet_list.append(Bullet(self))


class Game(arcade.Window):
    """ Main application class """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.enemy_list = []
        self.player = SpaceCraft()
        self.start_time = time.time()

        self.my_thread = threading.Thread(target=self.create_enemy)
        self.my_thread.start()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        for bullet in self.player.bullet_list:
            bullet.draw()

        self.player.draw()
        
        for enemy in self.enemy_list:
            enemy.draw()

    def create_enemy(self):
        while True:
            self.enemy_list.append(Enemy())
            time.sleep(3)

    def on_update(self, delta_time):
        """ All the game logic goes here. """
        self.player.rotate()

        for enemy in self.enemy_list:
            enemy.move()
        
        for bullet in self.player.bullet_list:
            bullet.move()

        for bullet in self.player.bullet_list:
            for enemy in self.enemy_list:
                if arcade.check_for_collision(bullet, enemy):
                    self.enemy_list.remove(enemy)
                    self.player.bullet_list.remove(bullet)

    def on_key_press(self, key, modifiers):
        # Rotate left/right
        if key == arcade.key.LEFT:
            self.player.change_angle = 1
        elif key == arcade.key.RIGHT:
            self.player.change_angle = -1
        elif key == arcade.key.SPACE:
            self.player.fire()        

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_angle = 0

    # def on_mouse_motion(self, x, y, delta_x, delta_y):
    #     """Called whenever the mouse moves. """
    #     self.player.center_x = x
    #     self.player.center_y = y


if __name__ == "__main__":
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()