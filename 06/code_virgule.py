# Code virgule - chapitre 6 p.136


def transfo_liste(liste_entree: list[str]):
    """Transforme une liste en chaîne de caractères avec les virgules
    par exemple :
            spam = ['apples', 'bananas', 'tofu', 'cats']
            spam_str = 'apples, bananas, tofu, and cats'

    Args:
        liste_entree (list[str]): Liste à transformer

    Returns:
        str : Chaîne issue de la liste
    """
    str_liste = ""
    if liste_entree:
        if len(liste_entree)==1:
            return liste_entree[0]
        str_liste = liste_entree[0]
        for entree in range(1, len(liste_entree)-1):
            str_liste = str_liste + ", " + liste_entree[entree]
        str_liste = str_liste + " and " + liste_entree[-1]
        return str_liste
    return "Liste vide"


spam = ["pommes", "bananes", "tofu", "chats"]
eggs = ["dogs","picnic","gland","pommes", "bananes", "tofu", "chats"]
ham=['jambon']
vide = []

print(transfo_liste(spam))
print(transfo_liste(eggs))
print(transfo_liste(ham))
print(transfo_liste(vide))
