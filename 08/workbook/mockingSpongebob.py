# mOcKiNg SpOnGeBoB mEmE - workbook chapitre 8 p.59


def spongecase(text):
    """Transforme une chaîne de caractères en mettant en majuscules une lettre sur deux

    Args:
        text ( str ): Chaîne à transformer

    Returns:
        str : Chaîne transformée
    """
    sponge_text = ""
    make_uppercase = False
    for i in range(len(text)):
        if not text[i].isalpha():
            sponge_text += text[i]
        else:
            if make_uppercase:
                sponge_text += text[i].upper()
            else:
                sponge_text += text[i].lower()
            make_uppercase = not make_uppercase
    return sponge_text


print("Entrez une phrase :")
phrase = input()

print(spongecase(phrase))
