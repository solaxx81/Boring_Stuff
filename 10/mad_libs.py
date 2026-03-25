import re


def mad_libs(input_filename, output_filename):
    # 1. Lecture du contenu du fichier
    try:
        with open(input_filename, encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("Erreur : Le fichier source n'a pas été trouvé.")
        return

    # Liste des mots à chercher
    targets = ["ADJECTIVE", "NOUN", "VERB", "ADVERB"]

    # 2. Analyse et Remplacement
    # On utilise une expression régulière pour trouver les mots-clés
    # La regex \b(ADJECTIVE|NOUN|VERB|ADVERB)\b assure de ne trouver que les mots entiers
    pattern = re.compile(r"\b(ADJECTIVE|NOUN|VERB|ADVERB)\b")

    def replace_match(match):
        word_type = match.group(0)
        # Gestion de l'article pour un meilleur rendu (facultatif mais élégant)
        article = "un" if word_type in ["ADJECTIVE", "ADVERB"] else "un(e)"
        replacement = input(f"Entrez {article} {word_type.lower()} : ")
        return replacement

    # re.sub permet de remplacer chaque occurrence trouvée via une fonction
    new_content = pattern.sub(replace_match, content)

    # 3. Affichage et Sauvegarde
    print("\n--- Résultat final ---\n")
    print(new_content)

    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(new_content)
    print(f"\nLe résultat a été enregistré dans '{output_filename}'.")


# Exemple d'utilisation
# Assurez-vous d'avoir un fichier 'mad_libs_input.txt' dans votre dossier
mad_libs("./10/mad_libs_input.txt", "./10/mad_libs_output.txt")
