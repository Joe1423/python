class GameStats():
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start the game in active state
        self.game_active = False
        self.score = 0
        #Highest score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit