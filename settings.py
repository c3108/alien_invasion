from random import randint

class Settings():
	"""A class to store all settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (0, 105, 204)
		self.margin = 20
		self.star_number = randint(0,200)


		# Ship settings
		self.ship_speed_factor = 5
		self.vert_ship_speed_factor = 5
		self.ship_limit = 3

		# Jeff settings
		self.jeff_limit = 1

		# Bullet Settings
		self.bullet_speed_factor = 6
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 5

		# Jeff Bullet Settings
		self.jeff_bullet_speed_factor = 3
		self.jeff_bullet_width = 15
		self.jeff_bullet_height = 3
		self.jeff_bullet_color = 255, 0, 0
		self.jeff_bullets_allowed = 1

		# Alien Settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 50
		#fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1
