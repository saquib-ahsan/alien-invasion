import sys
import pygame

class AlienInvasion(object):
    """Class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # create a display window for the game graphical's element
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn scren visible
            # Update the full display surface to the screen
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance,and run the game
    ai = AlienInvasion()
    ai.run_game()
