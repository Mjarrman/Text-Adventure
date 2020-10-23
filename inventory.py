import items

player_inventory = [items.Rock(), items.WoodenShield(), items.Dagger(), items.Fist(), items.CrustyBread(),
                    items.CrustyBread(), items.Apple(), items.StickWand()]


def get_inventory():
    return player_inventory


def get_player_inventory(item):
    player_inventory.append(item)