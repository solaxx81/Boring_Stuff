import random

taille = int(input("Entrer la taille de l'arbre : "))

for rang in range(1, taille + 1):
    espaces = " " * (taille - rang)
    feuilles = ""
    for _ in range(rang * 2 - 1):
        if random.random() < 0.2:
            feuilles += "o"
        else:
            feuilles += "^"
    print(f"{espaces}{feuilles}")

espaces = " " * (taille - 1)
print(f"{espaces}#")
print(f"{espaces}#")
