# NPC module
# Classes for Non playable characters, like a merchant or blacksmith

import items

# NPC class
class NPC():
	"""
	Basic class for non-playable character
	Either a merchant or blacksmith

	Attributes are name, gold on hand, and inventory of items to sell
	"""
	def __init__(self):
		raise NotImplementedError

	def __str__(self):
		return self.name

class Merchant(NPC):
	def __init__(self):
		self.name = "Merchant"
		self.gold = 200
		self.inventory = [items.Berries(), items.Mushrooms(), items.Potion()]

# lower quality merchant
class BadMerchant(NPC):
	def __init__(self):
		self.name = "Merchant"
		self.gold = 80
		self.inventory = [items.Berries(), items.Mushrooms(), items.Toadstools()]

class Blacksmith(NPC):
	def __init__(self):
		self.name = "Blacksmith"
		self.gold = 120
		self.inventory = [items.Dagger(), items.Bow(), items.LongSword()]

# Lower quality blacksmith
class BadBlacksmith(NPC):
	def __init__(self):
		self.name = "Blacksmith"
		self.gold = 100
		self.inventory = [items.Dagger(), items.RustySword(), items.Axe()]
