import random


class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

# Damage Modifier ###################


def determine_determine_damage(self):
    damage = random.randint(self.min_damage, self.max_damage)
    hit_test = random.randint(0,100)
    if hit_test > self.hit_pct:
        return damage
    else:
        return 0

# Loot ###################################
def loot(self, player_inventory):
    loot_item = 
    loot = random.randint(0, 100)
    loot_test = self.loot_pct
    if loot_test < loot:
        print("The", self.name, "has dropped some loot!")
        player_inventory.append(loot_item)

# Enemy Classes ######################
class BatColony(Enemy):
    def __init__(self):
        self.name = "Colony of bats"
        self.hp = 50
        self.loot_pct = 20
        self.min_damage = 4
        self.max_damage = 8
        self.hit_pct = 80
        self.damage = determine_determine_damage(self)
        self.loot = loot()


class GiantSpider(Enemy):
    def __init__(self):
        self.name = "Giant Spider"
        self.hp = 10
        self.loot_pct = 10
        self.min_damage = 4
        self.max_damage = 8
        self.hit_pct = 80
        self.damage = determine_determine_damage(self)
        self.loot = loot()


class Ogre(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 30
        self.loot_pct = 45
        self.min_damage = 5
        self.max_damage = 8
        self.hit_pct = 80
        self.damage = determine_determine_damage(self)
        self.loot = loot()


class RockMonster(Enemy):
    def __init__(self):
        self.name = "Rock Monster"
        self.hp = 50
        self.loot_pct = 50
        self.min_damage = 6
        self.max_damage = 8
        self.hit_pct = 70
        self.damage = determine_determine_damage(self)
        self.loot = loot()


class BlackKnight(Enemy):
    def __init__(self):
        self.name = "Black knight"
        self.hp = 60
        self.loot_pct = 50
        self.min_damage = 8
        self.max_damage = 10
        self.hit_pct = 70
        self.damage = determine_determine_damage(self)
        self.loot = loot()


class HulkingBeast(Enemy):
    def __init__(self):
        self.name = "Hulking Beast"
        self.hp = 200
        self.loot_pct = 60
        self.min_damage = 10
        self.max_damage = 12
        self.hit_pct = 60
        self.damage = determine_determine_damage(self)
        self.loot = loot()
