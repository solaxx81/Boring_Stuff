def is_leap_year(year):
    """Vérifie année bissextile"""
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False


while True:
    print('Enter a year or "done":')
    response = input()
    if response == "done":
        break
    print("Is leap year:", is_leap_year(int(response)))
