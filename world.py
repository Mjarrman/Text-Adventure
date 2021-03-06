import enemies
import npc
import random
import items
import time
from items import QuestItem


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self, player_inventory):
        raise NotImplementedError("Create a subclass instead!")
        # noinspection PyUnreachableCode
        return player_inventory

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self, player_inventory):
        print("You are on your way home from a long campaign in the hinterlands,\n" 
              " as you are walking down the path you come to a cross roads.\n" 
              " you can go any of four directions.")
        return player_inventory


class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.randint(0, 5)
        if r <= 1:
            self.enemy = enemies.GiantSpider()
            self.alive_text = "A giant spider jumps down from\nit's web down in front of you!"
            self.dead_text = "The corpse of a dead spider\nrots on the ground"

        elif r <= 2:
            self.enemy = enemies.Ogre()
            self.alive_text = "An ogre is blocking your path!"
            self.dead_text = "A dead ogre reminds you of your triumph."

        elif r <= 3:
            self.enemy = enemies.BatColony()
            self.alive_text = "You hear a squeaking noise growing louder\nsuddenly you are lost in a swarm of bats!"
            self.dead_text = "Dozens of dead bats are scattered on the ground."

        else:
            self.enemy = enemies.RockMonster()
            self.alive_text = "You've disturbed a rock monster!"
            self.dead_text = "Defeated, the monster has gone into a deep hibernation and appears to be a normal rock."

        super().__init__(x, y)

    def intro_text(self, player_inventory):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        print(text)
        return player_inventory

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage / (player.defence / 2)
            print("Enemy does {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.hp))


class BlackKnightTile(MapTile):
    def __init__(self, x, y):
        self.chance = random.randint(0, 5)
        self.enemy = enemies.BlackKnight()
        self.alive_text = "A black knight charges at you!"
        self.dead_text = "With a piercing wail the black knight crumbles to ash before you."

        super().__init__(x, y)

    def intro_text(self, player_inventory):
        if self.chance >= 2.5:
            text = self.alive_text if self.enemy.is_alive() else self.dead_text
            print(text)
            return player_inventory
        else:
            print("There is nothing here but a deep sense of dread,\n"
                  "perhaps you just missed a powerful enemy...")

    def modify_player(self, player):
        if self.enemy.is_alive() and self.chance >= 2.5:
            player.hp = player.hp - self.enemy.damage / (player.defence / 2)
            print("Enemy does {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.hp))


class BossTile(MapTile):
    def __init__(self, x, y):
        self.enemy = enemies.HulkingBeast()
        self.alive_text = "A hulking monstrosity looms before you! With a piercing screech it leaps at you!"
        self.dead_text = "With a final wail, the Hulking Beast falls before your might"
        super().__init__(x, y)

    def intro_text(self, player_inventory):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        print(text)
        return player_inventory

    def modify_player(self, player):
        if self.enemy.is_alive:
            player.hp = player.hp - self.enemy.damage / (player.defence / 2)
            print("Enemy does {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.hp))


class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self, player_inventory):
        print("You have made it home to your loved ones, well done!")
        return player_inventory


class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self, player_inventory):
        if self.gold_claimed:
            print("Another abandoned camp, best to move on.")
        else:
            print("Some unlucky soul left his worldly possessions behind, you find some gold among the tatters")
        return player_inventory


class StoryTileOne(MapTile, QuestItem):
    def intro_text(self, player_inventory):
        item_check = [item for item in player_inventory if isinstance(item, items.SmallCoin)]
        if not item_check:
            print("You walk into a ruined village, raided by gods knows what.\n"
                  "Among the wreckage you find a small coin.\n"
                  "Inscribed upon it are three unreadable runes.\n"
                  "Perhaps a wizard could read them.")
            player_inventory.append(items.SmallCoin())
            print("You have acquired a small coin.")
            return player_inventory
        else:
            print("You have already been through this village, it is where you found the small coin")


class StoryTileTwo(MapTile, QuestItem):
    def intro_text(self, player_inventory):
        item_check = [item for item in player_inventory if isinstance(item, items.SmallCoin)]
        if item_check:
            print("You see a strange figure in the distance.\n"
                  "As you walk closer, you realize it is a wizard.\n"
                  " Perhaps they can read the runes on the small coin you found.")
            time.sleep(2)
            print("The wizard says 'the runes say, go north-east to find a great treasure...'")
        else:
            print("You see a strange figure in the distance.\n"
                  "As you walk closer, you realize it is a wizard.\n")
            time.sleep(2)
            print("The wizard shouts. 'You have no business with me!'")
        return player_inventory


class StoryTileThree(MapTile, QuestItem):
    def __init__(self, x, y):
        self.jewel_claimed = 0
        self.x = x
        self.y = y
        super().__init__(x, y)

    def intro_text(self, player_inventory):
        item_check = [item for item in player_inventory if isinstance(item, items.SmallCoin)]
        if not item_check and not self.jewel_claimed:
            print("An empty clearing, maybe you need something for it to be of use to you...")
        elif item_check and not self.jewel_claimed:
            player_inventory.append(items.Jewel())
            self.jewel_claimed = 1
            print("You have found an ancient treasure!")
            time.sleep(1.5)
            print("Small Coin was removed")
            new_player_inv = []
            for item in player_inventory:
                if not isinstance(item, items.SmallCoin):
                    new_player_inv.append(item)
            player_inventory = new_player_inv
        elif self.jewel_claimed:
            print("An empty clearing where you found an ancient treasure...")
        return player_inventory


class StoryTileFour(MapTile, QuestItem):

    def __init__(self, x, y):
        self.check = 0
        self.x = x
        self.y = y
        super().__init__(x, y)

    def intro_text(self, player_inventory):
        item_check = [item for item in player_inventory if isinstance(item, items.WoodenKey)]
        if not item_check and not self.check:
            self.check = 1
            print("You are walking through a thick forest,\n"
                  "There are gnarled oaks all throughout.\n"
                  "as you walk into a small clearing you see an oak that is bigger than the rest.\n"
                  "You walk up to the ancient oak you hear a voice whisper...\n")
            time.sleep(2)
            print("'You must find the ancient key to open our secrets....'")
            print("'Go west to find the key...'")
        else:
            print("You have spoken to the forest spirits already, go west to find the key...")
        return player_inventory

    def modify_player(self, player):
        pass


class StoryTileFive(MapTile, QuestItem):
    def intro_text(self, player_inventory):
        item_check = [item for item in player_inventory if isinstance(item, items.WoodenKey)]
        if not item_check:
            print("You approach a glade of trees, as you walk closer they\n "
                  "seem to move of their own accord and open up to you\n"
                  "You see a small key emerging from the trunk of the central tree.\n"
                  "You take the key. As you take the key the forest spirits whisper\n"
                  " to you, ")
            time.sleep(2)
            print("'go south to find a great weapon...'")
            player_inventory.append(items.WoodenKey())
            print("You have found the Wooden Key!")
            return player_inventory
        else:
            print("A glade of trees where you found the small Wooden Key")


class StoryTileSix(MapTile, QuestItem):
    def __init__(self, x, y):
        self.wand_claimed = 0
        self.x = x
        self.y = y
        super().__init__(x, y)

    def intro_text(self, player_inventory):
        item_check = [item for item in player_inventory if isinstance(item, items.WoodenKey)]
        if not item_check and not self.wand_claimed:
            print("A small grove of trees, maybe you need something for it to be of use to you...")
        elif item_check and not self.wand_claimed:
            player_inventory.append(items.FabledWand())
            self.wand_claimed = 1
            print("The spirits whisper 'You have found the key!',\n"
                  " open the tree of light to receive your reward!")
            time.sleep(1.5)
            print("You have found the fabled wand!")
            time.sleep(1.5)
            print("Wooden Key has been removed")
            new_player_inv = []
            for item in player_inventory:
                if not isinstance(item, items.WoodenKey):
                    new_player_inv.append(item)
            player_inventory = new_player_inv
        elif self.wand_claimed:
            print("A stand of trees where you found an ancient weapon...")
        return player_inventory

# Make mountains unpassable


class MountainTile(MapTile):
    def intro_text(self, player_inventory):
        print("Unpassable mountains...")

    def modify_player(self, player):
        pass


class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        while True:
            for i, item in enumerate(seller.inventory, 1):
                print("{}. {} - {} Gold".format(i, item.name, item.value))
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError or IndexError:
                    print("Invalid choice!")

    @staticmethod
    def swap(seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return

        elif item.value <= 1:
            print("Nobody wants to buy that!")
        elif item.value >= 1:
            seller.inventory.remove(item)
            buyer.inventory.append(item)
            seller.gold = seller.gold + item.value
            buyer.gold = buyer.gold - item.value
            print("Trade complete!")

    def intro_text(self, player_inventory):
        print("A frail not-quite human, not-quite-creature\n"
              "squats in the corner clinking his gold coins\n"
              " together. He looks willing to trade.")
        return player_inventory


world_dsl = """
|FG|EN|EN|EN|EN|EN|FG|EN|EN|FG|S3|
|EN|TT|FG|EN|TT|FG|KT|EN|EN|FG|EN|
|EN|FG|EN|EN|EN|EN|FG|FG|EN|EN|EN|
|EN|EN|ST|EN|EN|S2|EN|EN|FG|KT|FG|
|S5|KT|S4|FG|EN|EN|FG|FG|EN|TT|EN|
|EN|EN|EN|EN|FG|S1|EN|MT|MT|KT|MT|
|KT|FG|EN|EN|EN|FG|FG|MT|KT|KT|KT|
|S6|TT|EN|EN|TT|EN|FG|MT|MT|BT|MT|
|EN|EN|FG|KT|FG|EN|KT|MT|MT|VT|MT|
"""


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True


tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "S1": StoryTileOne,
                  "S2": StoryTileTwo,
                  "S3": StoryTileThree,
                  "S4": StoryTileFour,
                  "S5": StoryTileFive,
                  "S6": StoryTileSix,
                  "MT": MountainTile,
                  "KT": BlackKnightTile,
                  "BT": BossTile,
                  "  ": None}

world_map = []

start_tile_location = None


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
