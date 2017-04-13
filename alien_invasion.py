import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from jeff import Jeff
import game_functions as gf

def run_game():
	#Initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Make a ship.
	ship = Ship(ai_settings, screen)
	# Make a group to store bullets in 
	bullets = Group()

	# Make a Jeff
	jeff = Jeff(screen)

	# Set the background color.
	bg_color = (0, 102, 204)

	# Start the main loop for the game
	while True:

		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()

		#Remove bullets that are off of the screen
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		gf.update_screen(ai_settings, screen, ship, bullets, jeff)


run_game()