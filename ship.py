import pygame

class Ship():

	def __init__(self, ai_settings, screen):
		"""Initialize the ship and set its starting position."""
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the ship image and get its rect.
		self.icon = pygame.image.load('images/ship3.bmp')
		self.image = pygame.transform.scale(self.icon, (50, 50))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

		# Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)
		self.vert_center = float(self.rect.centery)

		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False


	def update(self):
		"""Update the ship's position based on the movement flag."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.vert_center -= self.ai_settings.vert_ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.vert_center += self.ai_settings.vert_ship_speed_factor


		self.rect.centerx = self.center
		self.rect.centery = self.vert_center


	def blitme(self):
		"""Draw teh ship at its current location."""
		self.screen.blit(self.image, self.rect)