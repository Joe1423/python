#import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    #Initialize game and create a screen object
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    #Display the ship
    ship = Ship(screen, ai_settings)

    #Make a group of bullets and aliens
    bullets = Group()
    aliens = Group()

    #Create a fleet of aliens.
    gf.create_fleet(ai_settings, screen, aliens, ship)

    #Start the main loop for the game
    while True:
        #Watch for keyboard and mouse events
        gf.check_events(ship, ai_settings, screen, bullets)

        #Update ship movement based on keypresses
        ship.update()

        #Mange the bullets movement
        bullets.update()

        #Update and Get rid of the bullets that have dissapeared
        gf.update_bullets(bullets)

        #Redraw and update the screen
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)
        

run_game()