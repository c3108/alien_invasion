import pygame

class Jeff():

	def __init__(self, screen):
		"""Initialize Jeff and set his starting position"""
		self.screen = screen

		# Load the Jeff image and get its rect.
		self.image = pygame.image.load('images/jeff.bmp')
		#self.image = pygame.transform.scale(self.icon, (50, 50))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new jeff at the bottom left of the screen.
		self.rect.left = self.screen_rect.left
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		"""Draw teh ship at its current location."""
		self.screen.blit(self.image, self.rect)

