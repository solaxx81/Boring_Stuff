def collatz(number):
    """Calcule le prochain nombre dans la suite de Collatz."""
    if number % 2 == 0:
        print(number // 2, end=" ")
        return number // 2
    else:
        print(3 * number + 1, end=" ")
        return 3 * number + 1


def collatz_sequence(start_number):
    """Génère la suite de Collatz à partir d'un nombre de départ jusqu'à 1."""
    number = start_number
    while number != 1:
        number = collatz(number)

    print(1)  # Afficher le 1 final


if __name__ == "__main__":
    while True:
        try:
            user_input = input("Entre un nombre entier : ")
            number = int(user_input)
            collatz_sequence(number)
            break  # Sortir de la boucle si l'entrée est valide
        except ValueError:
            print("Erreur : Tu dois entrer un nombre entier, Jean-Yves.")
