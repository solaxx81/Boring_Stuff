# Diagonal Stripe Scroll Animation - workbook chapitre 8 p.58
import sys
import time

try:
    while True:
        for i in range(50):
            print("O" * i + "." * (50 - i))
            time.sleep(0.01)
        for i in range(50):
            print("." * i + "O" * (50 - i))
            time.sleep(0.01)

except KeyboardInterrupt:
    sys.exit()
