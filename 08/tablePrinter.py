# Table Printer - chapitre 8 p.181


def get_colWidths(tableData: list[list[str]]):
    """Calcule la plus grande largeur de chaque colonne

    Args:
        tableData (list[list[str]]): Liste le listes

    Returns:
        list[int] : list of max widths
    """

    colWidths = [0] * len(tableData)
    list_number = 0
    for data in tableData:
        greater = 0
        for word in data:
            if len(word) > greater:
                greater = len(word)
        colWidths[list_number] = greater
        list_number += 1
    return colWidths


def printTable(tableData):
    """Affiche une liste de listes en colonne alignées à droite.

    Args:
        tableData (list[list]): Liste de listes à aligner
        colWidths (list[int]) : largeurs max de chaque colonne
    """
    rows = len(tableData)
    cols = len(tableData[0])

    for r in range(cols):
        string = ""
        for c in range(rows):
            word = tableData[c][r]
            string += word.rjust(colWidths[c]) + " "

        print(string)


tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alicia", "Bob", "Carol", "David"],
    ["dogs", "cats", "elephant", "goose"],
]

colWidths = get_colWidths(tableData)

printTable(tableData)
