import arcade


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/alien/alienBlue_jump.png")
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        self.score = 0