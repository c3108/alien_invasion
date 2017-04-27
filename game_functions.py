import sys
import pygame
from random import randint
from time import sleep

from bullet import Bullet
from jeff_bullet import JeffBullet
from alien import Alien
from star import Star

def check_events(ai_settings, screen, ship, aliens, bullets, jeff, jeff_bullets, stats, play_button):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, aliens, screen, stats, 
				ship, bullets, jeff, jeff_bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, 
				jeff_bullets, mouse_x, mouse_y)

def start_game(ai_settings, screen, stats, ship, aliens, bullets, jeff_bullets):
	"""Start the game when either the play button or letter p is pressed"""
	#hide the mouse cursor.
	pygame.mouse.set_visible(False)

	#Empty the list of aliens and bullets
	aliens.empty()
	bullets.empty()
	jeff_bullets.empty()

	# Create a new fleet and center the ship.
	create_fleet(ai_settings, screen, ship, aliens)
	ship.center_ship()

	#reset the game statistics
	stats.reset_stats()
	stats.game_active = True


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, 
	jeff_bullets, mouse_x, mouse_y):
	"""Start a new game when the player clicks Play."""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		ai_settings.initialize_dynamic_settings()
		start_game(ai_settings, screen, stats, ship, aliens, bullets, jeff_bullets)

