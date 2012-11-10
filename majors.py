import time
class Major(object):
	def __init__(self, name):
		self.moves={}
		self.multipliers={'History': 1, 'MCB': 1, 'Haas': 1, 'EECS': 1}

	def get(self, action):
		return self.moves[action]

class EECS(Major):
	def __init__(self, name):
		self.moves={'Infinite Recursion':InfiniteRecursion, 'Abstraction Barrier':AbstractionBarrier, 'Pop': Pop, 'Hackathon Fuel': HackathonFuel }
		self.multipliers=major.multipliers.copy()
		self.multipliers.update(EECS=.5, History=2)
	
	def InfiniteRecursion(self,enemy):
		energycost = 60
		if self.energy < energycost:
			print("You're too tired to do that! Rack up some energy by taking some HackathonFuel.")
		i=0
		while i>20:
			print ("Enemy takes 1 point damage")
			self.enemy.hp -= 1
			i+=1 
		print("Stack overflow. Maximum recursion depth reached. Opponent "+enemy.name+" has crashed.")
		self.energy-=60
		print("Your energy decreases to "+str(self.energy)+" points.")

	def AbstractionBarrier(self,enemy):
		print("You create an abstraction barrier between you and "+enemy.name+".")
		self.defense+=2
		self.energy-=5
		print("Your defense increases to "+str(self.defense)+" points.")
		print("Your energy decreases to "+str(self.energy)+" points.")

	def Pop(self,enemy):
		print("You pop off 4 of "+enemy.name+"'s health points")
		self.hp-=4
		self.energy-=5
		print(enemy.name+"'s health points decrease to "+str(self.hp)+" points.")
		print("Your energy decreases to "+str(self.energy)+" points.")

	def HackathonFuel(self,enemy):
		print("You take a swig of a concoction made of Red Bull, Monster, Coffee, Coke, and liquified cocaine.")
		if self.energy+20 >=100:
			print("Your energy increases to 100 points.")
		else:
			self.energy+=20
			print("Your energy increases to "+ str(self.energy) +" points.")




class History(Major):
	def __init__(self, name):
		self.moves={}
		self.multipliers=major.multipliers.copy()
		self.multipliers.update(MCB=2, EECS=.5)

class MCB(Major):
	def __init__(self, name):
		self.moves={'Point Mutation': PointMutation}
		self.multipliers=major.multipliers.copy()
		self.multipliers.update(History=.5, Haas=2)

	def PointMutation(self,enemy):
		energycost = 50
		if self.energy > energycost:
			print(energy.name+" was too tired to do that!")
		print(self.name+" used Point Mutation!")
		print(self.name+" grows an extra arm and punches you square in the face.")
		print("Your health decreases to " +str(enemy.hp-=10)+" points.")
		enemy.atk+=5
		print(self.name+"'s attack increases to "+str(enemy.atk)+" points.")
		self.energy-=30

	def SetCurve(self,enemy):
		energycost = 40
		if self.energy > energycost:
			print(energy.name+" was too tired to do that!")
		print(self.name+" sets the curve!")
		print('"That test was so easy. I barely even studied."')
		enemy.energy-=5
		print("Your esteem is lowered, and your health and energy decrease to "+str(enemy.hp-=6)+" and "+str(enemy.energy)+ " respectively.")
		self.energy-=20

	def Photosynthesis(self,enemy):
		print(self.name+" uses Photosynthesis!")
		print(self.name+" unfolds his leaves and soaks up the incredible energy from the sun.")
		self.energy+=20
		print(self.name+"'s energy increases to "+str(self.energy)+" points.")

	def Mitosis(self,enemy):
		print(self.name+" undergoes Mitosis!")
		print('"Ho-ho! My defenses are now double!!"')
		if self.defense == 0:
			self.defense = 2
		else:
			self.defense*=2
		print(self.name+"'s defense increases to "+str(self.defense)+" points.")











class Haas(Major):
	def __init__(self, name):
		self.moves={}
		self.multipliers=major.multipliers.copy()
		self.multipliers.update(MCB=.5, EECS=2)