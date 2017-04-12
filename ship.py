import pygame

class Ship():

	def __init__(self, screen):
		"""Initialize the ship and set its starting position."""
		self.screen = screen

		# Load the ship image and get its rect.
		self.icon = pygame.image.load('images/ship3.bmp')
		self.image = pygame.transform.scale(self.icon, (50, 50))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ship's position based on the movement flag."""
		if self.moving_right:
			self.rect.centerx +=2
		if self.moving_left:
			self.rect.centerx -=2


	def blitme(self):
		"""Draw teh ship at its current location."""
		self.screen.blit(self.image, self.rect)