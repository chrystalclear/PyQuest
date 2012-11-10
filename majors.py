import time
class Major(object):
	def __init__(self, name):
		self.moves={}
		self.multipliers={'History': 1, 'MCB': 1, 'Haas': 1, 'EECS': 1}

	def get(self, action):
		return self.moves[action]

class EECS(Major):
	def __init__(self, name):
		self.moves={'Infinite Recursion':InfiniteRecursion, 
					'Abstraction Barrier':AbstractionBarrier, 
					'Pop': Pop, 
					'Hackathon Fuel': HackathonFuel }
		self.multipliers=major.multipliers.copy()
		self.multipliers.update(EECS=.5, History=2)
	
	def InfiniteRecursion(self,enemy):
		energycost = 60
		if self.energy < energycost:
			print("You're too tired to do that! Rack up some energy by taking some Hackathon Fuel.")
		i=0
		while i>20:
			print ("Enemy takes 1 point damage")
			self.enemy.hp -= 1
			i+=1 
		print("Stack overflow. Maximum recursion depth reached. Opponent "+enemy.name+" has crashed.")
		self.energy-=60
		time.sleep(1)
		print("Your energy decreases 60 points. Recursion indefinitely is incredibly tiring.")

	def AbstractionBarrier(self,enemy):
		print("You create an abstraction barrier between you and "+enemy.name+".")
		self.defense+=2
		self.energy-=5
		time.sleep(1)
		print("Your Abstraction Sheild makes you feel safe. Your defense increases 2 points.")
		print("Your energy decreases 5 points.")

	def Pop(self,enemy):
		dmg =int(0.75*self.atk*self.multipliers[enemy.Major])-enemy.defense
		print("You pop off"+dmg+"of "+enemy.name+"'s health points.")
		self.hp-=dmg
		self.energy-=5
		time.sleep(1)
		print("Your energy drops down to 5 points. Popping is hard work.")

	def HackathonFuel(self,enemy):
		print("You take a swig of a concoction made of Red Bull, Monster, Coffee, cola, and liquified cocaine.")
		time.sleep(1)
		if self.energy+20 >=100:
			print("Your energy increases to 100 points.")
		else:
			self.energy+=20
			print("Your energy increases 20 points. ")
			time.sleep(0.5)
			print("**BURRRRP**")



class History(Major):
	def __init__(self, name):
		self.moves={'Craft Paper':ResearchCraft, 
					'Flintlock':Flintlock, 
					'Trivia':Trivial, 
					'Time Travel':Timeshift}
		self.multipliers=Major.multipliers.copy()
		self.multipliers.update(MCB=2, EECS=.5)

	def ResearchCraft(self, enemy):
		energycost=30
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		self.energy-=energycost
		print(self.name,"crafted a research paper!")
		time.sleep(1)
		print("RESEARCH THIS")
		time.sleep(1)
		#enemy.hp-=int(.75*self.atk*self.multipliers[enemy.major])-enemy.defense
		dmg=int(.75*self.atk*self.multipliers[enemy.Major])-enemy.defense
		print(enemy.name, "doesn't understand this...took", dmg, "damage!")
		time.sleep(1)
		enemy.hp-=dmg
	
	def Trivial(self, enemy):
		energycost=5
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		self.energy-=energycost
		print("'Did you know that the tenth President of the United States has two living grandsons today?'")
		dmg=int(.25*self.atk*self.multipliers[enemy.Major])-enemy.defense
		time.sleep(1)
		print(enemy.name, "'s mind was blown for", dmg, "damage!")
		time.sleep(1)
		enemy.hp-=dmg

	def Timeshift(self, enemy):
		energycost=50
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		self.energy-=energycost
		print("You're at the Battle Stalingrad!")
		time.sleep(1)
		dmg=int(self.atk*(enemy.hp/enemy.maxhp)*self.multipliers[enemy.Major])-enemy.defense
		print(enemy.name, "was caught in crossfire for",dmg,"damage!")
		time.sleep(1)
		enemy.hp-=dmg
	def Flintlock(self, enemy):
		energycost=20
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		self.energy-=energycost
		print(self.name, "shoots", enemy.name,"!" )
		time.sleep(1)
		dmg=int(.60*self.atk*self.multipliers[enemy.Major])-enemy.defense
		print(enemy.name, "bled for", dmg, "damage!")
		time.sleep(1)
		enemy.hp-=dmg



