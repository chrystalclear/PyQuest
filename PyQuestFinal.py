"""
Contents:
1) MAIN
2) CLASSES
3) INITIALIZATIONS
4) MAJORS
5) PLOT
6) SELECTORS
"""
import random
########## MAIN ##########

#Starts the game, gets the Player's name
def main():
	init_enemies()
	init_encounters()
	init_items()
	init_locations()

	char_name = input('What is your name? ')
	player = Player(char_name, locations[0])
	print('Well hello, ' + player.name + '.\n')
	print(ALL_DIALOGUES['start'])
	game(player)

#Gameplay Function where everything happens
def game(player):
	while not GAME_END:
		init_enemies(player.floor)
		location_report(player)
		print('Type help for available commands\n')
		action = input('What would you like to do? ')
		print()
		parse_input(player, action)
	if GAME_END:
		print("You successfully passed Hilfinger's class....with a C-!")

def parse_input(player, action):
	if action == "help":
		print("""Type these commands without quotes! Mind case please!
'advance' : Attempt to get to the next floor. Be careful of fellow students!\n
'stats' : See your stats. 
'items' : See your inventory.
'help' : See this message again!
'location': See where you are""") 
	elif action == "advance":
		advance(player)
	elif action == "stats":
		display_stats(player)
	elif action == "items":
		print("Functionality doesn't exist yet! Patience!")
	elif action== "location":
		print(player.place)
	else:
		print("Invalid command")
		time.sleep(1)
		

def run_battle(player, enemy, win = False, lose = False):
	while not win and not lose:
		display_stats(player)
		display_stats(enemy)
		try:
			print('available moves' + str(list(player.moves.keys())) + '\t')
			player.get(input())(player, enemy)
		except KeyError:
			print('\ninvalid command!')
			continue
		display_stats(player)
		display_stats(enemy)
		time.sleep(1)
		if player.hp <=0:
			lose=True
		if enemy.hp<=0:
			win=True
			enemy.hp=float(enemy.max_hp)
			player.hp=100
			print(player.name+' won!')
		if not win and not lose:
			enemy.get(random.choice(list(enemy.moves.keys())))(enemy, player)	
			if player.hp <=0:
					lose=True
			if enemy.hp<=0:
					win=True
					enemy.hp=float(enemy.max_hp)
					player.hp=100
		if enemy.energy+10>=100:
			enemy.energy=100
		else:
			enemy.energy+=10
		if player.energy+10>=100:
			player.energy=100
		else:
			player.energy+=10
	if win == True:
		win = False
	elif lose == True:
		player.location.place = 0
		lose = False

	player.hp, player.energy, enemy.hp, enemy.energy = 100, 100, 100, 100


def display_stats(character):
	print('\n'+character.name + ': ' + character.major + '\n')
	print('HP: ' + str(character.hp) + '/' + str(character.max_hp))
	print('ENERGY: ' + str(character.energy) + '/' + str(character.max_energy )) 
	print('ATTACK: ' +str(character.atk))
	print('DEFENSE: ' + str(character.defense) )



########## CLASSES ##########

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
		else:
			return self.moves[action]

class Soda(Location):
	def __init__(self, name, floor, place=0):
		Location.__init__(self, name)
		self.floor = floor
		self.place = place

########## INITIALIZATIONS ##########

enemies, encounters, items, locations = [], [], [], []

