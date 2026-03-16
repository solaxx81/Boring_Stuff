# Série de lancers de pièces - chapitre 6 p.137

import random

"""
Détermine à quelle fréquence une séquence de six "pile" ou de six "face"
apparaît dans une liste générée aléatoirement de 100 pile et face.
Expérience à renouveler 10000 fois.
"""
nombre_de_series = 0

for _ in range(10000):  # Lance 10,000 fois l'expérience.
    # Code qui crée une liste de 100 'pile' ou 'faces'
    sequence = []
    for _ in range(100):
        sequence.append(random.choice(["P", "F"]))

    # Code that checks if there is a streak of 6 heads or tails in a row

    longueur_serie = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            longueur_serie += 1
        else:
            longueur_serie = 1

        if longueur_serie >= 6:
            nombre_de_series += 1
            break

print(f"Chance de série : {nombre_de_series / 100} %")

