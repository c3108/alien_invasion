import pygame
from pygame.sprite import Sprite

class JeffBullet(Sprite):
	"""A Class to manage bullets fired from the ship"""

	def __init__(self, ai_settings, screen, jeff):
		"""Create a bullet object at the ship's current position."""
		super(JeffBullet, self).__init__()
		self.screen = screen

		# Create a bullet rect at (0,0) and then est correct position
		self.rect = pygame.Rect(0, 0, ai_settings.jeff_bullet_width,
			ai_settings.jeff_bullet_height)
		self.rect.centerx = jeff.rect.centerx
		# Start bulletes from the approx location of Jeff's eyes
		self.rect.top = jeff.rect.top + 19

		# Store the bullet's position as a decimal value.
		self.x = float(self.rect.x)

		self.color = ai_settings.jeff_bullet_color
		self.speed_factor = ai_settings.jeff_bullet_speed_factor

	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal position of teh bullet.
		self.x += self.speed_factor
		# Update teh rect position.
		self.rect.x = self.x

	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)
