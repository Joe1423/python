import sys
import pygame
from bullet import Bullet

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


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

                        
def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    #Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

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
