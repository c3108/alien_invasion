class GameStats():
	"""Track statistics for alien invasion"""

	def __init__(self, ai_settings):
		"""Initialize statistics"""
		self.ai_settings = ai_settings
		self.reset_stats()
		# Start Alien Invasion in an active state
		self.game_active = False
		# High score should never be reset, read in from txt file
		self.read_high_score()


	def reset_stats(self):
		"""Initialize statistics that change during the game"""
		self.ships_left = self.ai_settings.ship_limit
		self.jeffs_left = self.ai_settings.jeff_limit
		self.score = 0
		self.level = 1

	def read_high_score(self):
		filename = 'ai_high_scores.txt'
		with open(filename) as file_object:
			self.high_score = int(file_object.readline())


