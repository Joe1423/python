class Settings():
    """Store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (0, 0, 102)
        self.ship_limit = 3

        #Alien settings
        self.fleet_drop_speed = 10

        #Bullet settings
        self.bullet_width = 4
        self.bullet_height = 12
        self.bullet_color = 247, 13, 26
        self.bullets_allowed = 3

        #Star settings
        self.star_height = 2
        self.star_width = 2
        self.star_color = 255, 255, 204
        self.star_max = 15

        #How quickly the game speeds up
        self.speedup_scale = 1.1

        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1
        #fleet direction right = 1; left = -1
        self.fleet_direction = 1
        self.alien_points = 50


    def increase_speed(self):
        """Increase speed settings and alien points values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

        