class MCB(Major):
	def __init__(self, name):
		self.moves={'Point Mutation': PointMutation, 
					'Set Curve':SetCurve, 
					'Photosynthesis':Photosynthesis,
					'Mitosis':Mitosis}
		self.multipliers=major.multipliers.copy()
		self.multipliers.update(History=.5, Haas=2)

	def PointMutation(self,enemy):
		energycost = 50
		if self.energy > energycost:
			print(energy.name+" was too tired to do that!")
		print(self.name+" used Point Mutation!")
		print(self.name+" grows an extra arm and punches you square in the face.")
<<<<<<< HEAD
		print("Your health decreases to " +str(enemy.hp-10)+" points.")
		enemy.atk+=5
		enemy.hp-=10
		print(self.name+"'s attack increases to "+str(enemy.atk)+" points.")
=======
		dmg=int(0.70*self.atk*self.multipliers[enemy.Major])-enemy.defense
		print("Your health decreases"+str(dmg)+" points.")
		enemy.atk+=5
		print(self.name+"'s attack increases 5 points.")
>>>>>>> b4a57f9cae1937b3045d666b8b8ec70b58b04d5d
		self.energy-=30

	def SetCurve(self,enemy):
		energycost = 40
		if self.energy > energycost:
			print(energy.name+" was too tired to do that!")
		print(self.name+" sets the curve!")
		time.sleep(1)
		print('"That test was so easy. I barely even studied."')
		time.sleep(1)
		enemy.energy-=5
		dmg=int(0.70*self.atk*self.multipliers[enemy.Major])-enemy.defense
		e.dmg=int(0.50*self.atk*self.multipliers[enemy.Major])-enemy.defense
		self.energy-=20
		print("Your esteem is lowered, and your health decreases "+str(dmg)+" points and your energy decreases "+str(e.dmg)+" points.")

	def Photosynthesis(self,enemy):
		print(self.name+" used Photosynthesis!")
		time.sleep(1)
		print(self.name+" unfolded his leaves and soaks up the incredible energy from the sun.")
		time.sleep(1)
		self.energy+=20
		print(self.name+"'s energy increases 20 points. How stellar!")

	def Mitosis(self,enemy):
		energycost=30
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		print(self.name+" undergoes Mitosis!")
		time.sleep(1)
		print('"Ho-ho! My defenses are now double!!"')
		time.sleep(1)
		if self.defense == 0:
			self.defense = 2
		else:
			self.defense*=2
		self.energy-=30
		print(self.name+"'s defense skyrockets to "+str(self.defense)+" points.")
		print(self.name+"'s energy falters 30 points.")

class Haas(Major):
	def __init__(self, name):
		self.moves={'Business Plan': BPlan, 
					'Brag':Brag, 
					'Analyze': Analy, 
					'Glare':Glare}
		self.multipliers=major.multipliers.copy()
		self.multipliers.update(MCB=.5, EECS=2)
	def BPlan(self, enemy):
		energycost=30
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		self.energy-=energycost
		print(self.name, "presents their startup idea!")
		time.sleep(1)
		print('...')
		time.sleep(2)
		dmg=int(.75*self.atk*self.multipliers[enemy.Major])-enemy.defense
		print("It's too good to be true!", enemy.name, "takes", dmg, "damage!")
		enemy.hp-=dmg
	def Brag(self, enemy):
		energycost=15
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		self.energy-=energycost
		print("'I got job offers from ALL of the Big Four! fufufufu")
		time.sleep(1)
		dmg=int(.5*self.atk*self.multipliers[enemy.Major])-enemy.defense
		print(enemy.name, "'s self esteem was hurt for", dmg, "damage!")
		time.sleep(1)
		enemy.hp-=dmg
	def Analy(self, enemy):
		energycost=10
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		self.energy-=energycost
		dmg=int(.25*self.atk*self.multipliers[enemy.Major])-enemy.defense
		print(self.name, "exposed", enemy.name, "'s financial flaws for", dmg, "damage!")
		time.sleep(1)
		enemy.hp-=dmg
	def Glare(self, enemy):
		energycost=5
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		self.energy-=energycost
		dmg=int(.12*self.atk*self.multipliers[enemy.Major])-enemy.defense
		print(self.name, "glared at", enemy.name, "for ", dmg, "damage!")
		time.sleep(1)
		enemy.hp-=dmg

