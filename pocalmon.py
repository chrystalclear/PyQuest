"""
Contents:
1) MAIN
2) CLASSES
3) INITIALIZATIONS
4) MAJORS
5) PLOT
6) SELECTORS
"""

########## MAIN ##########

#Starts the game, gets the Player's name
def start():
	init_enemies()
	init_encounters()
	init_items()
	init_locations()

	char_name = input('What is your name? ')
	player = Player(char_name, get_location("Dorm"))
	print('Well hello, ' + player.name + '.\n')
	print(ALL_DIALOGUES['start'])
	main(player)

#Main Function where everything happens
def main(player):
	while not GAME_END:
		location_report(player)
		print('Type help for available commands\n')
		print('You have cleared ' + player.floor + ' floors.')
		action = input('What would you like to do? ')
		parse_input(player, action)
	if GAME_END:
		print("You successfully passed Hilfinger's class....with a C-!")

def parse_input(player, action):
	return 0 #Change later


def run_battle(player, enemy):
	win=False
	lose=False
	while not win and not lose:
		display_stats(player)
		display_stats(enemy)
		player.get(input('available moves:'+str(list(player.moves.keys()))))
		display_stats(player)
		display_stats(enemy)
		time.sleep(1)
	if player.hp <=0:
		lose=True
	if enemy.hp<=0:
		win=True
	if not win and not lose:
		enemy.get(random.choice(list(enemy.moves.keys())))	
		if player.hp <=0:
			lose=True
		if enemy.hp<=0:
			win=True

def display_stats(character):
	print(character.name + ':')
	print('HP: ' + str(character.hp) + '/' + str(character.max_hp))
	print('ENERGY: ' + str(character.energy) + '/' + str(character.max_energy )) 
	print('ATTACK: ' +str(character.atk))
	print('DEFENSE: ' + str(character.defense) )


########## CLASSES ##########

class Character(object):
	def __init__(self, name):
		self.name = name
		self.max_hp = 100
		self.hp = 100
		self.max_energy = 100
		self.energy = 100
		self.atk = 25
		self.defense = 0

class Item(object):
	def __init__(self, name, role, increase):
		self.name = name
		self.role = role
		self.increase = increase

class Location(object):
	def __init__(self, name):
		self.name = name

class Major(object):
	def __init__(self, name):
		self.moves={}
		self.multipliers={'History': 1, 'MCB': 1, 'Haas': 1, 'EECS': 1}

	def get(self, action):
		if action=='list':
			print(self.moves.keys())
		return self.moves[action]

class Soda(Location):
	def __init__(self, name, floor):
		Location.__init__(self, name)
		self.floor = floor
		self.tile = 0

class Player(Character, Location):
	def __init__(self, name, location=0, floor=3):
		Character.__init__(self, name)
		self.name=self.name.name
		self.location = location
		self.floor = floor
		major='EECS'
		EECS.__init__(self, 'EECS')
class Enemy(Character, Major):
	def __init__(self, name, major):
		Character.__init__(self, name)
		self.moves=getattr(Major, 'moves')
		self.major=major
		self.name=self.name.name

class Encounters(Character):
	def __init__(self, name):
		Character.__init__(self, name)

########## INITIALIZATIONS ##########

enemies, encounters, items, locations = [], [], [], []

#Initialization
def init_enemies(level = 3):
	if level == 3:
		print(level)
	if level == 4:
		print(level)
	if level == 5:
		print(level)
	if level == 6:
		print(level)
	if level == 7:
		boss0 = Enemy("Boss0", "MCB")
		enemies.extend([boss0])
	else:
		print("You dirty cheater! Automatic Failure!")
		GAME_END = True

def init_encounters():
	friend0 = Encounters("Friend A")
	encounters.extend([friend0])

def init_items():
	item0 = Item("Fruit", "HP", "25")
	item1 = Item("5-hour energy", "Energy", "25")
	items.extend([item0, item1])

def init_locations():
	floor3 = Soda("Soda", 3)
	floor4 = Soda("Soda", 4)
	floor5 = Soda("Soda", 5)
	floor6 = Soda("Soda", 6)
	floor7 = Soda("Soda", 7)
	locations.extend([floor3, floor4, floor5, floor6, floor7])

########## MAJORS ##########

import time

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
			return 
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
		print("Your Abstraction Shield makes you feel safe. Your defense increases 2 points.")
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
		self.health-=5
		if self.energy+20 >=100:
			print("Your energy increases to 100 points.")
		else:
			self.energy+=20
			print("Your energy increases 20 points.")
			print("However, your health decreases by 5 points. Don't do drugs, children!")
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
		print(self.name, "used TIME TRAVEL!")
		time.sleep(1)
		print("You're at the Battle Stalingrad!")
		time.sleep(1)
		dmg=int(self.atk*(1+(enemy.hp/enemy.maxhp))*self.multipliers[enemy.Major])-enemy.defense
		print(enemy.name, "was caught in crossfire for",dmg,"damage!")
		time.sleep(1)
		enemy.hp-=dmg
	def Flintlock(self, enemy):
		energycost=20
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		self.energy-=energycost
		print(self.name, "draws a flintlock pistol!")
		time.sleep(1)
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
		dmg=int(0.70*self.atk*self.multipliers[enemy.Major])-enemy.defense
		print("Your health decreases"+str(dmg)+" points.")
		enemy.atk+=5
		print(self.name+"'s attack increases 5 points.")
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
		print(self.name, "uses BUSINESS PLAN!")
		time.sleep(1)
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
		print(self.name, "uses BRAG!")
		time.sleep(1)
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
		print(self.name, "uses ANALYSIS!")
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



########## PLOT ##########

ALL_DIALOGUES = {'start': "You are an EECS major at the University of California at Berkeley, and you wake up on a desk after a long, restful nap at the 2nd floor of Soda Hall. Looking around, the room is empty; all that is around is you and your trusty laptop.", 'battle': "START BATTLE"}
GAME_END = False
win = False
lose = False


########## SELECTORS ##########

#Selector function takes in name of location and returns the location object with that name
def get_location(name, floor = None):
	for location in locations:
		if location.name == name and floor == None:
			return location
		elif floor:
			if location.name == name and location.floor == floor:
				return location
	return None

#Gets enemy object by it's name
def get_enemy(name):
    for enemy in enemies:
    	if enemy.name == name:
    		return enemy
    return None

#Prints the location of the player
def location_report(player):
	if player.location.name == "Campanile":
		print('You are at the Campanile')
	elif player.location.name == "Dorm":
		print('You are inside your dorm')
	elif player.location.name == "Outside":
		print('You are outside')
	elif player.location.name == "Soda":
		print('You are inside Soda, floor ' + player.location.floor)

#Encounter chance = 5%
#def encounter(place = 0):
#	if place random.random() < 0.05:
#		return True
#	return False

start()
