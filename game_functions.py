import sys
import pygame

def check_events(ship):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def check_keydown_events(event, ship):
	"""Respond to keypresses"""	
	if event.key == pygame.K_RIGHT:
		#Move the ship to the right.
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		#Move the ship to the right.
		ship.moving_left = True
	if event.key == pygame.K_UP:
		#Move the ship up.
		ship.moving_up = True
	if event.key == pygame.K_DOWN:
		#Move the ship down.
		ship.moving_down = True

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

def update_screen(ai_settings, screen, ship, jeff):
	"""Update images on the screen and flip the screen"""

	# Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	jeff.blitme()
	ship.blitme()
	
	# Make the most recently drawn screen visible
	pygame.display.flip()
