import random

#Starts the game, gets the Player's name
def start():
	init_enemies()
	init_encounters()
	init_items()
	init_locations()

	print('--Beginning Story--')
	char_name = input('What is your name? ')
	player = Player(char_name, location("Dorm"))
	print('Well hello, ' + player.name + '.\n')
	main(player)

enemies, encounters, items, locations = [], [], [], []

#Initialization
def init_enemies():
	boss0 = Enemy("Boss0", "MCB")
	enemies.extend([boss0])

def init_encounters():
	friend0 = Encounters("Friend A")

def init_items():
	item0 = Item("Fruit", "HP", "25")
	item1 = Item("5-hour energy", "Energy", "25")
	items.extend([item0, item1])

def init_locations():
	campanile = Location("Campanile")
	dorm = Location("Dorm")
	outside = Location("Outside")
	floor1 = Soda("Soda", 1)
	floor2 = Soda("Soda", 2)
	floor3 = Soda("Soda", 3)
	floor4 = Soda("Soda", 4)
	floor5 = Soda("Soda", 5)
	floor6 = Soda("Soda", 6)
	locations.extend([campanile, dorm, outside, floor1, floor2, floor3, floor4, floor5, floor6])

#Main Function where everything happens
def main(player):
	location_report(player)
	print('Type help for available commands\n')
	action = input('What would you like to do? ')
	parse_input(action)

def parse_input(action):
	return 0 #Change later

#Selector function takes in name of location and returns the location object with that name
def location(name, floor = None):
	for location in locations:
		if location.name == name and floor == None:
			return location
		elif floor:
			if location.name == name and location.floor == floor:
				return location
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
def encounter():
	if random.random() < 0.05:
		return True

#Classes for Character, Major, Item, Player, Enemy
class Character(object):
	def __init__(self, name):
		self.name = name
		self.max_hp = 100
		self.hp = 100
		self.max_energy = 100
		self.energy = 100
		self.atk = 25
		self.defense = 0
		self.spd = 0

class Major(object):
	def __init__(self, major):
		self.major = major

class Item(object):
	def __init__(self, name, role, increase):
		self.name = name
		self.role = role
		self.increase = increase

class Location(object):
	def __init__(self, name):
		self.name = name

class Soda(Location):
	def __init__(self, name, floor):
		Location.__init__(self, name)
		self.floor = floor

class Player(Character, Location):
	def __init__(self, name, location = None):
		Character.__init__(self, name)
		self.location = location

class Enemy(Character, Major):
	def __init__(self, name, major):
		Character.__init__(self, name)
		Major.__init__(self, major)

class Encounters(Character):
	def __init__(self, name):
		Character.__init__(self, name)

start()