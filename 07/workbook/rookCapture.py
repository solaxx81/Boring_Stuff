# Chess Rook Capture Prediction - workbook chapitre 7 p.52


def white_rook_can_capture(rook, board):
    """check if white rook can capture some black pieces

    Args:
        rook ( str ): position of white rook on chessboard
        board ( dict ): piece name and coordinate

    Returns:
        list : coordinates of black pieces that can be captured
    """
    can_capture: list[str] = []
    rook_row = rook[1]
    rook_col = rook[0]

    for pos, piece in board.items():
        if (pos[1] == rook_row or pos[0] == rook_col) and piece[0] == "b":
            can_capture.append(pos)

    return can_capture


print(white_rook_can_capture("d3", {"d7": "bQ", "d2": "wB", "f1": "bP", "a3": "bN"}))
