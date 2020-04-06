#import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    #Initialize game and create a screen object
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    #Make the play button.
    play_button = Button(ai_settings, screen, 'play')

    #Creat an instance of to store game statistics
    stats = GameStats(ai_settings)

    #Display the ship
    ship = Ship(screen, ai_settings)

    #Make a group of bullets and aliens
    bullets = Group()
    aliens = Group()
    stars = Group()

    #Create a fleet of aliens.
    gf.create_fleet(ai_settings, screen, aliens, ship)

    #Create the stars
    gf.create_star(ai_settings, screen, stars)


    #Start the main loop for the game
    while True:
        #Watch for keyboard and mouse events
        gf.check_events(ship, ai_settings, screen, bullets, stats, play_button, aliens)

        if stats.game_active:
            #Update ship movement based on keypresses
            ship.update()
            #Manage the bullets movement
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            #Move the aliens
            gf.update_aliens(ai_settings, ship, screen, aliens, bullets, stats)
            #Update the stars position
            gf.update_stars(stars, ai_settings)
            
        #Redraw and update the screen
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stars, stats, play_button)

run_game()