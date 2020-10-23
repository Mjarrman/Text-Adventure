import items
class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.gold = 500
        self.inventory = [items.CrustyBread(),
                          items.CrustyBread(),
                          items.CrustyBread(),
                          items.HealingPotion(),
                          items.RustySword(),
                          items.LeatherArmor(),
                          items.IronArmor(),
                          items.IronSword(),
                          items.IronShield(),
                          items.WoodenStaff()]
