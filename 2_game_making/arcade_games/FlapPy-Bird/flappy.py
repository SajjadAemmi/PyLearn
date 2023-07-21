import arcade
import random
from bird import Bird
from pipe import Pipe
from game_state import State
from game_variables import *


class Game(arcade.Window):

    def __init__(self, width, height):

        """
        Initializer for the game window, note that we need to call setup() on the game object.
        """
        super().__init__(width, height, title="Flappy Bird!")

        self.sprites = None
        self.pipe_sprites = None
        self.bird = None
        # Background texture
        self.background = None
        # Base texture
        self.base = None
        # List of birds, even though we've only one bird, it's better to draw a SpriteList than to draw a Sprite
        self.bird_list = None
        # Score texture
        self.score_board = None
        # A boolean to check if the user tapped
        self.flapped = False
        # initial score
        self.score = None
        # Initial state of the game
        self.state = State.MAIN_MENU
        # The texture for the start and game over screens.
        self.menus = {'start': arcade.load_texture(GET_READY_MESSAGE),
                      'gameover': arcade.load_texture(GAME_OVER),
                      'play': arcade.load_texture(PLAY_BUTTON)}

    def setup(self):
        self.score = 0
        self.score_board = arcade.SpriteList()
        self.pipe_sprites = arcade.SpriteList()
        self.bird_list = arcade.SpriteList()
        # A dict holding sprites of static stuff like background & base
        self.background = arcade.load_texture(random.choice(BACKGROUNDS))
        self.base = arcade.load_texture(BASE)
        # A dict holding a reference to the textures
        self.sprites = dict()
        self.sprites['background'] = self.background
        self.sprites['base'] = self.base
        # The bird object itself.
        # The AnimatedTimeSprite makes an animated sprite that animates over time.
        self.bird = Bird(50, self.height//2, self.base.height)
        self.bird_list.append(self.bird)

        # Create a random pipe (Obstacle) to start with.
        start_pipe1 = Pipe.random_pipe_obstacle(self.sprites, self.height)
        self.pipe_sprites.append(start_pipe1[0])
        self.pipe_sprites.append(start_pipe1[1])

    def draw_score_board(self):
        """
        Draws the score board
        """
        self.score_board.draw()

    def draw_background(self):
        """
        Draws the background.
        """
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.background.width, self.background.height,
                                      self.background, 0)

    def draw_base(self):
        """
        Bet you expected what this does. :)
        """
        arcade.draw_texture_rectangle(self.width//2, self.base.height//2, self.base.width, self.base.height, self.base, 0)

    def on_draw(self):

        """
        This is the method called when the drawing time comes.
        """
        # Start rendering and draw all the objects
        arcade.start_render()
        # Calling "draw()" on a SpriteList object will call it on each child in the list.

        # Whatever the state, we need to draw background, then pipes on top, then base, then bird.
        self.draw_background()
        self.pipe_sprites.draw()
        self.draw_base()
        self.bird_list.draw()

        if self.state == State.MAIN_MENU:
            # Show the main menu
            texture = self.menus['start']
            arcade.draw_texture_rectangle(self.width//2, self.height//2 + 50, texture.width, texture.height, texture, 0)

        elif self.state == State.PLAYING:
            # Draw the score board when the player start playing.
            self.draw_score_board()

        elif self.state == State.GAME_OVER:
            # Draw the game over menu if the player lost + draw the score board.
            texture = self.menus['gameover']
            arcade.draw_texture_rectangle(self.width//2, self.height//2 + 50, texture.width, texture.height, texture, 0)
            texture = self.menus['play']
            arcade.draw_texture_rectangle(self.width//2, self.height//2 - 100, texture.width, texture.height, texture, 0)
            self.draw_score_board()

    def on_key_release(self, symbol, modifiers):

        if symbol == arcade.key.SPACE and self.state == State.MAIN_MENU:
            # If the game is starting, just change the state and return
            self.state = State.PLAYING
            return
        if symbol == arcade.key.SPACE:
            self.flapped = True

    def on_mouse_press(self, x, y, button, modifiers):

        if self.state == State.GAME_OVER:
            texture = self.menus['play']
            h = self.height//2 - 100
            w = self.width//2
            if w - texture.width//2 <= x <= w + texture.width//2:
                if h - texture.height//2 <= y <= h + texture.height//2:
                    self.setup()
                    self.state = State.MAIN_MENU

    def build_score_board(self):
        """
        Builds the score board with images. Basically how this work:
        1. Calculate how many digits in the score.
        2. Calculate width (Number of digits * width of each digit image width)
        3. Calculate the "left" x position that makes all the images centered.
        4. Just append every digit's image in the score board.
        :return:
        """
        score_length = len(str(self.score))
        score_width = 24 * score_length
        left = (self.width - score_width) // 2
        self.score_board = arcade.SpriteList()
        for s in str(self.score):
            self.score_board.append(arcade.Sprite(SCORE[s], 1, center_x=left + 12, center_y=450))
            left += 24

    def on_update(self, delta_time):

        """
        This is the method called each frame to update objects (Like their position, angle, etc..) before drawing them.
        """
        # print(delta_time)
        # Whatever the state, update the bird animation (as in advance the animation to the next frame)
        self.bird_list.update_animation()

        if self.state == State.PLAYING:
            self.build_score_board()

            # If the player pressed space, let the bird fly higher
            if self.flapped:
                arcade.play_sound(SOUNDS['wing'])
                self.bird.flap()
                self.flapped = False

            # Check if bird is too high
            if self.bird.top > self.height:
                self.bird.top = self.height

            # Check if bird is too low
            if self.bird.bottom <= self.base.height:
                if self.bird.change_y < 0:
                    self.bird.change_y = 0
                self.bird.bottom = self.base.height

            new_pipe = None

            # Kill pipes that are no longer shown on the screen as they're useless and live in ram and create a new pipe
            # when needed. (If the center_x of the closest pipe to the bird passed the middle of the screen)
            for pipe in self.pipe_sprites:
                if pipe.right <= 0:
                    pipe.kill()
                elif len(self.pipe_sprites) == 2 and pipe.right <= random.randrange(self.width // 2, self.width // 2 + 15):
                    new_pipe = Pipe.random_pipe_obstacle(self.sprites, self.height)

            if new_pipe:
                self.pipe_sprites.append(new_pipe[0])
                self.pipe_sprites.append(new_pipe[1])

            # This calls "update()" Method on each object in the SpriteList
            self.pipe_sprites.update()
            self.bird.update(delta_time)
            self.bird_list.update()

            # If the bird passed the center of the pipe safely, count it as a point.
            # Hard coding.. :)
            if self.bird.center_x >= self.pipe_sprites[0].center_x and not self.pipe_sprites[0].scored:
                arcade.play_sound(SOUNDS['point'])
                self.score += 1
                # Well, since each "obstacle" is a two pipe system, we gotta count them both as scored.
                self.pipe_sprites[0].scored = True
                self.pipe_sprites[1].scored = True
                print(self.score)

            # Check if the bird collided with any of the pipes
            hit = arcade.check_for_collision_with_list(self.bird, self.pipe_sprites)

            if any(hit):
                arcade.play_sound(SOUNDS['hit'])
                self.state = State.GAME_OVER
                self.bird.die()

        elif self.state == State.GAME_OVER:
            # We need to keep updating the bird in the game over scene so it can still "die"
            self.bird.update()


def main():
    game = Game(288, 512)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
