import sys
import pygame
from bullet import Bullet
from aliens import Alien
from time import sleep



def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
    	fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
    	sys.exit()



def fire_bullet(ai_settings, screen, ship, bullets):
	# Create a new bullet and add it to the bullets group.
	if len(bullets) < ai_settings.bullets_allowed:
	    new_bullet = Bullet(ai_settings, screen, ship)
	    bullets.add(new_bullet)
	else: print("running out of bullets, wait some bullets dispear on the screen")



def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x



def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows



def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""Create an alien and place it in the row."""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number 
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)



def create_fleet(ai_settings, screen, aliens, ship):
	"""Create a full fleet of aliens."""
	# Create an alien and find the number of aliens in a row.
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height,
           alien.rect.height)
	# # Create the first row of aliens.
	# for alien_number in range(number_aliens_x + 1):
	# 	create_alien(ai_settings, screen, aliens, alien_number)
	
	# Create the fleet of aliens.
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number,
                row_number)



# def create_fleet(ai_settings, screen, aliens):
#     """Create a full fleet of aliens."""
#     # Create an alien and find the number of aliens in a row.
#     # Spacing between each alien is equal to one alien width.
#     alien = Alien(ai_settings, screen)
#     alien_width = alien.rect.width
#     available_space_x = ai_settings.screen_width - 1.5 * alien_width
#     number_aliens_x = int(available_space_x / (1.5 * alien_width))
#     # Create the first row of aliens.
#     for alien_number in range(number_aliens_x +1):
#         # Create an alien and place it in the row.
#         alien = Alien(ai_settings, screen)
#         alien.x = alien_width + 1.5 * alien_width * alien_number
#         alien.rect.x = alien.x
#         aliens.add(alien)



def check_fleet_edges(ai_settings, aliens):
	"""Respond appropriately if any aliens have reached an edge."""
	for alien in aliens.sprites(): 
		if alien.check_edges():
			change_fleet_direction_and_update_y(ai_settings, aliens)
			break



def change_fleet_direction_and_update_y(ai_settings, aliens):
	"""Drop the entire fleet and change the fleet's direction."""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
		#print(ai_settings.fleet_direction)



def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False



def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        # Hide the mouse cursor. 
        pygame.mouse.set_visible(False)
        # Reset the game statistics. 
        stats.reset_stats() 
        stats.game_active = True
    
    # Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()
    stats.score = 0
    sb.prep_score()
    stats.level = 0
    sb.prep_level()
    sb.prep_ships()
        
    # Create a new fleet and center the ship.
    create_fleet(ai_settings, screen, aliens, ship)
    ship.center_ship()



def check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens, sb):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)



def remove_bullet(bullets):
	""" Remove bullet from Group that is out of screen """
	### use shallow copy
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
    ### To check if the bullet has been deleted from group
	print(len(bullets))



def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """Respond to ship being hit by alien."""
    # Decrement ships_left.
    
    if stats.ships_left > 0:
        ## Decrement ships_left
        stats.ships_left -= 1

        # Update scoreboard
        sb.prep_ships()

        # Empty the list of aliens and bullets. w aliens.empty()
        bullets.empty()
        aliens.empty()
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()
        # Pause.
        sleep(0.5)
    else: 
        stats.game_active = False
        pygame.mouse.set_visible(True)
        aliens.empty()



def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens,
        bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if a ship got hit.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """Update the postions of all aliens in the fleet."""
    """Check if the fleet is at an edge, 
    and then update the postions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

     # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!!!")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
        print(str(stats.ships_left) + ' ' + "lives left")

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)



def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
    check_high_score(stats, sb)

    if len(aliens) == 0:
        # Destroy existing bullets, create new fleet and speed up game.
        bullets.empty()
        ai_settings.increase_speed()

        # If the entire fleet is destroyed, start a new level.
        # Increase level.
        if not pygame.sprite.spritecollideany(ship, aliens):
            stats.level += 1
            sb.prep_level()

        create_fleet(ai_settings, screen, aliens, ship)



def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()



def update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb):
    """Update position of bullets and get rid of old bullets.""" 
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb)



def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, sb):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    # Draw the play button if the game is inactive.

    screen.fill(ai_settings.bg_color)
    ## Redraw all bullets behind ship and aliens      
    #Make the most recently drawn screen visible.
    for bullet in bullets.sprites():
    	bullet.draw_bullet()
    	bullet.update()
    remove_bullet(bullets)
    ship.blitme()
    update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)
    aliens.draw(screen)

    # Draw the score information. 
    sb.show_score()
    
    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

