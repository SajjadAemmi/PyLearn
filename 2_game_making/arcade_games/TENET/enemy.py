import random
import arcade


class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture = arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")

        self.center_x = random.randint(0, 1000)
        self.center_y = 1000
        self.speed = 2
        self.change_x = random.choice([-1, 1]) * self.speed