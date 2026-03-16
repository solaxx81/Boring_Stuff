# Code virgule - chapitre 6 p.136


def transfo_liste(liste_entree: list[str]):
    """Transforme une liste en chaîne de caractères avec les virgules
    par exemple :
            spam = ['apples', 'bananas', 'tofu', 'cats']
            spam_str = 'apples, bananas, tofu, et cats'

    Args:
        liste_entree (list[str]): Liste à transformer

    Returns:
        str : Chaîne issue de la liste
    """

    if liste_entree == []:
        return "Liste vide"

    if len(liste_entree) == 1:
        return liste_entree[0]

    return ", ".join(liste_entree[:-1]) + " et " + liste_entree[-1]


spam = ["pommes", "bananes", "tofu", "chats"]
eggs = ["chiens", "picnic", "gland", "pommes", "bananes", "tofu", "chats"]
ham = ["jambon"]
vide = []

print(transfo_liste(spam))
print(transfo_liste(eggs))
print(transfo_liste(ham))
print(transfo_liste(vide))
