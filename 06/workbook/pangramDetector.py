# Pangram Detector - workbook chapter 6 p.44


def est_pangram(phrase):
    """Détermine si la phrase est un pangramme

    Args:
        phrase ( str ): Phrase à vérifier

    Return:
        boolean : Pangramme ou non
    """

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lettres_phrases = []

    for lettre in phrase:
        lettre = lettre.upper()
        if lettre in ALPHABET and lettre not in lettres_phrases:
            lettres_phrases.append(lettre)

    if len(lettres_phrases) == 26:
        return True
    else:
        return False


phrase = "The quick brown fox jumps over the yellow lazy dog."
if est_pangram(phrase):
    print(f"\n{phrase}\nCette phrase est un pangramme.")
else:
    print(f"\n{phrase}\nCette phrase n'est pas un pangramme.")

phrase = "Portez ce vieux whisky au juge blond qui fume."
if est_pangram(phrase):
    print(f"\n{phrase}\nCette phrase est un pangramme.")
else:
    print(f"\n{phrase}\nCette phrase n'est pas un pangramme.")

phrase = "Voyez le brick géant que j’examine près du wharf."
if est_pangram(phrase):
    print(f"\n{phrase}\nCette phrase est un pangramme.")
else:
    print(f"\n{phrase}\nCette phrase n'est pas un pangramme.")
