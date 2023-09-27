import random
# BAD PRACTICE IN 3.. 2.. 1.. GO!
from game_variables import *

pipe = random.choice(PIPES)


class Pipe(arcade.Sprite):

    def __init__(self, image, scale=1):
        """
        Initializer for the pipe object, it's not really correct to call this Pipe since this class is responsible of
        creating two pipes as an obstacle for the bird.
        """
        super().__init__(image, scale)
        # the amount of pixels the pipe move each frame.
        self.horizontal_speed = -1.5
        # Just a boolean to check if the bird passed this pipe successfully.
        self.scored = False

    @classmethod
    def random_pipe_obstacle(cls, sprites, height):
        """
        A class method that creates two pipes each with minimum height of MIN_HEIGHT and minimum MIN_GAP distance
        between the two pipes. Each obstacle created from this method will be placed exactly 1 pixel out of the screen.
        Sprites: Dictionary holding textures to both base and background (to be used as a reference to where to draw
        the pipe, could be improved and optimized?)
        """
        bottom_pipe = cls(pipe)
        bottom_pipe.top = random.randrange(sprites['base'].height + MIN_HEIGHT, height - GAP_SIZE - MIN_HEIGHT)
        bottom_pipe.left = sprites['background'].width

        top_pipe = cls(pipe)
        top_pipe.angle = 180
        top_pipe.left = sprites['background'].width
        top_pipe.bottom = bottom_pipe.top + GAP_SIZE
        # top_pipe.bottom = random.randrange(bottom_pipe.top + MIN_GAP, height - MIN_HEIGHT)

        return bottom_pipe, top_pipe

    def update(self):
        # Move each frame in the negative x direction.
        self.center_x += self.horizontal_speed