import arcade
from player import Player
from coin import Coin


class ArcadeGame(arcade.Window):
    def __init__(self):
        """Create the main game window

        Arguments:
            width {float} -- Width of the game window
            height {float} -- Height of the game window
            title {str} -- Title for the game window
        """
        super().__init__(width=1024, height=768, title="Arcade Sample Game")

        # Set up a timer to create new coins
        self.coin_countdown = 2.5
        self.coin_interval = 0.1

        # How many coins must be on the screen before the game is over?
        self.coin_count = 10

        # How much is each coin worth?
        self.coin_value = 10

        # Set up empty sprite lists
        self.coins = arcade.SpriteList()

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

    def setup(self):
        arcade.set_background_color(color=arcade.color.DARK_BLUE)

        self.player = Player()

        # Spawn a new coin
        arcade.schedule(function_pointer=self.add_coin, interval=self.coin_countdown)

        # Load your coin collision sound
        self.coin_pickup_sound = arcade.load_sound("sounds/coin_pickup.wav")

    def add_coin(self, dt: float):
        """Add a new coin to the screen, reschedule the timer if necessary

        Arguments:
            dt {float} -- Time since last call (unused)
        """

        # Create a new coin
        new_coin = Coin(self.width, self.height)
        # Add the coin to the current list of coins
        self.coins.append(new_coin)

        # Decrease the time between coin appearances, but only if there are
        # fewer than three coins on the screen.
        if len(self.coins) < 3:
            self.coin_countdown -= self.coin_interval

            # Make sure you don't go too quickly
            if self.coin_countdown < 0.1:
                self.coin_countdown = 0.1

            # Stop the previously scheduled call
            arcade.unschedule(function_pointer=self.add_coin)

            # Schedule the next coin addition
            arcade.schedule(
                function_pointer=self.add_coin, interval=self.coin_countdown
            )

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """Processed when the mouse moves

        Arguments:
            x {float} -- X Position of the mouse
            y {float} -- Y Position of the mouse
            dx {float} -- Change in x position since last move
            dy {float} -- Change in y position since last move
        """

        # Ensure the player doesn't move off-screen
        self.player.center_x = arcade.clamp(x, 0, self.width)
        self.player.center_y = arcade.clamp(y, 0, self.height)

    def on_update(self, delta_time: float):
        """Update all the game objects

        Arguments:
            delta_time {float} -- How many seconds since the last frame?
        """

        # Check if you've picked up a coin
        coins_hit = arcade.check_for_collision_with_list(
            sprite=self.player, sprite_list=self.coins
        )

        for coin in coins_hit:
            self.player.score += self.coin_value
            arcade.play_sound(self.coin_pickup_sound)
            coin.remove_from_sprite_lists()

        # Are there more coins than allowed on the screen?
        if len(self.coins) > self.coin_count:
            # Stop adding coins
            arcade.unschedule(function_pointer=self.add_coin)

            # Show the mouse cursor
            self.set_mouse_visible(True)

            # Print the final score and exit the game
            print(f"Game over! Final score: {self.player.score}")
            exit()

    def on_draw(self):
        arcade.start_render()

        self.coins.draw()
        self.player.draw()

        # Draw the score in the lower-left corner
        arcade.draw_text(text=f"Score: {self.player.score}", start_x=50, start_y=50, font_size=32, color=arcade.color.WHITE)


if __name__ == "__main__":
    arcade_game = ArcadeGame()
    arcade_game.setup()
    arcade.run()
