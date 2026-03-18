# Conversion de butin de liste en dictionnaire

def add_to_inventory(inventory, added_items):
    """Add list to dictionary

    Args:
        inventory (dict): dictionary of inventory
        added_items (list): table of loot to add to inventory

    Returns:
        dict : dictionary of inventory
    """
    for item in added_items:
        inventory[item]= inventory.get(item,0)+1

    return inventory

def display_inventory(inventory):
    """Display inventory

    Args:
        inventory (dict[str,int]): dictionary with inventory
    """
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count}\t{item}")
        item_total += count

    print(f"Total number of items: {item_total}")


inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
