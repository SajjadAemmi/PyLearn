import random
import arcade


class Coin(arcade.Sprite):
    def __init__(self, game_width, game_height):
        super().__init__(":resources:images/items/coinGold.png")
        self.center_x = random.randint(20, game_width - 20)
        self.center_y = random.randint(20, game_height - 20)
