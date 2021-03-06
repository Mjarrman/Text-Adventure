from collections import OrderedDict
from player import Player
import world


def play():
    print("A Long Journey")

    world.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        player.update_inventory(room.intro_text(player.return_inventory()))
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("You have succumbed to the evils of this world...")


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    action_adder(actions, 'p', player.print_map, 'Print map')

    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Print inventory")
    if player.equip:
        action_adder(actions, 'x', player.equip, "Equip")
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")
    if (isinstance(room, world.EnemyTile) or isinstance(room, world.BlackKnightTile) or isinstance(room, world.BossTile)) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
        action_adder(actions, 'm', player.magic_attack, "Magic attack")

    else:
        if world.tile_at(room.x + 1, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go north")
        if world.tile_at(room.x + 1, room.y + 1):
            action_adder(actions, 's', player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go west")
    if player.hp < 100:
        action_adder(actions, 'h', player.heal, "Heal")
    if player.mana < 100:
        action_adder(actions, 'k', player.regen_mana, 'Mana')
    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


play()
