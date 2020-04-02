import pygame

class Ship():
    def __init__(self, screen, ai_settings):
        """Initialize the ship and the starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ship images and get its rect
        self.image = pygame.image.load('images/space_ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        #Movement Flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship position based on the flags value."""
        #Update the ship's center value, not the rect.
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        #Update rect object from self.center
        self.rect.centerx = self.center
            

    def blitme(self):
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx