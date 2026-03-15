# Arithmetic Functions Without Arithmetic Operators - workbook chapter 4 p.31


def add(number1, number2):
    """Add 2 numbers without using '+' operator

    Args:
        number1 (int): first number to add
        number2 (int): second number to add

    Returns:
        int: sum of numbers
    """
    total_sum = number1
    for _ in range(number2):
        total_sum = plus_one(total_sum)
    return total_sum


def multiply(number1, number2):
    """Multiply 2 numbers without using '*' operator

    Args:
        number1 (int): first number to multiply
        number2 (int): second number to multiply

    Returns:
        int: product of numbers
    """
    total_multiply = 0
    for _ in range(number2):
        total_multiply = add(total_multiply, number1)
    return total_multiply


def plus_one(number):
    """Add 1 to number"""
    return number + 1


print(add(24, 12))
print(multiply(4, 12))
