def a():
    """Fonction a"""
    print("a() starts")
    b()
    d()
    print("a() returns")


def b():
    """Fonction b"""
    print("b() starts")
    c()
    print("b() returns")


def c():
    """Fonction c"""
    print("c() starts")
    print("c() returns")


def d():
    """Fonction d"""
    print("d() starts")
    print("d() returns")


a()
