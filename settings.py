from random import randint

class Settings():
	"""A class to store all settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 700
		self.margin = 40

		# Ship settings
		self.ship_limit = 3

		# Jeff settings
		self.jeff_limit = 1

		# Bullet Settings
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 5

		# Jeff Bullet Settings
		self.jeff_bullet_width = 15
		self.jeff_bullet_height = 3
		self.jeff_bullet_color = 255, 0, 0
		self.jeff_bullets_allowed = 1

		# Alien Settings
		self.fleet_drop_speed = 15
		# HOw quickly the game speeds up
		self.speedup_scale = 1.1
		#How quickly the alien point values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize number of stars"""
		self.star_number = randint(0,200)
		self.red, self.green, self.blue = 0, 105, 205
		self.darken = True
		self.bg_color = (self.red, self.green, self.blue)

		"""Initialize settings that change throughout the game."""
		self.ship_speed_factor = 1.5
		self.vert_ship_speed_factor = 1.5
		self.jeff_bullet_speed_factor = 3
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 2

		# fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1

		#Scoring
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings"""
		self.ship_speed_factor *= self.speedup_scale
		self.vert_ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.jeff_bullet_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)

	def update_background(self):
		"""Change number of stars with new level"""
		self.star_number = randint(0,200)
		"""Update background color"""
		if self.blue < 20:
			self.darken = False
		elif self.blue >= 205:
			self.darken = True

		if self.darken == True:
			if self.green > 20:
				self.green -= 20
			self.blue -= 20

		if self.darken == False:
			if self.blue < 205:
				self.blue += 20
			if self.blue > 100:
				self.green += 20
			
		self.bg_color = (self.red, self.green, self.blue)


