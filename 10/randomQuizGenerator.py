# randomQuizGenerator.py - Inspiré de 'Automate the Boring Stuff' p.235

import random

departements_prefectures = {
    "Ain": "Bourg-en-Bresse",
    "Aisne": "Laon",
    "Allier": "Moulins",
    "Alpes-de-Haute-Provence": "Digne-les-Bains",
    "Hautes-Alpes": "Gap",
    "Alpes-Maritimes": "Nice",
    "Ardèche": "Privas",
    "Ardennes": "Charleville-Mézières",
    "Ariège": "Foix",
    "Aube": "Troyes",
    "Aude": "Carcassonne",
    "Aveyron": "Rodez",
    "Bouches-du-Rhône": "Marseille",
    "Calvados": "Caen",
    "Cantal": "Aurillac",
    "Charente": "Angoulême",
    "Charente-Maritime": "La Rochelle",
    "Cher": "Bourges",
    "Corrèze": "Tulle",
    "Corse-du-Sud": "Ajaccio",
    "Haute-Corse": "Bastia",
    "Côte-d'Or": "Dijon",
    "Côtes-d'Armor": "Saint-Brieuc",
    "Creuse": "Guéret",
    "Dordogne": "Périgueux",
    "Doubs": "Besançon",
    "Drôme": "Valence",
    "Eure": "Évreux",
    "Eure-et-Loir": "Chartres",
    "Finistère": "Quimper",
    "Gard": "Nîmes",
    "Haute-Garonne": "Toulouse",
    "Gers": "Auch",
    "Gironde": "Bordeaux",
    "Hérault": "Montpellier",
    "Ille-et-Vilaine": "Rennes",
    "Indre": "Châteauroux",
    "Indre-et-Loire": "Tours",
    "Isère": "Grenoble",
    "Jura": "Lons-le-Saunier",
    "Landes": "Mont-de-Marsan",
    "Loir-et-Cher": "Blois",
    "Loire": "Saint-Étienne",
    "Haute-Loire": "Le Puy-en-Velay",
    "Loire-Atlantique": "Nantes",
    "Loiret": "Orléans",
    "Lot": "Cahors",
    "Lot-et-Garonne": "Agen",
    "Lozère": "Mende",
    "Maine-et-Loire": "Angers",
    "Manche": "Saint-Lô",
    "Marne": "Châlons-en-Champagne",
    "Haute-Marne": "Chaumont",
    "Mayenne": "Laval",
    "Meurthe-et-Moselle": "Nancy",
    "Meuse": "Bar-le-Duc",
    "Morbihan": "Vannes",
    "Moselle": "Metz",
    "Nièvre": "Nevers",
    "Nord": "Lille",
    "Oise": "Beauvais",
    "Orne": "Alençon",
    "Pas-de-Calais": "Arras",
    "Puy-de-Dôme": "Clermont-Ferrand",
    "Pyrénées-Atlantiques": "Pau",
    "Hautes-Pyrénées": "Tarbes",
    "Pyrénées-Orientales": "Perpignan",
    "Bas-Rhin": "Strasbourg",
    "Haut-Rhin": "Colmar",
    "Rhône": "Lyon",
    "Haute-Saône": "Vesoul",
    "Saône-et-Loire": "Mâcon",
    "Sarthe": "Le Mans",
    "Savoie": "Chambéry",
    "Haute-Savoie": "Annecy",
    "Paris": "Paris",
    "Seine-Maritime": "Rouen",
    "Seine-et-Marne": "Melun",
    "Yvelines": "Versailles",
    "Deux-Sèvres": "Niort",
    "Somme": "Amiens",
    "Tarn": "Albi",
    "Tarn-et-Garonne": "Montauban",
    "Var": "Toulon",
    "Vaucluse": "Avignon",
    "Vendée": "La Roche-sur-Yon",
    "Vienne": "Poitiers",
    "Haute-Vienne": "Limoges",
    "Vosges": "Épinal",
    "Yonne": "Auxerre",
    "Territoire de Belfort": "Belfort",
    "Essonne": "Évry-Courcouronnes",
    "Hauts-de-Seine": "Nanterre",
    "Seine-Saint-Denis": "Bobigny",
    "Val-de-Marne": "Créteil",
    "Val-d'Oise": "Pontoise",
    "Guadeloupe": "Basse-Terre",
    "Martinique": "Fort-de-France",
    "Guyane": "Cayenne",
    "La Réunion": "Saint-Denis",
    "Mayotte": "Mamoudzou",
}

# Génère 20 fichiers de quiz
for num_quiz in range(20):
    # Crée les fichiers de questions et réponses
    quiz_file = open(f"prefs_quiz{num_quiz + 1}.txt", "w", encoding="UTF-8")
    reponse_file = open(f"prefs_quiz_reponses{num_quiz + 1}.txt", "w", encoding="UTF-8")

    # Écrit l'entête du quiz.
    quiz_file.write("Nom : \n\nDate : \n\n")
    quiz_file.write((" " * 20) + f"Quiz Préfectures des départements (Questionnaire {num_quiz + 1})")
    quiz_file.write("\n\n")

    # Mélange l'ordre des départements
    departements = list(departements_prefectures.keys())
    random.shuffle(departements)

    for num in range(100):
        # Scan les départements et crée une question pour chaque
        bonne_reponse = departements_prefectures[departements[num]]
        mauvaises_reponses = list(departements_prefectures.values())
        del mauvaises_reponses[mauvaises_reponses.index(bonne_reponse)]
        mauvaises_reponses = random.sample(mauvaises_reponses, 3)
        choix_reponses = mauvaises_reponses + [bonne_reponse]
        random.shuffle(choix_reponses)

        # Écrit la question et le choix de réponses dans le fichier quiz
        quiz_file.write(f"{num + 1}. Préfecture du département {departements[num]} : \n")
        for i in range(4):
            quiz_file.write(f"{'ABCD'[i]}. {choix_reponses[i]}\n")
        quiz_file.write("\n")

        # Écrit la réponse dans un fichier
        reponse_file.write(f"{num + 1}. {'ABCD'[choix_reponses.index(bonne_reponse)]}\n")
quiz_file.close()
reponse_file.close()
