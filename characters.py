#Starts the game, gets the Player's name
def start():
	init_characters()
	#init_items()

	print('--Beginning Story--')
	char_name = input('What is your name? ')
	player = Player(char_name)
	print('Well hello, ' + player.name + '.')
	main(player)

characters, items = [], []

#Initialize all characters
def init_characters():
	boss0 = Enemy("Boss0", "MCB")
	characters.extend([boss0])

def init_items():
	item0 = Item("Fruit", "HP", "25")
	item1 = Item("5-hour energy", "Energy")
	items.extend([item0, item1])

#Main Function where everything happens
def main(player):
	print('')

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

class Player(Character):
	def __init__(self, name):
		Character.__init__(self, name)

class Enemy(Character, Major):
	def __init__(self, name, major):
		Character.__init__(self, name)
		Major.__init__(self, major)

start()