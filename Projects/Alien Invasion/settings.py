class Settings():
    """Store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game settings."""
        #Screen settings
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (0, 0, 102)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet direction right = 1; left = -1
        self.fleet_direction = 1

        #Bullet settings
        self.bullet_speed_factor = 2 
        self.bullet_width = 4
        self.bullet_height = 12
        self.bullet_color = 247, 13, 26
        self.bullets_allowed = 3

        #Star settings
        self.star_height = 2
        self.star_width = 2
        self.star_color = 255, 255, 204
        self.star_max = 15