# Coordinate Directions - workbook chapter 6 p.45


def coordonnees(directions):
    """Accepte une liste de directions (N,S,E,O) et retourne des coordonnées cartésiennes

    Args:
        directions (list[str]): liste de directions

    Returns:
        list[int] : coordonnées cartésiennes
    """
    x = 0
    y = 0
    for direction in directions:
        if direction == "E":
            x += 1
        elif direction == "O":
            x -= 1
        elif direction == "N":
            y += 1
        elif direction == "S":
            y -= 1

    return [x, y]


directions = []

while True:
    direction = input("Entrer une direction cardinale E,S,O,N ou 'Entrée' pour quitter : ")
    direction = direction.upper()
    if direction == "":
        break
    if direction in ["E", "S", "O", "N"]:
        directions.append(direction)

print(coordonnees(directions))
