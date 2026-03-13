# Feuille - Pierre - Ciseaux chapitre 3 p.67
import random
import sys

gagne = 0
perdu = 0
egalite = 0
choix_machine=""

while True:
    print(f"\n{gagne} victoire(s), {perdu} défaite(s), {egalite} égalité(s).")

    joueur = input("Votre choix : (f)euille (p)ierre (c)iseaux (q)uitter : ")
    if joueur == "q":
        sys.exit()
    elif joueur == "f":
        print("Feuille contre ...")
    elif joueur == "p":
        print("Pierre contre ...")
    elif joueur == "c":
        print("Ciseaux contre ...")

    random_number = random.randint(1, 3)
    if random_number == 1:
        choix_machine = "f"
        print("Feuille")
    elif random_number == 2:
        print('Pierre')
        choix_machine = "p"
    elif random_number == 3:
        print('Ciseaux')
        choix_machine = "c"

    if joueur=='f' and choix_machine=='f':
        egalite+=1
        print("Égalité")
    elif joueur=='f' and choix_machine=='p':
        gagne+=1
        print("Gagné")
    elif joueur=='f' and choix_machine=='c':
        perdu+=1
        print("Perdu")
    elif joueur == "p" and choix_machine == "p":
        egalite += 1
        print("Égalité")
    elif joueur == "p" and choix_machine == "c":
        gagne += 1
        print("Gagné")
    elif joueur == "p" and choix_machine == "f":
        perdu += 1
        print("Perdu")
    elif joueur == "c" and choix_machine == "c":
        egalite += 1
        print("Égalité")
    elif joueur == "c" and choix_machine == "f":
        gagne += 1
        print("Gagné")
    elif joueur == "c" and choix_machine == "p":
        perdu += 1
        print("Perdu")
