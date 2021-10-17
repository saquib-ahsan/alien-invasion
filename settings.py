# Instead of adding settings throughout the code, this
# module stores all the necessary settings for the
# Alien Invasion game.
class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5
