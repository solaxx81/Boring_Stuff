# Tick Tock - workbook chapter 4 p.32

import time


def tic_tac(seconds):
    """Affiche tic tac

    Args:
        seconds (int_): temps d'affichage de tic-tac
    """

    tic_ou_tac = "Tic ..."
    for _ in range(seconds):
        print(tic_ou_tac)
        time.sleep(1)
        if tic_ou_tac == "Tic ...":
            tic_ou_tac = "Tac ..."
        else:
            tic_ou_tac = "Tic ..."


tic_tac(4)
