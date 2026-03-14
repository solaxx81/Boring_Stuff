def spam():
    """Variable globale"""
    global eggs
    eggs = "spam"  # This is the global variable.


def bacon():
    """Variable locale"""
    eggs = "bacon"  # This is a local variable.


def ham():
    """Variable globale"""
    print(eggs)  # This is the global variable.


eggs = "global"  # This is the global variable.
spam()
print(eggs)