#Initialization
def init_enemies(floor = 3):
	if floor < 7:
		enemy0 = Enemy("Enemy", random_major())
		enemy1 = Enemy("Enemy", random_major())
		boss = Enemy("Boss", random_major(), True)
		enemies.extend([enemy0, enemy1, boss])
	elif level == 7:
		boss0 = Enemy("Final Boss", "MCB")
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
		Major.__init__(self, name)
		self.multipliers.update(EECS=.5, Haas=2, History=.5)
	
	def InfiniteRecursion(self,enemy):
		energycost = 50
		if self.energy < energycost:
			print(self.name, " is too tired to do that! Rack up some energy by taking some Hackathon Fuel.")
			return 
		i=0
		while i<40:
			print ("Enemy takes 1 point damage")
			enemy.hp -= 1
			i+=1 
		print("Stack overflow. Maximum recursion depth reached. Opponent "+enemy.name+" has crashed.")
		self.energy-=50
		time.sleep(1)
		print(self.name+"'s energy decreases 50 points. Recursion indefinitely is incredibly tiring.")
		time.sleep(1)

	def AbstractionBarrier(self,enemy):
		print(self.name+" creates an abstraction barrier between "+self.name+" and "+enemy.name+".")
		energycost=5
		if self.energy < energycost:
			print(self.name, " is too tired to do that! Rack up some energy by taking some Hackathon Fuel.")
			return 
		self.defense+=5
		self.energy-=5
		time.sleep(1)
		print(self.name+"'s Abstraction Shield makes "+self.name+" feel safe. "+self.name+"'s defense increases 5 points.")
		print(self.name+"'s energy decreases 5 points.")
		time.sleep(1)

	def Pop(self,enemy):
		energycost = 10
		if self.energy < energycost:
			print(self.name, " is too tired to do that! Rack up some energy by taking some Hackathon Fuel.")
			return 
		dmg =int(1.25*self.atk*self.multipliers[enemy.major])-enemy.defense
		print(self.name+" pops off",dmg,"of "+enemy.name+"'s health points.")
		enemy.hp-=dmg
		self.energy-=energycost
		time.sleep(1)
		print(self.name+"'s energy drops down 10 points. Popping is hard work.")
		time.sleep(1)

	def HackathonFuel(self,enemy):
		print("You take a swig of a concoction made of Red Bull, Monster, Coffee, cola, and liquified cocaine.")
		time.sleep(1)
		self.hp-=5
		if self.energy+30 >=100:
			print(self.name+"'s energy increases to 100 points.")
		else:
			self.energy+=30
			print(self.name+"'s energy increases 30 points.")
			print("However, "+self.name+"'s health decreases by 5 points. Don't do drugs, children!")
			time.sleep(1)
			print("**BURRRRP**")
			time.sleep(.5)
	moves={'Infinite Recursion':InfiniteRecursion,
     'Abstraction Barrier':AbstractionBarrier,
     'Pop': Pop,
     'Hackathon Fuel': HackathonFuel }



class History(Major):
	def __init__(self, name):
		Major.__init__(self, name)
		self.multipliers.update(MCB=2, EECS=2)

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
		dmg=int(.75*self.atk*self.multipliers[enemy.major])-enemy.defense
		print(enemy.name, "doesn't understand this...took", dmg, "damage!")
		time.sleep(1)
		enemy.hp-=dmg
	
	def Trivial(self, enemy):
		energycost=5
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		self.energy-=energycost
		print("'Did you know that the tenth President of the United States has two living grandsons today?'")
		dmg=int(.25*self.atk*self.multipliers[enemy.major])-enemy.defense
		time.sleep(1)
		print(enemy.name, "'s mind was blown for", dmg, "damage!")
		time.sleep(1)
		enemy.hp-=dmg

	def Timeshift(self, enemy):
		energycost=50
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		self.energy-= energycost
		print(self.name, "used TIME TRAVEL!")
		time.sleep(1)
		print("You're at the Battle Stalingrad!")
		time.sleep(1)
		dmg=int(self.atk+(1+(enemy.hp/enemy.max_hp))*self.multipliers[enemy.major])-enemy.defense
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
		dmg=int(.60*self.atk*self.multipliers[enemy.major])-enemy.defense
		print(enemy.name, "bleeds for", dmg, "damage!")
		time.sleep(1)
		enemy.hp-=dmg
	moves={'Craft Paper':ResearchCraft,
     'Flintlock':Flintlock,
     'Trivia':Trivial,
     'Time Travel':Timeshift}




class MCB(Major):
	def __init__(self, name):
		Major.__init__(self, name)
		self.multipliers.update(History=2, Haas=.5, MCB=.5)

	def PointMutation(self,enemy):
		energycost = 50
		if self.energy < energycost:
			print(self.name+" was too tired to do that!")
		print(self.name+" used Point Mutation!")
		print('...')
		time.sleep(.25)
		print(self.name+" grows an extra arm and punches "+enemy.name+" square in the face.")
		time.sleep(1)
		dmg=int(0.70*self.atk*self.multipliers[enemy.major])-enemy.defense
		print("Your health decreases "+str(dmg)+" points.")
		time.sleep(1)
		self.atk+=5
		enemy.hp-=dmg
		print(self.name+"'s attack increases 5 points.")
		time.sleep(1)
		print("...OP.")
		time.sleep(1)
		self.energy-=50

	def SetCurve(self,enemy):
		energycost = 40
		if self.energy < energycost:
			print(enemy.name+" was too tired to do that!")
			return
		print(self.name+" sets the curve!")
		time.sleep(1)
		print('"That test was so easy. I barely even studied."')
		time.sleep(1)
		enemy.energy-=5
		dmg=int(0.70*self.atk*self.multipliers[enemy.major])-enemy.defense
		edmg=int(0.50*self.atk*self.multipliers[enemy.major])-enemy.defense
		self.energy-=40
		enemy.hp-=dmg
		enemy.energy-=edmg
		print(enemy.name+"'s esteem is lowered, and their health decreases "+str(dmg)+" points and"+enemy.name+"'s energy decreases "+str(edmg)+" points.")

	def Photosynthesis(self,enemy):
		print(self.name+" used Photosynthesis!")
		time.sleep(1)
		print(self.name+" unfolded his leaves and soaked up the incredible energy from the sun.")
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
		time.sleep(1)
		print(self.name+"'s energy falters 30 points.")
		time.sleep(1)
	moves={'Point Mutation': PointMutation,
		'Set Curve':SetCurve, 
		'Photosynthesis':Photosynthesis,
		'Mitosis':Mitosis}


