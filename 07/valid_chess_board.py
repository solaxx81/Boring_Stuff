# Validateur de dictionnaire d'échecs - chapitre 7 p.156
"""
Vérifie que dans le dictionnaire représentant un échiquier
avec les coordonnées des cases de 1 à 8 et de a à f et
les pièces qui s'y trouvent (P N B R Q K)
correspondent à ces conditions :
   - il y a un roi noir (bK) ET un roi blanc (wK) dans le tableau
   - il ne peut pas y avoir plus de 8 pièces blanches et 8 pièces noires
   - il ne peut pas y avoir plus de 8 points (xP) par couleur
   - le nom des pièces est valide de la forme c(ouleur)T(ype)
   - c étant soir "b" soit "w" et T étant une des lettres P N B R Q K
   - le code des cases doit être valide de a1 à 8f
 Il ne s’agit pas d’une liste exhaustive d’exigences, mais elle est
 suffisamment proche pour cet exercice.
"""


def isValidChessBoard(board):
    """Vérifie la validité du dico représentant un échiquier

    Args:
        board (dict[str]): dictionnaire contenant les paires pièce-position

    Returns:
        boolean : dictionnaire valide ou pas
    """

    piece_blanche = piece_noire = 0
    wP = bP = 0

    if "bK" not in board.values() or "wK" not in board.values():
        return False

    for case, piece in board.items():
        couleur = piece[0]
        type_piece = piece[1]
        if couleur not in ["w", "b"] or type_piece not in ["P", "N", "B", "R", "Q", "K"]:
            return False

        if couleur == "w":
            piece_blanche += 1
            if type_piece == "P":
                wP += 1
        else:
            piece_noire += 1
            if type_piece == "P":
                bP += 1
        if piece_noire > 16 or piece_blanche > 16:
            return False
        if wP > 8 or bP > 8:
            return False

        colonne = case[0]
        ligne = case[1]
        if colonne not in "abcdefgh" or ligne not in "12345678":
            return False

    return True


board_valide = {"h1": "bK", "c8": "wQ", "g2": "bB", "h5": "bQ", "e3": "wK"}
print(isValidChessBoard(board_valide))
board_invalide_1 = {"h1": "bK", "c6": "cQ", "g2": "bB", "h5": "bQ", "e3": "wK"}  # Couleur inexistante (cQ)
print(isValidChessBoard(board_invalide_1))
board_invalide_2 = {"h1": "bP", "c6": "wQ", "g2": "bB", "h5": "bQ", "e3": "wK"}  # Pas de roi noir
print(isValidChessBoard(board_invalide_2))
board_invalide_3 = {"h1": "bK", "c6": "wQ", "g2": "bD", "h5": "bQ", "e3": "wK"}  # Nom pièce inexistant (bD)
print(isValidChessBoard(board_invalide_3))
board_invalide_4 = {"h1": "bK", "c9": "wQ", "g2": "bB", "h5": "bQ", "e3": "wK"}  # Case incohérente (c9)
print(isValidChessBoard(board_invalide_4))

board_invalide_5 = {
    "h1": "bP",
    "c8": "bP",
    "g2": "bP",
    "a5": "bP",
    "h5": "bP",
    "e3": "bP",
    "d4": "bP",
    "f1": "bP",
    "b3": "bP",
    "a6": "wK",
    "b7": "bK",
}  # Trop de pions noirs
print(isValidChessBoard(board_invalide_5))
