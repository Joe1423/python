import pygame 
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    """A class to create stars."""
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #Create the star at 0,0 with 2px width and height
        self.rect = pygame.Rect(0, 0,
            ai_settings.star_width,
            ai_settings.star_height)
        #position of the start
        self.rect.centerx = randint(0, ai_settings.screen_width)
        self.rect.centery = randint(0, ai_settings.screen_height)
        #Star color
        self.color = ai_settings.star_color

    def update(self, ai_settings):
        """Change the position of the stars"""
        self.rect.centerx = randint(0, ai_settings.screen_width)
        self.rect.centery = randint(0, ai_settings.screen_height)

    def draw(self):
        """Draw the star."""
        pygame.draw.rect(self.screen, self.color, self.rect)