class Haas(Major):
	def __init__(self, name):
		Major.__init__(self, name)
		self.multipliers.update(MCB=.5, History=2, Haas=.5)
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
		dmg=int(.75*self.atk*self.multipliers[enemy.major])-enemy.defense
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
		dmg=int(.5*self.atk*self.multipliers[enemy.major])-enemy.defense
		print(enemy.name+ "'s self esteem was hurt for", dmg, "damage!")
		time.sleep(1)
		enemy.hp-=dmg
	def Analy(self, enemy):
		energycost=10
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		self.energy-=energycost
		print(self.name, "uses ANALYSIS!")
		dmg=int(.25*self.atk*self.multipliers[enemy.major])-enemy.defense
		print(self.name, "exposed", enemy.name+ "'s financial flaws for", dmg, "damage!")
		time.sleep(1)
		enemy.hp-=dmg
	def Glare(self, enemy):
		energycost=5
		if self.energy<energycost:
			return str(self.name)+" was too tired to do that!"
		self.energy-=energycost
		dmg=int(.12*self.atk*self.multipliers[enemy.major])-enemy.defense
		print(self.name, "glared at", enemy.name, "for ", dmg, "damage!")
		time.sleep(1)
		enemy.hp-=dmg
	moves={'Business Plan': BPlan,
     'Brag':Brag,
     'Analyze': Analy,
     'Glare':Glare}


class Character(object):
	def __init__(self, name):
		self.name = name
		self.max_hp = 100
		self.hp = 100
		self.max_energy = 100
		self.energy = 100
		self.atk = 25
		self.defense = 0

class Player(Character, EECS):
	def __init__(self, name, location = None, floor = 3, place = 0):
		Character.__init__(self, name)
		Soda.__init__(self, name, floor)
		self.location = location
		self.major = 'EECS'
		self.moves=EECS.moves
		self.floor = floor
		self.multipliers=EECS(Major).multipliers

class Enemy(Character, Major):
	def __init__(self, name, major, boss = False):
		dispatch = {"MCB": MCB, "History": History, "EECS": EECS, "Haas": Haas}
		enemy_major = dispatch[major]
		Character.__init__(self, name)
		enemy_major.__init__(self, name)
		self.moves=enemy_major.moves
		self.major=major
		if boss:
			self.max_hp *= 1.25
			self.hp *= 1.25
			self.atk *= .75


class Encounters(Character):
	def __init__(self, name):
		Character.__init__(self, name)


########## PLOT ##########

ALL_DIALOGUES = {'start': "You are an EECS major at the University of California at Berkeley, and you wake up on a desk after a long, restful nap at the 2nd floor of Soda Hall. Looking around, the room is empty; all that is around is you and your trusty laptop. You must get to the top! Office hours ends soon!\n", 'battle': "START BATTLE"}
GAME_END = False
win = False
lose = False

def advance(player):
	if battle_encounter(player.place):
		whofights(player, player.place)
	else:
		print("It seems too quiet, but the coast is clear!")
	if player.place == 0:
		player.place = 1
	elif player.place == 1:
		player.place = 2
	elif player.place == 2:
		changefloors(player)

def whofights(player,location):
	enemy = enemies[location]
	print("A CHALLENGER APPEARS!")
	time.sleep(2)
	print("BATTLE START!!!")
	time.sleep(1)
	run_battle(player,enemy)

def changefloors(player):
	player.floor += 1
	if player.floor == 7:
		print("As you open the door to the professor's office Hilfinger rotates towards you at his desk. 'I've been waiting for you,", player.name, "let's see if you've improved!")
        sleep.time(4)
        print("You are bombarded by questions!")
		LastBoss()
	player.place = 0
	player.location = locations[player.floor-3] #floor3 is index 0, etc.
	
