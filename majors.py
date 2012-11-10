class Major(object):
	def __init__(self, name):
		self.moves={}
		self.multipliers={'History': 1, 'MCB': 1, 'Haas': 1, 'EECS': 1}

	def get(self, action):
		if action in self.moves:
			return self.moves[action]
		 
class EECS(major):
	def __init__(self, name):
		self.moves={}
		self.multipliers=major.multipliers.copy()
		self.multipliers.update(EECS=.5, History=2)
	

class History(major):
	def __init__(self, name):
		self.moves={}
		self.multipliers=major.multipliers.copy()
		self.multipliers.update(MCB=2, EECS=.5)

class MCB(major):
	def __init__(self, name):
		self.moves={}
		self.multipliers=major.multipliers.copy()
		self.multipliers.update(History=.5, Haas=2)

class Haas(major):
	def __init__(self, name):
		self.moves={}
		self.multipliers=major.multipliers.copy()
		self.multipliers.update(MCB=.5, EECS=2)