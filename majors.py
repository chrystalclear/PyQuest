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
	

	@property
	def InfiniteRecursion:
		print("Stack overflow. Opponent "+str(eval(repr(enemy.major)))+" has crashed.")
		enemy.stats['health'] -= 1 
		print("Enemy stats: "+str(s) for s in enemy.stats)




