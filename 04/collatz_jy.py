# Calcul de la séquence de collatz chapitre 4 p.94
import sys


def collatz(nombre):
    """Calcule le prochain nombre de la suite de Collatz.

    Args:
        nombre (int): Le nombre de départ.

    Returns:
        int: Le prochain nombre de la suite.
    """
    if nombre % 2 == 0:
        print(nombre // 2, end=" ")
        return nombre // 2
    else:
        print(nombre * 3 + 1, end=" ")
        return nombre * 3 + 1


nombre = 0

try:
    nombre_depart = int(input("Entrer un nombre entier : "))
    nombre = collatz(nombre_depart)
    while nombre != 1:
        nombre = collatz(nombre)

except ValueError:
    print("Le nombre entré n'est pas valide.")
    sys.exit()
