import sys
import pygame
from bullet import Bullet
from alien import Alien
from stars import Star

def check_events(ship, ai_settings, screen, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        #Move a ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #MOve ship to left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Create a new bullet and add it to the bullet group
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        #Finish the game
        sys.exit()  


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

                        
def update_screen(ai_settings, screen, ship, bullets, aliens, stars):
    """Update images on the screen and flip to the new screen."""
    #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    #Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #Draw the ship
    ship.blitme()
    #Draw the alien fleet
    aliens.draw(screen)
    #Draw star group
    for star in stars:
        star.draw()

    #Make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(bullets):
    """Update bullet's positions and get rid of old bullets."""
    #Update bullet positions
    bullets.update()
    #Get rid of old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit hasn't been reached yet."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in a row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    """Create a full fleet of aliens."""
    #Create an alien and find the number of aliens in a row
    #Space between each alien is equal to an alien width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, 
        alien.rect.height)

    #Create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #Create an alien an place it the row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
        

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_star(ai_settings, screen, stars):
    """Add stars to the group until it reach its limit"""
    count = 0
    while count < ai_settings.star_max:
        new_star = Star(ai_settings, screen)
        stars.add(new_star)
        count += 1


# def update_stars(stars):
#     """Change the position of the stars."""
#     stars.update()