class major(object):
	def __init__(self, name):
		self.moves={}
		self.multipliers={'History': 1, 'MCB': 1, 'Haas': 1, 'EECS': 1}
		 
class EECS(major):
	def __init__(self, name):
		self.moves={}
		self.multipliers=major.multipliers.copy()
		self.multipliers.update(EECS=.5, History=2)
	
	def get(self, action):
		if action in self.moves:
			return self.moves[action]

	def nogirlsallowed
