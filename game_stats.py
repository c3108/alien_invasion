class GameStats():
	"""Track statistics for alien invasion"""

	def __init__(self, ai_settings):
		"""Initialize statistics"""
		self.ai_settings = ai_settings
		self.reset_stats()
		# Start Alien Invasion in an active state
		self.game_active = False

	def reset_stats(self):
		"""Initialize statistics that change during the game"""
		self.ships_left = self.ai_settings.ship_limit
		self.jeffs_left = self.ai_settings.jeff_limit
		self.score = 0

