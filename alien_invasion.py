import sys
import pygame

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
	ship = Ship(screen)
	jeff = Jeff(screen)

	# Set the background color.
	bg_color = (0, 102, 204)

	# Start the main loop for the game
	while True:

		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship, jeff)


run_game()