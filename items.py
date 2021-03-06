class QuestItem:
    def __init__(self):
        raise NotImplementedError("Do not create raw quest items!")

    def __str__(self):
        return self.name


class SmallCoin(QuestItem):
    def __init__(self):
        self.name = "Small coin"
        self.description = " A small coin with three runes inscribed upon it"
        self.value = 1


class WoodenKey(QuestItem):
    def __init__(self):
        self.name = "Key"
        self.description = " A small wooden key carved from the heart of a tree..."
        self.value = 1


############################################################################
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Fist(Weapon):
    def __init__(self):
        self.name = "Fist"
        self.description = " Your fists, idiot"
        self.damage = 1
        self.value = 0.5


class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = " A fist-sized rock, suitable for bludgeoning."
        self.damage = 5
        self.value = 1


class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = " A small dagger with some rust.\nSomewhat more dangerous than a rock"
        self.damage = 10
        self.value = 25


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = " This sword is showing it's age.\nBut still has some fight in it"
        self.damage = 20
        self.value = 250


class IronSword(Weapon):
    def __init__(self):
        self.name = "Iron Sword"
        self.description = " A sturdy Iron Sword"
        self.damage = 30
        self.value = 400
        

##############################################################################
class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.description = " A loaf of crusty bread"
        self.healing_value = 10
        self.value = 10


class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.description = ' A disgusting tasting potion that restores some health'
        self.healing_value = 50
        self.value = 60


class ManaPotion(Consumable):
    def __init__(self):
        self.name = "Mana Potion"
        self.description = " An even fouler concoction that restores some mana"
        self.mana_value = 50
        self.value = 120


class Apple(Consumable):
    def __init__(self):
        self.name = "Apple"
        self.description = " A simple apple"
        self.healing_value = 5
        self.value = 5
########################################################################


class Armor:
    def __init__(self):
        raise NotImplementedError("Do not create raw Armor objects.")

    def __str__(self):
        return "{} (+{} Armor)".format(self.name, self.defence_value)


class LeatherArmor(Armor):
    def __init__(self):
        self.name = "Leather armor"
        self.description = " Soft leather armor"
        self.defence_value = 5
        self.value = 150


class WoodenShield(Armor):
    def __init__(self):
        self.name = "Wooden Shield"
        self.description = " A simple wooden shield"
        self.defence_value = 1
        self.value = 15


class IronArmor(Armor):
    def __init__(self):
        self.name = "Iron Armor"
        self.description = " Sturdy Iron Armor"
        self.defence_value = 8
        self.value = 250


class IronShield(Armor):
    def __init__(self):
        self.name = "Iron Shield"
        self.description = " A sturdy Iron Shield"
        self.defence_value = 6
        self.value = 200

#################################################
class Valuable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Armor objects.")

    def __str__(self):
        return "{} {}".format(self.name, self.value)


class Jewel(Valuable):
    def __init__(self):
        self.name = 'Jewel'
        self.description = " A valuable jewel"
        self.value = 1500

############################################################
class MagicalItem:
    def __init__(self):
        raise NotImplementedError("Do not create raw MagicalItem objects.")

    def __str__(self):
        return "{}".format(self.name)


class WoodenStaff(MagicalItem):
    def __init__(self):
        self.name = "Wooden Staff"
        self.description = " A sturdy wooden staff, it hums with a small amount of energy."
        self.magic_value = 15
        self.value = 100


class StickWand(MagicalItem):
    def __init__(self):
        self.name = "Stick Wand"
        self.description = " A small stick that hisses with a tiny amount of energy."
        self.magic_value = 5
        self.value = 10


class IronStaff(MagicalItem):
    def __init__(self):
        self.name = "Iron Staff"
        self.description = " A sturdy Iron Staff that hums with a large amount of energy"
        self.magic_value = 15
        self.value = 350


class FabledWand(MagicalItem, QuestItem):
    def __init__(self):
        self.name = "Fabled Wand"
        self.description = " A legendary wand that has immense power"
        self.magic_value = 25
        self.value = 1
