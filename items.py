# Items module
# Contains classes for all items used in the game, like weapons and consumables

# Weapons
class Weapon:
	"""
	Basic weapon class

	Provides names, descriptions, damage per attack, and sale value of the different weapons.
	"""
    def __init__(self):
        raise NotImplementedError

    def __str__(self):
        return self.name

class Stick(Weapon):
	def __init__(self):
		self.name = "Stick"
		self.description = "A fallen branch from a nearby tree. Could be used like a sword in a pinch."
		self.damage = 3
		self.value = 1

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock. Great for hitting things."
        self.damage = 5
        self.value = 1

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small, sharp dagger, favored by bandits or thieves because of its easily concealed size." 
        self.damage = 15
        self.value = 30

class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "A rusty long sword. Since its edge is significantly dulled, it's best use is probably to blugeon something."
        self.damage = 15
        self.value = 50

class Axe(Weapon):
    def __init__(self):
        self.name = "Axe"
        self.description = "An axe whose original purpose was to chop trees. While it is small, it should be sharp enough to do some damage when it hits a target."
        self.damage = 25
        self.value = 80

class Bow(Weapon):
    def __init__(self):
        self.name = "Bow"
        self.description = "An austere longbow. While it lacks the finesse or ornamentation of common ceremonial bows, it appears to have been a reliable hunter's bow for years in this forest."
        self.damage = 40
        self.value = 120

class LongSword(Weapon):
	def __init__(self):
		self.name = "Long Sword"
		self.description = "A sharp long sword. It would take someone strong to wield it effectively, but should cut through nearly anything it hits."
		self.damage = 60
		self.value = 200

# Consumables
class Consumable:
	"""
	Basic consumable class

	Provides names, healing value, and sale value of the different consumable item.
	"""
    def __init__(self):
        raise NotImplementedError

    def __str__ (self):
        return "{} (+{} HP)".format(self.name, self.healing_value)

class Berries(Consumable):
	def __init__(self):
		self.name = "Berries"
		self.healing_value = 10
		self.value = 12

class Mushrooms(Consumable):
	def __init__(self):
		self.name = "Mushrooms"
		self.healing_value = 8
		self.value = 5

class Toadstools(Consumable):
	def __init__(self):
		self.name = "Toadstools"
		self.healing_value = -10
		self.value = 10

class Potion(Consumable):
	def __init__(self):
		self.name = "Potion"
		self.healing_value = 100
		self.value = 150


if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")
