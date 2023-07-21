import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Turn and Move Example"


class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.center_x = random.randint(1, SCREEN_WIDTH)
        self.center_y = random.randint(1, SCREEN_HEIGHT)
        self.change_x = 0
        self.change_y = 0
        self.color = arcade.color.RED
        self.size = 10
        self.width = 20
        self.height = 20

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.size, self.color)


class Snake(arcade.Sprite):
    """
    Sprite that turns and moves
    """
    def __init__(self):
        super().__init__()

        self.speed = 4
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.change_x = 0
        self.change_y = 0
        self.width = 16
        self.height = 16

        self.color1 = arcade.color.GREEN
        self.color2 = arcade.color.DARK_GREEN
        self.r = 8
        self.body = []
        self.body_size = 0

    def draw(self):
        for i, part in enumerate(self.body):
            if i % 2 == 0:
                arcade.draw_circle_filled(part['center_x'], part['center_y'], self.r, self.color2)
            else:
                arcade.draw_circle_filled(part['center_x'], part['center_y'], self.r, self.color1)
                
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color1)

    def eat(self):
        self.body_size += 1

    def on_update(self, delta_time: float = 1/60):
        self.body.append({'center_x': self.center_x, 'center_y': self.center_y})
        if len(self.body) > self.body_size:
            self.body.pop(0)

        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
     

#  Main application class
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
        arcade.set_background_color(arcade.color.SAND)

        self.snake = Snake()
        self.apple = Apple()
        # self.set_update_rate(1/30)

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.snake.draw()
        self.apple.draw()
        
    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        self.snake.on_update(delta_time)
        self.apple.on_update()

        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat()
            self.apple = Apple()

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
    
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

        elif key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
    
        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
    

if __name__ == "__main__":
    window = MyGame()
    arcade.run()
