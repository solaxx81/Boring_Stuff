# Inventaire de jeu de fantasy
"""
La structure de données permettant de modéliser l’inventaire du joueur
est un dictionnaire dont les clés sont des chaînes décrivant l’objet dans
l’inventaire et dont les valeurs sont des nombres entiers détaillant
la quantité de cet objet dont dispose le joueur.
Par exemple, la valeur du dictionnaire
    {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
signifie que le joueur possède one rope, six torches, 42 gold coins, etc.

Écrire une fonction nommée display_inventory() qui prendrait n'importe quel
« inventaire » possible et l'afficherait comme suit :
    Inventory:
    12 arrow
    42 gold coin
    1 rope
    6 torch
    1 dagger
    Total number of items: 62
"""


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


stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}

display_inventory(stuff)
