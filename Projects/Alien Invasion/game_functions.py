import sys
import pygame
from bullet import Bullet
from alien import Alien
from stars import Star
from time import sleep

def check_events(ship, ai_settings, screen, bullets, stats, play_button, aliens):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, ai_settings, screen, ship, aliens, bullets)


def check_play_button(stats, play_button, mouse_x, mouse_y, ai_settings, screen, ship, aliens, bullets):
    """Start a new game when the player clicks play."""
    button_clicked = play_button.rect.collidepoint(mouse_y, mouse_y)
    if button_clicked and not stats.game_active:
        #Hide cursor
        pygame.mouse.set_visible(False)  
        #Reset game statistics
        stats.reset_stats()
        stats.game_active = True

        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #Create a new fleet    
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()


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

                        
def update_screen(ai_settings, screen, ship, bullets, aliens, stars, stats, play_button):
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
    #Draw the button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    #Make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Update bullet's positions and get rid of old bullets."""
    #Update bullet positions
    bullets.update()
    #Get rid of old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    #Check for any bullets that have hit aliens, if so, get rid of the bullet an the allien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        #Destroy the existing bullets and create a new fleet.
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)


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


def update_stars(stars, ai_settings):
    """Change the position of the stars."""
    stars.update(ai_settings)


def update_aliens(ai_settings, ship, screen, aliens, bullets, stats):
    """Check if the fleet is at an edge then update the position of aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    #Look for aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached and edge."""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to being hit by an alien."""
    if stats.ships_left > 0:
        #Decrement ships left
        stats.ships_left -= 1
        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        #Create a new fleet and center the ship
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()
        #Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #React the same as if the ship got hit.
            ship_hit(ai_settings, stats, stats, screen, ship, aliens, bullets)
            break


