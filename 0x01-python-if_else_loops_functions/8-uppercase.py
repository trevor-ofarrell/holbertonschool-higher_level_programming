#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        return True
    return False


def uppercase(str):
    c = 0
    for i in str:
        if islower(i):
            c = 32
        else:
            c = 0
        print('{:c}'.format(ord(i) - c), end="")
    print(" ")
