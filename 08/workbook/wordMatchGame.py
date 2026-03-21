# Word Match Game - workbook chapitre 8 p.57
import random
import sys


def get_word_hint(secret_word, guess_word):
    """Retourne les indices de position de lettres dans un mot caché

    Args:
        secret_word ( str ): Mot à deviner
        guess_word ( str ): Tentative de mot

    Returns:
        str : indice décrivant les lettres bien et mal placées
    """
    hint = ""

    for i in range(5):
        if guess[i] in secret:
            if guess[i]==secret[i]:
                hint+='O'
            else:
                hint+='o'
        else:
            hint+='x'
    return hint


secret = random.choice(
    ["table", "arbre", "liste", "froid", "ombre", "blanc", "court", "image", "chant", "livre", "porte", "place"]
)

tentatives = 0
while tentatives < 6:
    guess = input("Entrer un mot de 5 lettres : ")
    guess=guess.lower()
    if not guess.isalpha() or len(guess) != 5:
        print("Mot incorrect")
        continue
    tentatives += 1
    if guess == secret:
        print(f"Vous avez trouvé le mot secret en {tentatives} essais.")
        sys.exit()
    print(get_word_hint(secret, guess))

print(f"\nPerdu ! Le mot était : {secret.upper()}.")