########## SELECTORS ##########

#Selector function takes in name of location and returns the location object with that name
def get_location(name): #USELESS BECAUSE LIST INDEXING OF LOCATIONS IS MORE EFFICIENT
	for location in locations:
		if location.name == name:
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
		print('You are inside Soda, floor ' + str(player.floor) + ', place ' + str(player.place))

#Encounter chance = 5%
def encounter(place = 0):
	if random.random() < 0.05:
		return True
	return False

def battle_encounter(place = 0):
	if (place<2 and random.random() < 0.5) or place == 2:
		return True
	return False

majors = ["MCB", "Haas", "History", "EECS"]

def random_major():
	return majors[int(random.random() * 4)]


def LastBoss(): 
        def question1(strikes=0):
                if strikes >=3:
                        print( "Hilfinger can no longer take your moronic stupidity. In a fit of rage he clenches his fists, bangs them on the table and screams “You dishonor me! You have dishonored this entire University! I knew by the look of your puny little head that you had a tiny brain to match. You disgust me, and I have no wish to see you any longer. Leave. I reward you an F in my class, and may God have mercy on your soul. \n\t\t THE END")
                        return
                q1 = input('''QUESTION 1:\nEvaluate the following expression written in Scheme:\n
                (+ 1 2 (* 3 5) (- 9 (/ 15 3)) 4)\n>>> ''' ) #26
                if q1 != '26':
                        strikes+=1
                        print("Hilfinger's teeth gnash as his brow furrows and his face reddens.")
                        time.sleep(1)
                        print("This is strike number "+str(strikes)+".\n")
                        time.sleep(1)
                        question1(strikes)
                elif q1 == '26':
                        question2(strikes)
        def question2(strikes):
                if strikes >=3:             
                        print("Hilfinger can no longer take your moronic stupidity. In a fit of rage he clenches his fists, bangs them on the table and screams “You dishonor me! You have dishonored this entire University! I knew by the look of your puny little head that you had a tiny brain to match. You disgust me, and I have no wish to see you any longer. Leave. I reward you an F in my class, and may God have mercy on your soul.\nTHE END")
                        time.sleep(20)
                        return exit()


                q2 = input('''QUESTION 2:\ndef fn(x):
        prev,curr=4,3
        for _ in range(n-1):
                prev,curr = curr, prev+curr+4
        return curr
Define a simple mathematical function f(n) such that 
evaluating fn(x) with x=n performing theta(f(n)) 
function calls. Leave out constants.\n>>> ''' ) 
                if q2 != "n":
                        strikes+=1
                        print("Hilfinger's teeth gnash as his brow furrows and his face reddens.")
                        time.sleep(1)
                        print("This is strike number "+str(strikes)+".\n")
                        time.sleep(1)
                        question2(strikes)
                else:
                        question3(strikes)

        def question3(strikes):
                if strikes >=3:
                        print("Hilfinger can no longer take your moronic stupidity. In a fit of rage he clenches his fists, bangs them on the table and screams “You dishonor me! You have dishonored this entire University! I knew by the look of your puny little head that you had a tiny brain to match. You disgust me, and I have no wish to see you any longer. Leave. I reward you an F in my class, and may God have mercy on your soul.")
                        time.sleep(20)
                        return exit()


                q3 = input('''QUESTION 3:\n>>> sequence=[11,13,15,12,14,16]
>>> summer=(sum((k-5) for k in sequence if ((k%7) >= 2)))
>>> print(summer)\nWhat will be printed?\n>>> ''' ) 
                if q3 != '32':
                        strikes+=1
                        
                        print("Hilfinger's teeth gnash as his brow furrows and his face reddens.")
                        time.sleep(1)
                        print("This is strike number "+str(strikes)+".\n")
                        time.sleep(20)
                        question3(strikes)
                else:

                        print("As you stand proudly looking out the window of Soda Hall you feel a strangely familiar hand on your shoulder, and Hilfinger comments, 'Good job kid, I know you had the smarts to do it,' somehow that hits you right in the feels and you heart starts beating faster. This is it. This is what you've been working for. You are a master of Introductory Python. You did it. We did it. Congratulations. A winner is you.\n\t\t\tTHE END")
                        time.sleep(20)
                        return exit()
        return question1(0)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('|                                                         |')
print('|                  Welcome, to PoCALmon!                  |')
print('|                    Enjoy your stay!                     |')
print('|                                                         |')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
time.sleep(2)
main()