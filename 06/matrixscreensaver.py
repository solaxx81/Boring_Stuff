import random
import sys
import time

WIDTH = 70  # nombre de colonnes

try:
    # For each column, when the counter is 0, no stream is shown.
    # Otherwise, it acts as a counter for how many times a 1 or 0
    # should be displayed in that column.
    columns = [0] * WIDTH  # Crée un tableau de 0 de la largeur définie
    while True:
        for i in range(WIDTH):
            if random.random() < 0.02:
                # Restart a stream counter on this column.
                # The stream length is between 4 and 14 characters long.
                columns[i] = random.randint(4, 14)

            if columns[i] == 0:
                # Change this ' '' to '.' to see the empty spaces:
                print(" ", end="")
            else:
                # Print 0 or 1
                print(random.choice([0, 1]), end="")
                columns[i] -= 1
        print()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
