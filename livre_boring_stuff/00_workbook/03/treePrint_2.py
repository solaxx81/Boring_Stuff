taille = int(input("Entrer la taille de l'arbre : "))
rang=0

while rang <= taille:
    espaces = " " * (taille - rang)
    feuilles = "^" * (rang * 2 - 1)
    print(f"{espaces}{feuilles}")
    rang+=1

espaces = " " * (taille - 1)
print(f"{espaces}#")
print(f"{espaces}#")