def check_keydown_events(event, ai_settings, aliens, screen, stats, ship, bullets, jeff, jeff_bullets):
	"""Respond to key presses"""
	if event.key == pygame.K_RIGHT:
		#Move the ship to the right.
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		#Move the ship to the right.
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		#Move the ship up.
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		#Move the ship down.
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		#Fire a bullet
		fire_bullets(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_j:
		#Fire a Jeff bullet
		fire_jeff_bullets(ai_settings, screen, jeff, jeff_bullets)
	elif event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_p:
		#start the game using the p key
		ai_settings.initialize_dynamic_settings()
		start_game(ai_settings, screen, stats, ship, aliens, bullets, jeff_bullets)

def check_keyup_events(event, ship):
	"""Respond to key releases"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False
	if event.key == pygame.K_UP:
		ship.moving_up = False
	if event.key == pygame.K_DOWN:
		ship.moving_down = False

def update_screen(ai_settings, screen, stats, sb, ship, 
	bullets, aliens, stars, jeff, jeff_bullets, play_button):
	"""Update images on the screen and flip the screen"""

	# Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	stars.draw(screen)

	#Draw the score information
	sb.prep_score()
	sb.show_score()

	ship.blitme()
	aliens.draw(screen)
	
	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	jeff.blitme()
	
	for jeff_bullet in jeff_bullets.sprites():
		jeff_bullet.draw_bullet()
	
	#Draw the play button if the game is inactive.
	if not stats.game_active:
		play_button.draw_button()

	# Make the most recently drawn screen visible
	pygame.display.flip()

def update_bullets(ai_settings, aliens, bullets, screen, ship):
	"""Update position of bullets and get rid of old bullets."""	
	bullets.update()

	#Remove bullets that are off of the screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	
def check_alien_collisions(ai_settings, aliens, bullets, jeff_bullets, screen, 
	ship, stars, stats, sb):
	"""Check for any bullets that have hit aliens and if so, get rid of the bullets"""
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
			check_high_score(stats, sb)
	#jeff_bullets are super bullets and are not destroyed by hitting aliens
	collisions = pygame.sprite.groupcollide(jeff_bullets, aliens, False, True)
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
			check_high_score(stast, sb)
	#Destroy existing bullets and create new fleet.
	#Check for if all the aliens have been destroyed, if so, remove remaining bullets and
	# create a new fleet
	if len(aliens) == 0:
		ship.center_ship()
		bullets.empty()
		jeff_bullets.empty()
		stars.empty()
		ai_settings.increase_speed()
		ai_settings.update_background()
		stats.level += 1
		sb.prep_level()
		create_fleet(ai_settings, screen, ship, aliens)
		create_stars(ai_settings, screen, stars)

def fire_bullets(ai_settings, screen, ship, bullets):
	"""Create a new bullet and add it to the bullets group"""
	new_bullet = Bullet(ai_settings, screen, ship)
	if len(bullets) < ai_settings.bullets_allowed:
		bullets.add(new_bullet)


def get_number_of_aliens_x(ai_settings, alien_width):
	"""Get the number of aliens that will fit in the screen x-direction"""
	available_space_x = ai_settings.screen_width - 2 * ai_settings.margin
	number_aliens_x = int(available_space_x/(ai_settings.margin + alien_width))
	return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
	"""Get th enumber of rows of aliens that will fit on the screen"""
	available_space_y = ai_settings.screen_height - (10 * alien_height) - ship_height
	number_rows = int(available_space_y / (alien_height + ai_settings.margin))
	return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""Create an alien and place it in the row"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = ai_settings.margin + (alien_width + ai_settings.margin) * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + (alien.rect.height + ai_settings.margin) * row_number
	aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
	"""Create a full fleet of aliens."""
	#Create an alien and find the number of aliens in the row.
	#Spacing between each alien is equal to ai_settings.margin
	#Create the first row of aliens
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_of_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)

def create_stars(ai_settings, screen, stars):
	"""Create a star background."""
	star = Star(ai_settings, screen)
	for star_number in range(ai_settings.star_number):
		star = Star(ai_settings, screen)
		star.rect.x = randint(0, ai_settings.screen_width)
		star.rect.y = randint(0, ai_settings.screen_height)
		stars.add(star)

def update_jeff_bullets(ai_settings, aliens, jeff_bullets):
	"""Update position of bullets and get rid of old bullets."""	
	jeff_bullets.update()

	#Remove bullets that are off of the screen
	for jeff_bullet in jeff_bullets.copy():
		if jeff_bullet.rect.left >= ai_settings.screen_width:
			jeff_bullets.remove(jeff_bullet)

def fire_jeff_bullets(ai_settings, screen, jeff, jeff_bullets):
	"""Create a new bullet and add it to the bullets group"""
	new_jeff_bullet = JeffBullet(ai_settings, screen, jeff)
	if len(jeff_bullets) < ai_settings.jeff_bullets_allowed:
		jeff_bullets.add(new_jeff_bullet)

def update_aliens(ai_settings, stats, screen, ship, jeff, aliens, bullets, jeff_bullets, stars, sb):
	"""Update the position of all aliens in the fleet"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	#Look for alien-ship collisions.
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets, jeff_bullets)
		print("Ship hit!!!")
	elif pygame.sprite.spritecollideany(jeff, aliens):
		print("Jeff hit!!! Ouchie!")

	check_alien_collisions(ai_settings, aliens, bullets, jeff_bullets, screen, ship, stars, stats, sb)
	#Check for aliens hitting the bottom of the screen
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, jeff_bullets)

def check_fleet_edges(ai_settings, aliens):
	"""Respond appropriately if any aliens have reached an edge."""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	"""Drop the entire fleet and change the fleet's diretion"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, jeff_bullets):
	"""Respond to ship being hit by alien"""
	if stats.ships_left > 0:
		#Decrement  ships left
		stats.ships_left -=1 

		#Make sure that bullets can't be fired before starting new round
		# Empty the list of aliens and bullets.
		
		aliens.empty()
		bullets.empty()
		jeff_bullets.empty()
		# Create a new fleet and center the ship.
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		#Need this update to get the ship coordinates fixed for space bar 
		#hits occuring right when the game goes active for bullet to fire
		#correctly
		ship.update()

		# Pause 
		sleep(2.0)
	
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, jeff_bullets):
	"""Check if any aliens have reached the botom of the screen."""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Treat this the same as if teh ship got hit.
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets, jeff_bullets)
			break

def check_high_score(stats, sb):
	"""Check to see if there is a new high score"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()


