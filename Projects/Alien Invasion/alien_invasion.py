#import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    #Initialize game and create a screen object
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    #Display the ship
    ship = Ship(screen, ai_settings)

    #Start the main loop for the game
    while True:
        #Watch for keyboard and mouse events
        gf.check_events(ship)
        #Redraw and update the screen
        gf.update_screen(ai_settings, screen, ship)
        #Update ship movement based on keypresses
        ship.update()


run_game()