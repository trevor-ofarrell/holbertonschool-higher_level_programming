#!/usr/bin/python3
def add_integer(a, b=98):
    if isinstance(a, (int, float)) == False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) == False:
        raise TypeError("b must be an integer")
    if isinstance(a, float) == True:
        a = int(a)
    if isinstance(b, float) == True:
        b = int(b)
    ssum = a + b
    return ssum
