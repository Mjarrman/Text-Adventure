import items
import world
from inventory import get_inventory


class Player:

    def __init__(self):
        self.inventory = get_inventory()
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 100
        self.gold = 100
        self.victory = False
        self.defence = 1
        self.mana = 100

    def return_inventory(self):
        return self.inventory

    def update_inventory(self, new_inventory):
        self.inventory = new_inventory

    def is_alive(self):
        return self.hp > 0

    def print_map(self):

        for y_line in range(9):
            for x_line in range(11):
                if self.x == x_line and y_line == self.y:
                    print(" #", end="")
                elif (x_line == 7 and y_line == 5) or (x_line == 7 and y_line == 6) or (
                        x_line == 7 and y_line == 7) or (x_line == 7 and y_line == 8) or (
                        x_line == 8 and y_line == 5) or (x_line == 10 and y_line == 5):
                    print(" ⌂", end="")
                else:
                    print(" |", end="")

            print("")

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item) + ',' + str(item.description))
        print("Gold: {}".format(self.gold))

    def equip(self):
        armor = [item for item in self.inventory if isinstance(item, items.Armor)]
        if not armor:
            print("You don't have anything to equip!")
            return
        for i, item in enumerate(armor, 1):
            print("Choose something to equip: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_equip = armor[int(choice) - 1]
                self.defence = min(200, self.defence + to_equip.defence_value)
                self.inventory.remove(to_equip)
                print("Current defence: {}".format(self.defence))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    def regen_mana(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any items to charge your mana!")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to charge your mana: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_charge = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_charge.mana_value)
            except AttributeError:
                print("This item has no mana value")
                self.inventory.remove(to_charge)
                print("Current Mana: {}".format(self.mana))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    def most_magical_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.magic_value > max_damage:
                    best_weapon = item
                    max_damage = item.magic_value
            except AttributeError:
                pass

        return best_weapon

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def magic_attack(self):
        best_weapon = self.most_magical_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        if self.mana >= 10:
            print("you use {} against {}!".format(best_weapon.name, enemy.name))
            enemy.hp -= best_weapon.magic_value
            self.mana = self.mana - best_weapon.magic_value
            print("You mana is now {}".format(self.mana))
        else:
            print("Your mana is too low to cast anything!")

        if not enemy.is_alive():
            print("You killed the {}".format(enemy.name))
            self.inventory.append(enemy.loot())
        else:
            print("{} HP is {}".format(enemy.name, enemy.hp))

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
            self.inventory.append(enemy.loot())
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)
