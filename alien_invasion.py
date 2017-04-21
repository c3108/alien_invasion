import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from jeff import Jeff
import game_functions as gf
from game_stats import GameStats
from button import Button

def run_game():
	#Initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Make the play button
	play_button = Button(ai_settings, screen, "Play")

	# Make a ship.
	ship = Ship(ai_settings, screen)
	# Make a group to store bullets in 
	bullets = Group()
	jeff_bullets = Group()
	aliens = Group()
	stars = Group()

	# Make a Jeff
	jeff = Jeff(screen)


	gf.create_stars(ai_settings, screen, stars)
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Create an instance to sotre game statistics.
	stats = GameStats(ai_settings)

	# Start the main loop for the game
	while True:

		gf.check_events(ai_settings, screen, ship, aliens, bullets, jeff, jeff_bullets, stats, play_button)
		
		if stats.game_active:
			ship.update()
			gf.update_jeff_bullets(ai_settings, aliens, jeff_bullets)
			gf.update_bullets(ai_settings, aliens, bullets, screen, ship)
			gf.update_aliens(ai_settings, stats, screen, ship, jeff, aliens, bullets, jeff_bullets)
		gf.update_screen(ai_settings, screen, stats, ship, bullets, aliens, stars, jeff, jeff_bullets, play_button)


run_game()