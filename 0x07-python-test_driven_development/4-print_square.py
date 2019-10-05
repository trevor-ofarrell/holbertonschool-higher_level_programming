#!/usr/bin/python3


"""module to print square based on area data

   Args - size (int) size to calculate area with

"""


def print_square(size):
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")

    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >=")

    for i in range(size):
        for i in range(size):
            print("#", end="")
        print("")
