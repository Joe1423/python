class Settings():
    """Store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game settings."""
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 0, 102)
        self.ship_speed_factor = 1.5

        #Bullet settings
        self.bullet_speed_factor = 1 
        self.bullet_width = 3
        self.bullet.height = 15
        self.bullet.color = 247, 13, 26