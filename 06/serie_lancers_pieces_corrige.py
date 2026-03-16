import random

number_of_streaks = 0

for _ in range(10000):
    # Générer une liste de 100 'H' et 'T'
    sequence = [random.choice(["H", "T"]) for _ in range(100)]

    # Vérifier s'il y a une séquence de six 'H' ou 'T' d'affilée
    streak_length = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            streak_length += 1
        else:
            streak_length = 1

        if streak_length >= 6:
            number_of_streaks += 1
            break

print("Chance of streak: %s%%" % (number_of_streaks / 100))
