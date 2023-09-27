import pygame
from player import Player
from coin import Coin


class Game:
    def __init__(self):
        # Set the width and height of the output window, in pixels
        self.width = 1024
        self.height = 768

        # How quickly do you generate coins? Time is in milliseconds
        self.coin_countdown = 2500
        self.coin_interval = 100

        # How many coins can be on the screen before you end?
        self.COIN_COUNT = 10

        # Set up the drawing window
        self.screen = pygame.display.set_mode(size=[self.width, self.height])
        pygame.mouse.set_visible(False)  # Hide the mouse cursor
        self.font = pygame.font.SysFont("any_font", 36)

        # Set up the clock for a decent frame rate
        self.clock = pygame.time.Clock()

        # Create a custom event for adding a new coin
        self.ADDCOIN = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDCOIN, self.coin_countdown)

        # Set up the coin_list
        self.coin_list = pygame.sprite.Group()
        self.coin_pickup_sound = pygame.mixer.Sound("sounds/coin_pickup.wav")
        self.player = Player()

    def draw(self):
        self.screen.fill((0, 0, 32))

        self.player.draw(self.screen)
        for coin in self.coin_list:
            coin.draw(self.screen)

        # draw the score at the bottom left
        score_block = self.font.render(f"Score: {self.player.score}", False, (255, 255, 255))
        self.screen.blit(score_block, (50, self.height - 50))

        pygame.display.update()

    def play(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == self.ADDCOIN:
                    # Create a new coin and add it to the coin_list
                    new_coin = Coin(self.width, self.height)
                    self.coin_list.add(new_coin)

                    # Speed things up if fewer than three coins are on-screen
                    if len(self.coin_list) < 3:
                        self.coin_countdown -= self.coin_interval
                    # Need to have some interval
                    if self.coin_countdown < 100:
                        self.coin_countdown = 100

                    # Stop the previous timer by setting the interval to 0
                    pygame.time.set_timer(self.ADDCOIN, 0)

                    # Start a new timer
                    pygame.time.set_timer(self.ADDCOIN, self.coin_countdown)

            # Update the player position
            self.player.update(pygame.mouse.get_pos())

            # Check if the player has collided with a coin, removing the coin if so
            coins_collected = pygame.sprite.spritecollide(
                sprite=self.player, group=self.coin_list, dokill=True
            )
            for coin in coins_collected:
                self.player.score += 10
                self.coin_pickup_sound.play()

            if len(self.coin_list) >= self.COIN_COUNT:
                running = False

            self.draw()

            # Ensure you maintain a 30 frames per second rate
            self.clock.tick(30)

        print("Game over! Final score:", self.player.score)
        

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.play()
    pygame.quit()
