#!/usr/bin/python3


"""module to add ints

   Args: a (int) and b (int)

"""


def add_integer(a, b=98):
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")

    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")

    if isinstance(a, float) is True:
        a = int(a)

    if isinstance(b, float) is True:
        b = int(b)

    return a + b
