#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            c = 32
        else:
            c = 0
        print('{:c}'.format(ord(i) - c), end="")
    print(" ")
