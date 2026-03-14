def spam(divide_by):
    """Divise 42 par un nombre

    Args:
        divide_by (int): diviseur

    Returns:
        float: résultat de la division
    """
    return 42 / divide_by


try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print("Erreur : division par 0.")
