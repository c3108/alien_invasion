import pygame
from pygame.sprite import Sprite

class Star(Sprite):

	def __init__(self, ai_settings, screen):
		"""A class to represent a single alien in the fleet"""
		super(Star, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the alien image and get its rect.
		self.image = pygame.image.load('images/star.bmp')
		#self.image = pygame.transform.scale(self.icon, (66, 35))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the top left of the screen.
		self.rect.x = 0
		self.rect.y = 10
		
		# Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)
		self.vert_center = float(self.rect.centery)

	def blitme(self):
		"""Draw the alien at its current location."""
		self.screen.blit(self.image, self.rect)